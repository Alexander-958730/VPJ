from django.urls import path
from . import views

app_name = 'marketplace'

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('mis-productos/', views.mis_productos, name='mis_productos'),
    path('crear/', views.crear_producto, name='crear_producto'),
    path('editar/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('top-vistos/', views.productos_mas_vistos, name='productos_mas_vistos'),
    # Búsqueda en tiempo real
    path('busqueda-tiempo-real/', views.busqueda_tiempo_real_view, name='busqueda_tiempo_real'),
    path('api/buscar-productos/', views.buscar_productos_tiempo_real, name='buscar_productos_tiempo_real'),
    path('api/buscar-suplidores/', views.buscar_suplidores_tiempo_real, name='buscar_suplidores_tiempo_real'),
    path('gestion-categorias/', views.gestion_categorias, name='gestion_categorias'),
]