from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    # ========== URLs EXISTENTES ==========
    path('iniciar/<int:productor_id>/', views.iniciar_chat, name='iniciar_chat'),
    path('iniciar/<int:productor_id>/producto/<int:producto_id>/', views.iniciar_chat, name='iniciar_chat_producto'),
    path('ver/<int:room_id>/', views.ver_chat, name='ver_chat'),
    path('mis-chats/', views.mis_chats, name='mis_chats'),
    
    # ========== NUEVAS URLs ==========
    path('supervisar/', views.supervisar_chats, name='supervisar_chats'),
    path('privado-onpeco-acopio/', views.chat_privado_onpeco_acopio, name='chat_privado_onpeco_acopio'),
    path('ver-supervision/<int:room_id>/', views.ver_chat_supervision, name='ver_chat_supervision'),
    path('conversacion/<int:room_id>/', views.ver_chat, name='detalle_conversacion'),
]