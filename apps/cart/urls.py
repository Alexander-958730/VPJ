from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('ver/', views.ver_carrito, name='ver_carrito'),
    path('agregar/<int:product_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('actualizar/<int:item_id>/', views.actualizar_cantidad, name='actualizar_cantidad'),
    path('eliminar/<int:item_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('vaciar/', views.vaciar_carrito, name='vaciar_carrito'),
    path('checkout/', views.checkout, name='checkout'),
    path('confirmacion/<int:order_id>/', views.order_confirmation, name='order_confirmation'),
    path('mis-pedidos/', views.mis_pedidos, name='mis_pedidos'),
    path('pedido/<int:order_id>/', views.detalle_pedido, name='detalle_pedido'),
    path('mis-ventas/', views.mis_ventas, name='mis_ventas'),
    path('detalle-venta/<int:order_id>/', views.detalle_venta, name='detalle_venta'),
    path('actualizar-estado/<int:order_id>/', views.actualizar_estado_pedido, name='actualizar_estado_pedido'),
    path('pedidos-acopio/', views.pedidos_acopio, name='pedidos_acopio'),
    path('detalle-acopio/<int:order_id>/', views.detalle_acopio, name='detalle_acopio'),
    path('balance-ventas/', views.balance_ventas, name='balance_ventas'),
    path('registrar-pago/<int:order_id>/<int:productor_id>/', views.registrar_pago_productor, name='registrar_pago_productor'),
]
