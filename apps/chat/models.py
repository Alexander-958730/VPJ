"""
APPS.CHAT.MODELS
================
Modelos de datos para el sistema de chat en tiempo real de VPJ.

Este módulo contiene los modelos que gestionan:
- Salas de chat (ChatRoom): Conversaciones entre productores y consumidores
- Mensajes de chat (ChatMessage): Mensajes individuales dentro de una sala
- Chat privado ONPECO ↔ Centro de Acopio

Relaciones:
    - ChatRoom → User (productor, consumidor)
    - ChatRoom → Product (producto relacionado, opcional)
    - ChatMessage → ChatRoom (sala)
    - ChatMessage → User (sender)

Roles de usuario:
- consumidor: Participante en chats (puede enviar y recibir mensajes)
- productor: Participante en chats (puede enviar y recibir mensajes)
- regulador (ONPECO): Supervisa chats (solo lectura) y tiene chat privado con Acopio
- acopio (Centro de Acopio): Supervisa chats y tiene chat privado con ONPECO
"""

from django.db import models
from django.conf import settings


# =============================================================================
# MODELO: ChatRoom
# =============================================================================
# Propósito: Almacena las salas de chat entre un productor y un consumidor.
# Cada sala está asociada a un producto específico (opcional).
#
# Campos principales:
#   - productor: Usuario productor (dueño del producto)
#   - consumidor: Usuario consumidor (comprador potencial)
#   - producto: Producto relacionado con el chat (opcional)
#   - created_at: Fecha de creación
#   - updated_at: Fecha de última actualización
#   - is_private_onpeco_acopio: Indica si es el chat privado ONPECO-Acopio
#
# Restricciones:
#   - Un productor y consumidor no pueden tener más de una sala por producto
#   - unique_together: ['productor', 'consumidor', 'producto']
#
# Casos especiales:
#   - Chat privado ONPECO-Acopio: is_private_onpeco_acopio = True
#   - Se crea automáticamente cuando ONPECO o Acopio acceden a la vista
#   - No se muestra en la lista de supervisión general
# =============================================================================
class ChatRoom(models.Model):
    """
    Modelo de sala de chat entre productor y consumidor
    """
    
    # ============================================================
    # RELACIONES
    # ============================================================
    productor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='chat_rooms_as_productor',
        help_text="Usuario productor (dueño del producto)"
    )
    consumidor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='chat_rooms_as_consumidor',
        help_text="Usuario consumidor (comprador potencial)"
    )
    producto = models.ForeignKey(
        'marketplace.Product',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text="Producto relacionado con el chat (opcional)"
    )
    
    # ============================================================
    # FECHAS
    # ============================================================
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Fecha y hora de creación de la sala"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Fecha y hora de última actualización (nuevo mensaje)"
    )
    
    # ============================================================
    # CHAT PRIVADO ONPECO-ACOPIO
    # ============================================================
    is_private_onpeco_acopio = models.BooleanField(
        default=False,
        help_text="Indica si es el chat privado entre ONPECO y Centro de Acopio"
    )
    
    # ============================================================
    # CONFIGURACIÓN
    # ============================================================
    class Meta:
        unique_together = ['productor', 'consumidor', 'producto']
        verbose_name = 'Sala de chat'
        verbose_name_plural = 'Salas de chat'
    
    # ============================================================
    # MÉTODOS
    # ============================================================
    def __str__(self):
        """Representación legible del objeto"""
        if self.is_private_onpeco_acopio:
            return f"Chat Privado: ONPECO ↔ Centro de Acopio"
        return f"Chat: {self.consumidor.username} - {self.productor.username}"


# =============================================================================
# MODELO: ChatMessage
# =============================================================================
# Propósito: Almacena los mensajes individuales dentro de una sala de chat.
#
# Campos principales:
#   - room: Sala de chat a la que pertenece el mensaje
#   - sender: Usuario que envió el mensaje
#   - message: Contenido del mensaje (texto)
#   - is_read: Indica si el mensaje ha sido leído por el destinatario
#   - created_at: Fecha y hora de envío
#
# Métodos:
#   - __str__(): Representación legible del objeto
#   - get_unread_count_for_user(): Cuenta mensajes no leídos para un usuario
#
# Uso de is_read:
#   - Se marca como leído cuando el destinatario abre la sala de chat
#   - Se usa para mostrar notificaciones de mensajes no leídos
#   - Actualización en la vista `ver_chat` al hacer GET
# =============================================================================
class ChatMessage(models.Model):
    """
    Modelo de mensaje dentro de una sala de chat
    """
    
    # ============================================================
    # RELACIONES
    # ============================================================
    room = models.ForeignKey(
        ChatRoom,
        on_delete=models.CASCADE,
        related_name='messages',
        help_text="Sala de chat a la que pertenece el mensaje"
    )
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='sent_messages',
        help_text="Usuario que envió el mensaje"
    )
    
    # ============================================================
    # DATOS DEL MENSAJE
    # ============================================================
    message = models.TextField(
        help_text="Contenido del mensaje (texto)"
    )
    is_read = models.BooleanField(
        default=False,
        help_text="Indica si el mensaje ha sido leído por el destinatario"
    )
    
    # ============================================================
    # FECHA
    # ============================================================
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Fecha y hora de envío del mensaje"
    )
    
    # ============================================================
    # MÉTODOS
    # ============================================================
    def __str__(self):
        """Representación legible del objeto"""
        return f"{self.sender.username}: {self.message[:30]}"
    
    # ============================================================
    # MÉTODO DE CLASE: get_unread_count_for_user
    # ============================================================
    @classmethod
    def get_unread_count_for_user(cls, user):
        """
        Devuelve el número total de mensajes no leídos para un usuario
        en todas sus conversaciones.
        
        Parámetros:
            - user: Usuario autenticado
            
        Retorna:
            - int: Número de mensajes no leídos
            
        Uso:
            - Context processor para mostrar el badge en el navbar
            - Actualización en tiempo real con WebSockets
            
        Lógica:
            - Suma los mensajes no leídos donde el usuario es productor
            - Suma los mensajes no leídos donde el usuario es consumidor
            - Excluye los mensajes enviados por el propio usuario
        """
        return cls.objects.filter(
            room__productor=user,
            is_read=False
        ).exclude(sender=user).count() + cls.objects.filter(
            room__consumidor=user,
            is_read=False
        ).exclude(sender=user).count()