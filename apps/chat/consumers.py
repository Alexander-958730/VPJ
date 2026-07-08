"""
APPS.CHAT.CONSUMERS
===================
WebSocket consumers para el sistema de chat en tiempo real de VPJ.

Este módulo contiene la lógica de conexión WebSocket que permite:
- Comunicación bidireccional en tiempo real entre usuarios
- Supervisión de chats por ONPECO y Centro de Acopio (solo lectura)
- Chat privado ONPECO ↔ Centro de Acopio

Tecnologías:
- channels (Django Channels): Manejo de WebSockets
- AsyncWebsocketConsumer: Consumer asíncrono para WebSockets
- database_sync_to_async: Operaciones síncronas de BD en contexto asíncrono

Roles de usuario:
- consumidor: Puede enviar y recibir mensajes en sus chats
- productor: Puede enviar y recibir mensajes en sus chats
- regulador (ONPECO): Supervisa chats (solo lectura) y chat privado con Acopio
- acopio (Centro de Acopio): Supervisa chats y chat privado con ONPECO
"""

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async


# =============================================================================
# CONSUMER: ChatConsumer
# =============================================================================
# Propósito: Maneja las conexiones WebSocket para el chat en tiempo real.
# Gestiona la conexión, desconexión, recepción y envío de mensajes.
#
# Group naming:
#   - Formato: chat_{room_id}
#   - Ejemplo: chat_123
#
# Modos:
#   - Normal: Participantes (productor/consumidor) pueden enviar y recibir
#   - Supervisión: ONPECO/Acopio pueden ver pero NO enviar (excepto chat privado)
#   - Privado: Chat exclusivo ONPECO ↔ Acopio (con envío permitido)
#
# Flujo de conexión:
#   1. Usuario se conecta a la URL /ws/chat/<room_id>/
#   2. Verificar autenticación del usuario
#   3. Verificar acceso al chat (participante o supervisor)
#   4. Unirse al grupo WebSocket
#   5. Aceptar la conexión
# =============================================================================
class ChatConsumer(AsyncWebsocketConsumer):
    """
    Consumer WebSocket para el chat en tiempo real
    """
    
    # ============================================================
    # CONEXIÓN
    # ============================================================
    async def connect(self):
        """
        Maneja la conexión WebSocket entrante.
        
        Flujo:
            1. Obtener room_id de la URL
            2. Verificar autenticación del usuario
            3. Verificar acceso al chat
            4. Determinar modo (normal, supervisión, privado)
            5. Unirse al grupo y aceptar conexión
        """
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = f'chat_{self.room_id}'
        
        user = self.scope['user']
        
        # ============================================================
        # 1. VERIFICAR AUTENTICACIÓN
        # ============================================================
        if user.is_anonymous:
            await self.close()
            return
        
        # ============================================================
        # 2. VERIFICAR ACCESO AL CHAT
        # ============================================================
        chat_info = await self.get_chat_info()
        
        if chat_info is None:
            await self.close()
            return
        
        # ============================================================
        # 3. DETERMINAR SI ES SUPERVISOR
        # ============================================================
        is_supervisor = user.role == 'regulador' or user.is_superuser or user.username == 'centro_acopio'
        
        # Si es supervisor y NO es el chat privado ONPECO-Acopio → SUPERVISIÓN
        if is_supervisor and not chat_info['is_private']:
            await self.channel_layer.group_add(self.room_group_name, self.channel_name)
            await self.accept()
            
            # Mensaje de bienvenida informando que es solo lectura
            await self.send(text_data=json.dumps({
                'type': 'system',
                'message': '🔍 Modo supervisión - Solo lectura. No puedes enviar mensajes.'
            }))
            return
        
        # Si es supervisor y ES el chat privado ONPECO-Acopio
        if is_supervisor and chat_info['is_private']:
            # Verificar que sea participante (ONPECO o Acopio)
            if not chat_info['is_participant']:
                await self.close()
                return
            # Unirse al chat privado
            await self.channel_layer.group_add(self.room_group_name, self.channel_name)
            await self.accept()
            return
        
        # ============================================================
        # 4. USUARIO NORMAL (PRODUCTOR O CONSUMIDOR)
        # ============================================================
        # Verificar que sea participante
        if not chat_info['is_participant']:
            await self.close()
            return
        
        # Unirse al chat normal
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()
    
    # ============================================================
    # DESCONEXIÓN
    # ============================================================
    async def disconnect(self, close_code):
        """
        Maneja la desconexión WebSocket.
        Elimina al usuario del grupo.
        """
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
    
    # ============================================================
    # RECEPCIÓN DE MENSAJES
    # ============================================================
    async def receive(self, text_data):
        """
        Procesa mensajes recibidos desde el cliente WebSocket.
        
        Flujo:
            1. Verificar autenticación del usuario
            2. Verificar permisos de envío (supervisores no pueden enviar)
            3. Guardar el mensaje en la base de datos
            4. Transmitir el mensaje a todos los miembros del grupo
        """
        user = self.scope['user']
        
        # ============================================================
        # 1. VERIFICAR SI ES SUPERVISOR
        # ============================================================
        is_supervisor = user.role == 'regulador' or user.is_superuser or user.username == 'centro_acopio'
        
        # Obtener información del chat
        chat_info = await self.get_chat_info()
        
        if chat_info is None:
            await self.send(text_data=json.dumps({
                'type': 'error',
                'message': '⛔ Chat no encontrado.'
            }))
            return
        
        # ============================================================
        # 2. BLOQUEAR ENVÍO DE MENSAJES A SUPERVISORES (excepto chat privado)
        # ============================================================
        if is_supervisor and not chat_info['is_private']:
            await self.send(text_data=json.dumps({
                'type': 'error',
                'message': '⛔ No tienes permiso para enviar mensajes en este chat (modo supervisión).'
            }))
            return
        
        # Si es supervisor y es chat privado, permitir enviar
        if is_supervisor and chat_info['is_private']:
            # Verificar que sea participante
            if not chat_info['is_participant']:
                await self.send(text_data=json.dumps({
                    'type': 'error',
                    'message': '⛔ No tienes permiso para enviar mensajes aquí.'
                }))
                return
        
        # ============================================================
        # 3. PROCESAR EL MENSAJE
        # ============================================================
        try:
            data = json.loads(text_data)
            message = data.get('message', '').strip()
            
            if not message:
                return
            
            # Guardar mensaje en la base de datos
            saved_message = await self.save_message(message)
            
            # Transmitir el mensaje a todos en el grupo
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'username': self.scope['user'].username,
                    'timestamp': saved_message['timestamp'],
                }
            )
        except json.JSONDecodeError:
            await self.send(text_data=json.dumps({
                'type': 'error',
                'message': '⛔ Error al procesar el mensaje.'
            }))
    
    # ============================================================
    # ENVÍO DE MENSAJES (group_send handler)
    # ============================================================
    async def chat_message(self, event):
        """
        Envía un mensaje al cliente WebSocket.
        Este método es llamado por group_send para transmitir mensajes.
        
        Datos enviados:
            - type: 'chat_message' (identificador para el cliente)
            - message: Contenido del mensaje
            - username: Nombre del remitente
            - timestamp: Hora de envío (formato HH:MM)
        """
        await self.send(text_data=json.dumps({
            'type': 'chat_message',
            'message': event['message'],
            'username': event['username'],
            'timestamp': event['timestamp'],
        }))
    
    # ============================================================
    # MÉTODOS AUXILIARES (database_sync_to_async)
    # ============================================================
    
    @database_sync_to_async
    def get_chat_info(self):
        """
        Obtiene información del chat desde la base de datos.
        
        Retorna:
            - dict: {
                'is_private': bool,          # Chat privado ONPECO-Acopio
                'is_participant': bool,       # Usuario es participante
                'productor': str,             # Nombre del productor
                'consumidor': str,            # Nombre del consumidor
            }
            - None: Si el chat no existe
        
        Nota:
            - Esta operación se ejecuta de forma síncrona en un hilo separado
            - database_sync_to_async permite operaciones de BD en contexto asíncrono
        """
        from apps.chat.models import ChatRoom
        try:
            chat = ChatRoom.objects.get(id=self.room_id)
            user = self.scope['user']
            
            return {
                'is_private': chat.is_private_onpeco_acopio,
                'is_participant': user == chat.consumidor or user == chat.productor,
                'productor': chat.productor.username,
                'consumidor': chat.consumidor.username,
            }
        except ChatRoom.DoesNotExist:
            return None
    
    @database_sync_to_async
    def is_user_in_chat(self):
        """
        Verifica si el usuario está en el chat (método de compatibilidad).
        
        Retorna:
            - bool: True si el usuario es participante, False en caso contrario
        """
        info = self.get_chat_info()
        return info is not None and info['is_participant']
    
    @database_sync_to_async
    def save_message(self, message):
        """
        Guarda un mensaje en la base de datos.
        
        Parámetros:
            - message: str - Contenido del mensaje
            
        Retorna:
            - dict: {
                'timestamp': str,  # Hora de envío (formato HH:MM)
                'id': int          # ID del mensaje guardado
            }
        
        Nota:
            - La hora se convierte a la zona horaria local
            - Se actualiza la fecha 'updated_at' de la sala de chat
        """
        from django.utils import timezone
        from apps.chat.models import ChatRoom, ChatMessage
        
        chat = ChatRoom.objects.get(id=self.room_id)
        msg = ChatMessage.objects.create(
            room=chat,
            sender=self.scope['user'],
            message=message
        )
        chat.save()  # Actualiza updated_at
        return {
            'timestamp': timezone.localtime(msg.created_at).strftime('%H:%M'),
            'id': msg.id
        }