from django.urls import path
from . import views

app_name = 'complaints'

urlpatterns = [
    # ========== DENUNCIAS ==========
    path('crear/', views.crear_denuncia, name='crear_denuncia'),
    path('crear/producto/<int:producto_id>/', views.crear_denuncia, name='crear_denuncia_producto'),
    path('mis-denuncias/', views.mis_denuncias, name='mis_denuncias'),
    path('detalle/<int:pk>/', views.detalle_denuncia, name='detalle_denuncia'),
    path('lista/', views.lista_denuncias, name='lista_denuncias'),
    path('actualizar/<int:pk>/', views.actualizar_denuncia, name='actualizar_denuncia'),
    
    # ========== BACKUPS ==========
    path('gestion-backups/', views.gestion_backups, name='gestion_backups'),
    path('gestion-backups/crear-punto/', views.crear_punto_restauracion, name='crear_punto_restauracion'),
    path('gestion-backups/restaurar/<str:backup_filename>/', views.restaurar_backup, name='restaurar_backup'),
    
    # ========== REPORTE DE DENUNCIAS ==========
    path('reporte-denuncias/', views.reporte_denuncias, name='reporte_denuncias'),
    path('api/denuncias-por-mes/', views.denuncias_por_mes_api, name='denuncias_por_mes_api'),
    
    # ========== EXPORTAR DENUNCIAS A EXCEL ==========
    path('exportar-excel/', views.exportar_denuncias_excel, name='exportar_denuncias_excel'),
    
    # ========== PORTAL ONPECO ==========
    path('portal/', views.portal_onpeco, name='portal_onpeco'),
    path('api/denuncias/recientes/', views.api_denuncias_recientes, name='api_denuncias_recientes'),
    
    # ========== PRODUCTORES MÁS DENUNCIADOS ==========
    path('productores-mas-denunciados/', views.productores_mas_denunciados, name='productores_mas_denunciados'),
    
    # ========== GESTIÓN DE REPUTACIÓN ==========
    path('gestion-reputacion/', views.gestion_reputacion, name='gestion_reputacion'),
    path('asignar-reputacion/<int:user_id>/', views.asignar_reputacion, name='asignar_reputacion'),
    path('historial-reputacion/<int:user_id>/', views.historial_reputacion, name='historial_reputacion'),
    
    # ========== REPORTES DE VENTAS PARA ONPECO ==========
    path('reportes/ventas/general/', views.reporte_ventas_general, name='reporte_ventas_general'),
    path('reportes/ventas/productor/<int:productor_id>/', views.reporte_ventas_productor, name='reporte_ventas_productor'),
    path('reportes/fincas/excel/', views.reporte_fincas_excel, name='reporte_fincas_excel'),
    path('reportes/ventas/excel/', views.exportar_ventas_excel, name='exportar_ventas_excel'),
    
    # ========== NUEVAS EXPORTACIONES ==========
    path('exportar-consumidores-excel/', views.exportar_consumidores_excel, name='exportar_consumidores_excel'),
    path('exportar-productores-excel/', views.exportar_productores_excel, name='exportar_productores_excel'),
]