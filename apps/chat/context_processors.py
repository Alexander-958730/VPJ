from .models import ChatMessage

def chat_notifications(request):
    """Context processor para notificaciones de chat no leídas"""
    if request.user.is_authenticated:
        unread_count = ChatMessage.get_unread_count_for_user(request.user)
        return {
            'chat_unread_count': unread_count,
        }
    return {
        'chat_unread_count': 0,
    }