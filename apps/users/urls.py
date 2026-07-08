from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    # ========== AUTENTICACIÓN ==========
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # ========== REGISTROS ==========
    path('registro/productor/', views.registro_productor, name='registro_productor'),
    path('registro/consumidor/', views.registro_consumidor, name='registro_consumidor'),
    path('registro/suplidor/', views.registro_suplidor, name='registro_suplidor'),
    
    # ========== PERFIL ==========
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/<int:user_id>/', views.perfil_publico_productor, name='perfil_publico_productor'),
    
    # ========== APROBACIÓN DE PRODUCTORES ==========
    path('aprobar-productores/', views.lista_productores_pendientes, name='lista_productores_pendientes'),
    path('aprobar/<int:user_id>/', views.aprobar_productor, name='aprobar_productor'),
    path('rechazar/<int:user_id>/', views.rechazar_productor, name='rechazar_productor'),
    
    # ========== APROBACIÓN DE SUPLIDORES ==========
    path('aprobar-suplidores/', views.lista_suplidores_pendientes, name='lista_suplidores_pendientes'),
    path('aprobar-suplidor/<int:user_id>/', views.aprobar_suplidor, name='aprobar_suplidor'),
    path('rechazar-suplidor/<int:user_id>/', views.rechazar_suplidor, name='rechazar_suplidor'),
    
    # ========== PERFILES PÚBLICOS ==========
    path('productores/', views.lista_productores_publicos, name='lista_productores_publicos'),
    
    # ====================== RECUPERACIÓN DE CONTRASEÑA ======================
    path('password-reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', views.CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', views.CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    # ====================== NUEVAS URLS PARA ONPECO ======================
    # Gestión de usuarios y restablecimiento de contraseñas
    path('onpeco/usuarios/', views.lista_usuarios_onpeco, name='lista_usuarios_onpeco'),
    path('onpeco/resetear-contrasena/<int:user_id>/', views.resetear_contrasena_usuario, name='resetear_contrasena'),
    
    # ====================== CAMBIAR CONTRASEÑA TEMPORAL ======================
    path('cambiar-contrasena-temporal/', views.cambiar_contrasena_temporal, name='cambiar_contrasena_temporal'),
]