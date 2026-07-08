"""
APPS.CHAT.VIEWS
===============
Vistas para el sistema de chat en tiempo real de VPJ.

Este módulo contiene todas las vistas relacionadas con:
- Iniciar chats entre consumidores y productores
- Ver y enviar mensajes en tiempo real (WebSockets)
- Lista de conversaciones del usuario
- Supervisión de chats por ONPECO y Centro de Acopio
- Chat privado ONPECO ↔ Centro de Acopio

Roles de usuario:
- consumidor: Puede iniciar chats con productores
- productor: Puede recibir chats de consumidores
- regulador (ONPECO): Puede supervisar chats (solo lectura)
- acopio (Centro de Acopio): Puede supervisar chats y tiene chat privado con ONPECO
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import models
from .models import ChatRoom, ChatMessage
from apps.marketplace.models import Product
from apps.users.models import User


# =============================================================================
# FUNCIÓN: iniciar_chat
# =============================================================================
# Propósito: Inicia un chat entre un consumidor y un productor.
# Valida que el productor no tenga productos en común con el usuario actual.
#
# Parámetros:
#   - request: Objeto HttpRequest
#   - productor_id: ID del productor con quien iniciar el chat
#   - producto_id: (Opcional) ID del producto relacionado
#
# Retorna:
#   - HttpResponse: Redirige a 'ver_chat' con el room_id creado
#
# URLs asociadas:
#   - /chat/iniciar/<productor_id>/
#   - /chat/iniciar/<productor_id>/<producto_id>/
#
# Roles permitidos:
#   - ✅ Consumidor (puede iniciar chats)
#   - ❌ Productor (no puede iniciar chats con otros productores)
#   - ❌ Suplidor (no puede iniciar chats)
#   - ❌ Regulador
#   - ❌ Centro de Acopio
#
# Flujo de trabajo:
#   1. Verificar que el usuario sea consumidor
#   2. Obtener productor y producto (si aplica)
#   3. Validar que no compartan productos en común
#   4. Crear o obtener sala de chat
#   5. Redirigir a la sala de chat
# =============================================================================
@login_required
def iniciar_chat(request, productor_id, producto_id=None):
    """
    Inicia un chat con un productor desde un producto específico
    VALIDA que el productor no tenga productos en común con el usuario actual
    """
    # Solo consumidores pueden iniciar chats
    if request.user.role != 'consumidor':
        messages.error(request, 'Solo los consumidores pueden iniciar chats.')
        return redirect('marketplace:lista_productos')
    
    productor = get_object_or_404(User, id=productor_id, role='productor')
    producto = None
    if producto_id:
        producto = get_object_or_404(Product, id=producto_id)
    
    # ============================================================
    # VALIDACIÓN: PRODUCTOR NO PUEDE CHATEAR CON OTRO CON PRODUCTOS EN COMÚN
    # ============================================================
    if request.user.role in ['productor', 'suplidor']:
        if request.user.tiene_productos_comunes_con(productor):
            mis_productos = request.user.productos_que_vende
            sus_productos = productor.productos_que_vende
            comunes = list(set(mis_productos).intersection(sus_productos))
            
            messages.error(
                request, 
                f'❌ No puedes chatear con {productor.business_name or productor.username} porque '
                f'ambos venden: {", ".join(comunes)}. '
                f'Puedes chatear con productores que vendan productos diferentes a los tuyos.'
            )
            return redirect('marketplace:detalle_producto', producto_id=producto.id if producto else 1)
    # ============================================================
    # FIN VALIDACIÓN
    # ============================================================
    
    # Crear o obtener la sala de chat
    chat_room, created = ChatRoom.objects.get_or_create(
        productor=productor,
        consumidor=request.user,
        producto=producto
    )
    
    return redirect('chat:ver_chat', room_id=chat_room.id)


# =============================================================================
# FUNCIÓN: ver_chat
# =============================================================================
# Propósito: Muestra la interfaz de chat y maneja el envío de mensajes.
# Soporta diferentes modos: normal, supervisión y privado.
#
# Parámetros:
#   - request: Objeto HttpRequest (GET, POST)
#   - room_id: ID de la sala de chat
#
# Retorna:
#   - GET: Renderiza 'chat/ver_chat.html' con los mensajes
#   - POST: Guarda el mensaje y redirige a la misma vista
#
# URLs asociadas:
#   - /chat/ver/<room_id>/
#
# Roles permitidos:
#   - ✅ Participantes (consumidor, productor)
#   - ✅ Supervisores (ONPECO, Centro de Acopio) - solo lectura
#   - ❌ Otros usuarios
#
# Modos:
#   - Normal: Participantes pueden enviar y recibir mensajes
#   - Supervisión: ONPECO/Acopio pueden ver pero no enviar
#   - Privado: Chat exclusivo ONPECO ↔ Acopio
# =============================================================================
@login_required
def ver_chat(request, room_id):
    chat_room = get_object_or_404(ChatRoom, id=room_id)
    
    # ============================================================
    # PERMITIR A SUPERVISORES VER CHATS (SOLO LECTURA)
    # ============================================================
    is_supervisor = request.user.role == 'regulador' or request.user.is_superuser or request.user.username == 'centro_acopio'
    is_participant = request.user == chat_room.consumidor or request.user == chat_room.productor
    
    # Si es supervisor y NO es el chat privado ONPECO-Acopio
    if is_supervisor and not chat_room.is_private_onpeco_acopio:
        # Supervisión: puede ver pero NO enviar mensajes
        mensajes = chat_room.messages.all().order_by('created_at')
        context = {
            'chat_room': chat_room,
            'mensajes': mensajes,
            'otro_usuario': None,
            'is_supervision': True,
            'is_private': False,
        }
        return render(request, 'chat/ver_chat.html', context)
    
    # Si es supervisor y ES el chat privado ONPECO-Acopio
    if is_supervisor and chat_room.is_private_onpeco_acopio:
        # Verificar que sea participante (ONPECO o Acopio)
        if not is_participant:
            messages.error(request, 'No tienes permiso para ver este chat.')
            return redirect('inicio')
        # Continuar con el chat normal (puede enviar mensajes)
    # ============================================================
    # FIN SUPERVISORES
    # ============================================================
    
    # Verificar permisos para usuarios normales
    if not is_participant:
        messages.error(request, 'No tienes permiso para ver este chat.')
        return redirect('marketplace:lista_productos')
    
    # ============================================================
    # PROCESAR ENVÍO DE MENSAJE (POST)
    # ============================================================
    if request.method == 'POST':
        mensaje = request.POST.get('mensaje')
        if mensaje:
            ChatMessage.objects.create(
                room=chat_room,
                sender=request.user,
                message=mensaje
            )
            chat_room.save()
    
    # ============================================================
    # MARCAR MENSAJES COMO LEÍDOS (GET)
    # ============================================================
    if request.method == 'GET':
        ChatMessage.objects.filter(room=chat_room, is_read=False).exclude(sender=request.user).update(is_read=True)
    
    mensajes = chat_room.messages.all().order_by('created_at')
    
    context = {
        'chat_room': chat_room,
        'mensajes': mensajes,
        'otro_usuario': chat_room.consumidor if request.user == chat_room.productor else chat_room.productor,
        'is_supervision': False,
        'is_private': chat_room.is_private_onpeco_acopio,
    }
    return render(request, 'chat/ver_chat.html', context)


# =============================================================================
# FUNCIÓN: mis_chats
# =============================================================================
# Propósito: Lista todas las conversaciones del usuario actual.
# Para productores, filtra los chats con productores que tengan productos en común.
#
# Parámetros:
#   - request: Objeto HttpRequest
#
# Retorna:
#   - HttpResponse: Renderiza 'chat/lista_conversaciones.html' con las conversaciones
#
# URLs asociadas:
#   - /chat/mis-chats/
#
# Roles permitidos:
#   - ✅ Consumidor
#   - ✅ Productor
#   - ✅ Suplidor
#   - ✅ Regulador
#   - ✅ Centro de Acopio
#
# Datos preparados por conversación:
#   - id: ID de la sala
#   - other_user: El otro participante
#   - ultimo_mensaje: Último mensaje enviado
#   - mensajes_no_leidos: Contador de mensajes no leídos
# =============================================================================
@login_required
def mis_chats(request):
    """
    Lista de chats del usuario (VERSIÓN MEJORADA PARA TEMPLATE MODERNO)
    Para productores: FILTRA los chats con productores que tengan productos en común
    """
    # ============================================================
    # 1. OBTENER CHATS DEL USUARIO
    # ============================================================
    if request.user.role == 'productor':
        chats = ChatRoom.objects.filter(productor=request.user).order_by('-updated_at')
    elif request.user.role == 'consumidor':
        chats = ChatRoom.objects.filter(consumidor=request.user).order_by('-updated_at')
    else:
        # Para ONPECO y CentroAcopio, mostrar sus chats
        chats = ChatRoom.objects.filter(
            models.Q(productor=request.user) | models.Q(consumidor=request.user)
        ).order_by('-updated_at')
    
    # ============================================================
    # 2. FILTRAR CHATS PARA PRODUCTORES
    # ============================================================
    if request.user.role in ['productor', 'suplidor']:
        chats_filtrados = []
        for chat in chats:
            otro_usuario = chat.productor if chat.consumidor == request.user else chat.consumidor
            if otro_usuario.role in ['productor', 'suplidor']:
                # Verificar compatibilidad: solo si NO comparten productos en común
                if not request.user.tiene_productos_comunes_con(otro_usuario):
                    chats_filtrados.append(chat)
            else:
                # Si el otro usuario es consumidor, siempre se muestra
                chats_filtrados.append(chat)
        chats = chats_filtrados
    # ============================================================
    # FIN FILTRO
    # ============================================================
    
    # ============================================================
    # 3. PREPARAR DATOS PARA EL TEMPLATE
    # ============================================================
    conversaciones = []
    for chat in chats:
        # Determinar el otro usuario
        otro_usuario = chat.productor if chat.consumidor == request.user else chat.consumidor
        
        # Contar mensajes no leídos
        no_leidos = ChatMessage.objects.filter(
            room=chat, 
            is_read=False
        ).exclude(sender=request.user).count()
        
        # Obtener el último mensaje
        ultimo_mensaje = ChatMessage.objects.filter(room=chat).order_by('-created_at').first()
        
        conversaciones.append({
            'id': chat.id,
            'other_user': otro_usuario,
            'ultimo_mensaje': ultimo_mensaje,
            'mensajes_no_leidos': no_leidos,
        })
    
    context = {
        'conversaciones': conversaciones,
        'total_chats': len(conversaciones),
    }
    return render(request, 'chat/lista_conversaciones.html', context)


# =============================================================================
# FUNCIÓN: supervisar_chats
# =============================================================================
# Propósito: Muestra a ONPECO y Centro de Acopio todos los chats del sistema
# en modo supervisión (solo lectura).
#
# Parámetros:
#   - request: Objeto HttpRequest
#
# Retorna:
#   - HttpResponse: Renderiza 'chat/supervisar_chats.html' con todos los chats
#
# URLs asociadas:
#   - /chat/supervisar/
#
# Roles permitidos:
#   - ✅ Regulador (ONPECO)
#   - ✅ Centro de Acopio (acopio)
#   - ❌ Consumidor
#   - ❌ Productor
#
# Características:
#   - Excluye el chat privado ONPECO-Acopio (tiene su propia vista)
#   - Muestra participantes y cantidad de mensajes
# =============================================================================
@login_required
def supervisar_chats(request):
    """Vista para que ONPECO y CentroAcopio vean todos los chats (solo lectura)"""
    
    # Verificar permisos
    is_onpeco = request.user.role == 'regulador' or request.user.is_superuser
    is_acopio = request.user.username == 'centro_acopio'
    
    if not (is_onpeco or is_acopio):
        messages.error(request, 'No tienes permiso para acceder a esta sección.')
        return redirect('inicio')
    
    # Excluir el chat privado ONPECO-Acopio (ese tiene su propia vista)
    chats = ChatRoom.objects.filter(
        is_private_onpeco_acopio=False
    ).order_by('-updated_at')
    
    for chat in chats:
        chat.last_message = ChatMessage.objects.filter(room=chat).order_by('-created_at').first()
        chat.participant_names = f"{chat.productor.get_full_name() or chat.productor.username} ↔ {chat.consumidor.get_full_name() or chat.consumidor.username}"
        chat.message_count = ChatMessage.objects.filter(room=chat).count()
    
    context = {
        'chats': chats,
        'is_supervisor': True,
        'total_chats': chats.count(),
    }
    return render(request, 'chat/supervisar_chats.html', context)


# =============================================================================
# FUNCIÓN: chat_privado_onpeco_acopio
# =============================================================================
# Propósito: Canal de comunicación privado y exclusivo entre ONPECO
# y el Centro de Acopio para coordinación de temas regulatorios.
#
# Parámetros:
#   - request: Objeto HttpRequest
#
# Retorna:
#   - HttpResponse: Renderiza 'chat/ver_chat.html' con el chat privado
#
# URLs asociadas:
#   - /chat/privado-acopio/
#
# Roles permitidos:
#   - ✅ Regulador (ONPECO)
#   - ✅ Centro de Acopio (acopio)
#   - ❌ Consumidor
#   - ❌ Productor
#
# Características:
#   - Solo ONPECO y Acopio pueden ver y enviar mensajes
#   - El chat se crea automáticamente la primera vez
#   - No aparece en la lista de supervisión general
# =============================================================================
@login_required
def chat_privado_onpeco_acopio(request):
    """Chat privado entre ONPECO y Centro de Acopio (solo ellos dos)"""
    
    # ============================================================
    # 1. VERIFICAR PERMISOS
    # ============================================================
    is_onpeco = request.user.role == 'regulador' or request.user.is_superuser
    is_acopio = request.user.username == 'centro_acopio'
    
    if not (is_onpeco or is_acopio):
        messages.error(request, 'No tienes permiso para acceder a esta sección.')
        return redirect('inicio')
    
    # ============================================================
    # 2. OBTENER EL OTRO PARTICIPANTE
    # ============================================================
    if is_acopio:
        # El otro es ONPECO (buscar un regulador)
        otro = User.objects.filter(role='regulador').first()
        if not otro:
            otro = User.objects.filter(is_superuser=True).first()
    else:
        # El otro es Centro de Acopio
        try:
            otro = User.objects.get(username='centro_acopio')
        except User.DoesNotExist:
            messages.error(request, '❌ Centro de Acopio no encontrado.')
            return redirect('inicio')
    
    if not otro:
        messages.error(request, '❌ No se encontró el otro participante.')
        return redirect('inicio')
    
    # ============================================================
    # 3. CREAR O OBTENER LA SALA PRIVADA
    # ============================================================
    productor = min(request.user, otro, key=lambda x: x.id)
    consumidor = max(request.user, otro, key=lambda x: x.id)
    
    room, created = ChatRoom.objects.get_or_create(
        productor=productor,
        consumidor=consumidor,
        is_private_onpeco_acopio=True,
        defaults={'producto': None}
    )
    
    # ============================================================
    # 4. OBTENER MENSAJES
    # ============================================================
    mensajes = ChatMessage.objects.filter(room=room).order_by('created_at')
    
    context = {
        'chat_room': room,
        'mensajes': mensajes,
        'otro_usuario': otro,
        'is_private': True,
        'is_supervision': False,
    }
    return render(request, 'chat/ver_chat.html', context)


# =============================================================================
# FUNCIÓN: ver_chat_supervision
# =============================================================================
# Propósito: Permite a ONPECO o Centro de Acopio ver un chat específico
# en modo supervisión (solo lectura).
#
# Parámetros:
#   - request: Objeto HttpRequest
#   - room_id: ID de la sala de chat a supervisar
#
# Retorna:
#   - HttpResponse: Renderiza 'chat/ver_chat_supervision.html'
#
# URLs asociadas:
#   - /chat/supervisar/<room_id>/
#
# Roles permitidos:
#   - ✅ Regulador (ONPECO)
#   - ✅ Centro de Acopio (acopio)
#   - ❌ Consumidor
#   - ❌ Productor
#
# Características:
#   - Modo solo lectura (no se puede enviar mensajes)
#   - Excluye el chat privado ONPECO-Acopio
# =============================================================================
@login_required
def ver_chat_supervision(request, room_id):
    """Vista para ver un chat específico en modo supervisión (solo lectura)"""
    
    # Verificar permisos
    is_onpeco = request.user.role == 'regulador' or request.user.is_superuser
    is_acopio = request.user.username == 'centro_acopio'
    
    if not (is_onpeco or is_acopio):
        messages.error(request, 'No tienes permiso para acceder a esta sección.')
        return redirect('inicio')
    
    chat_room = get_object_or_404(ChatRoom, id=room_id, is_private_onpeco_acopio=False)
    mensajes = chat_room.messages.all().order_by('created_at')
    
    context = {
        'chat_room': chat_room,
        'mensajes': mensajes,
        'otro_usuario': None,
        'is_supervision': True,
        'is_private': False,
    }
    return render(request, 'chat/ver_chat_supervision.html', context)