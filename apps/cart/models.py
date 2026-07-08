"""
APPS.CART.MODELS
================
Modelos de datos para el sistema de carrito de compras, pedidos y ventas.

Este módulo contiene los modelos que gestionan:
- Carrito de compras (Cart): Almacena productos seleccionados por el usuario
- Items del carrito (CartItem): Productos individuales en el carrito
- Pedidos (Order): Compras realizadas por consumidores
- Items del pedido (OrderItem): Productos individuales en un pedido

Relaciones:
    - Cart → User (uno a uno)
    - CartItem → Cart, Product (muchos a uno)
    - Order → User (comprador), User (vendedor), User (acopio)
    - OrderItem → Order, Product (muchos a uno)

Roles de usuario:
- consumidor: Crea pedidos (compra)
- productor: Recibe pedidos (vende)
- acopio (Centro de Acopio): Gestiona pedidos y pagos
"""

from django.db import models
from django.conf import settings
from apps.marketplace.models import Product


# =============================================================================
# MODELO: Cart
# =============================================================================
# Propósito: Almacena el carrito de compras de un usuario.
# Cada usuario tiene un solo carrito (relación uno a uno).
#
# Campos principales:
#   - user: Usuario dueño del carrito
#   - created_at: Fecha de creación
#   - updated_at: Fecha de última actualización
#
# Métodos:
#   - get_total_items(): Suma de todas las cantidades
#   - get_total_price(): Suma de todos los subtotales
#   - clear_cart(): Elimina todos los items del carrito
#
# Relaciones:
#   - items: Items del carrito (CartItem)
#   - user: Usuario asociado (OneToOne)
# =============================================================================
class Cart(models.Model):
    """Modelo del carrito de compras"""
    
    # ============================================================
    # RELACIONES
    # ============================================================
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='cart',
        help_text="Usuario dueño del carrito"
    )
    
    # ============================================================
    # FECHAS
    # ============================================================
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Fecha de creación del carrito"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Fecha de última actualización del carrito"
    )
    
    # ============================================================
    # MÉTODOS
    # ============================================================
    def __str__(self):
        """Representación legible del objeto"""
        return f"Carrito de {self.user.username}"
    
    def get_total_items(self):
        """
        Devuelve el número total de items en el carrito.
        Suma las cantidades de todos los items.
        """
        return sum(item.quantity for item in self.items.all())
    
    def get_total_price(self):
        """
        Devuelve el precio total del carrito.
        Suma los subtotales de todos los items.
        """
        return sum(item.get_total_price() for item in self.items.all())
    
    def clear_cart(self):
        """Vacía el carrito eliminando todos sus items"""
        self.items.all().delete()
    
    # ============================================================
    # CONFIGURACIÓN
    # ============================================================
    class Meta:
        verbose_name = "Carrito"
        verbose_name_plural = "Carritos"


# =============================================================================
# MODELO: CartItem
# =============================================================================
# Propósito: Almacena un producto específico dentro del carrito de un usuario.
# Cada item tiene una cantidad y un producto asociado.
#
# Campos principales:
#   - cart: Carrito al que pertenece
#   - product: Producto agregado
#   - quantity: Cantidad de unidades
#   - added_at: Fecha de adición
#
# Restricciones:
#   - Un producto no puede estar dos veces en el mismo carrito (unique_together)
#
# Métodos:
#   - get_total_price(): Precio unitario * cantidad
#
# Relaciones:
#   - cart: Carrito asociado (ForeignKey)
#   - product: Producto asociado (ForeignKey)
# =============================================================================
class CartItem(models.Model):
    """Modelo de items dentro del carrito"""
    
    # ============================================================
    # RELACIONES
    # ============================================================
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='items',
        help_text="Carrito al que pertenece este item"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        help_text="Producto agregado al carrito"
    )
    
    # ============================================================
    # DATOS DEL ITEM
    # ============================================================
    quantity = models.PositiveIntegerField(
        default=1,
        help_text="Cantidad de unidades del producto"
    )
    added_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Fecha y hora en que se agregó al carrito"
    )
    
    # ============================================================
    # MÉTODOS
    # ============================================================
    def __str__(self):
        """Representación legible del objeto"""
        return f"{self.quantity} x {self.product.name}"
    
    def get_total_price(self):
        """
        Devuelve el precio total del item.
        Calculo: precio_unitario * cantidad
        """
        return self.product.price * self.quantity
    
    # ============================================================
    # CONFIGURACIÓN
    # ============================================================
    class Meta:
        verbose_name = "Item del carrito"
        verbose_name_plural = "Items del carrito"
        unique_together = ['cart', 'product']  # Un producto no puede estar dos veces


# =============================================================================
# MODELO: Order
# =============================================================================
# Propósito: Almacena los pedidos realizados por consumidores.
# Un pedido agrupa productos de múltiples productores y es gestionado
# por el Centro de Acopio.
#
# Campos principales:
#   - user: Comprador (consumidor)
#   - seller: Vendedor (productor/suplidor que recibe el pedido)
#   - acopio: Centro de Acopio que gestiona el pedido
#   - status: Estado del pedido (pending, confirmed, preparing, delivered, cancelled)
#   - total_amount: Monto total del pedido
#   - delivery_type: Tipo de entrega (delivery, pickup)
#   - payment_status: Estado del pago (pending, partial, paid)
#   - payment_breakdown: Desglose de pagos por productor (JSON)
#
# Estados del pedido:
#   - pending: ⏳ Pendiente de confirmación
#   - confirmed: ✅ Confirmado por productor
#   - preparing: 📦 En preparación
#   - delivered: 🏠 Entregado - Pago realizado
#   - cancelled: ❌ Cancelado
#
# Tipos de entrega:
#   - delivery: 🚚 Entrega a domicilio (requiere dirección)
#   - pickup: 🏪 Paso a recoger (requiere ubicación)
#
# Estructura de payment_breakdown:
#   {
#       "productor_id": {
#           "nombre": "Finca Don Juan",
#           "total": 1500.00,
#           "pagado": 0,
#           "paid": False,
#           "items": [
#               {"producto": "Zanahorias", "cantidad": 10, "subtotal": 500.00}
#           ]
#       }
#   }
#
# Métodos:
#   - get_status_display_icon(): Devuelve el estado con ícono
#   - get_delivery_type_display_icon(): Devuelve el tipo de entrega con ícono
#   - get_payment_status_display_icon(): Devuelve el estado de pago con ícono
#   - actualizar_stock(): Reduce el stock cuando el pedido se entrega
# =============================================================================
class Order(models.Model):
    """Modelo de pedido/compra - Pago contra entrega"""
    
    # ============================================================
    # ESTADOS DEL PEDIDO
    # ============================================================
    ESTADO_CHOICES = [
        ('pending', '⏳ Pendiente de confirmación'),
        ('confirmed', '✅ Confirmado por productor'),
        ('preparing', '📦 En preparación'),
        ('delivered', '🏠 Entregado - Pago realizado'),
        ('cancelled', '❌ Cancelado'),
    ]
    
    # ============================================================
    # TIPOS DE ENTREGA
    # ============================================================
    TIPO_ENTREGA_CHOICES = [
        ('delivery', '🚚 Entrega a domicilio'),
        ('pickup', '🏪 Paso a recoger (Retiro en punto de venta)'),
    ]
    
    # ============================================================
    # ESTADOS DE PAGO
    # ============================================================
    PAGO_CHOICES = [
        ('pending', '⏳ Pendiente de pago'),
        ('partial', '💰 Pago parcial'),
        ('paid', '✅ Pagado'),
    ]
    
    # ============================================================
    # RELACIONES
    # ============================================================
    # Comprador (quien hace el pedido)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='orders',
        help_text="Consumidor que realiza el pedido"
    )
    
    # Vendedor (productor/suplidor que recibe el pedido)
    seller = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='received_orders',
        null=True,
        blank=True,
        help_text="Productor o suplidor que recibe el pedido"
    )
    
    # Centro de acopio que maneja el pedido
    acopio = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='acopio_orders',
        null=True,
        blank=True,
        help_text="Centro de Acopio que gestiona el pedido"
    )
    
    # ============================================================
    # DATOS DEL PEDIDO
    # ============================================================
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Fecha y hora de creación del pedido"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Fecha y hora de última actualización"
    )
    status = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='pending',
        help_text="Estado actual del pedido"
    )
    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        help_text="Monto total del pedido"
    )
    
    # ============================================================
    # PAGOS
    # ============================================================
    payment_status = models.CharField(
        max_length=20,
        choices=PAGO_CHOICES,
        default='pending',
        help_text="Estado del pago a los productores"
    )
    payment_date = models.DateTimeField(
        blank=True,
        null=True,
        help_text="Fecha en que se completó el pago"
    )
    payment_breakdown = models.JSONField(
        default=dict,
        blank=True,
        help_text="Desglose de pagos por productor (JSON)"
    )
    
    # ============================================================
    # ENTREGA
    # ============================================================
    delivery_type = models.CharField(
        max_length=20,
        choices=TIPO_ENTREGA_CHOICES,
        default='delivery',
        help_text="Tipo de entrega seleccionado"
    )
    
    # Entrega a domicilio
    shipping_address = models.TextField(
        blank=True,
        help_text="Dirección donde se entregará el pedido"
    )
    
    # Paso a recoger (Pickup)
    pickup_location = models.CharField(
        max_length=255,
        blank=True,
        help_text="Lugar donde recogerá el pedido"
    )
    
    # Datos de contacto
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        help_text="Número de contacto para la entrega"
    )
    delivery_instructions = models.TextField(
        blank=True,
        help_text="Instrucciones adicionales para la entrega"
    )
    notes = models.TextField(
        blank=True,
        help_text="Notas adicionales del pedido"
    )
    
    # ============================================================
    # MÉTODOS
    # ============================================================
    def __str__(self):
        """Representación legible del objeto"""
        seller_name = self.seller.username if self.seller else "Sin asignar"
        return f"Pedido #{self.id} - {self.user.username} → {seller_name} - RD$ {self.total_amount}"
    
    def get_status_display_icon(self):
        """Devuelve el estado con su ícono correspondiente"""
        icons = {
            'pending': '⏳ Pendiente',
            'confirmed': '✅ Confirmado',
            'preparing': '📦 En preparación',
            'delivered': '🏠 Entregado',
            'cancelled': '❌ Cancelado',
        }
        return icons.get(self.status, self.status)
    
    def get_delivery_type_display_icon(self):
        """Devuelve el tipo de entrega con su ícono correspondiente"""
        icons = {
            'delivery': '🚚 Entrega a domicilio',
            'pickup': '🏪 Paso a recoger',
        }
        return icons.get(self.delivery_type, self.delivery_type)
    
    def get_payment_status_display_icon(self):
        """Devuelve el estado de pago con su ícono correspondiente"""
        icons = {
            'pending': '⏳ Pendiente de pago',
            'partial': '💰 Pago parcial',
            'paid': '✅ Pagado',
        }
        return icons.get(self.payment_status, self.payment_status)
    
    def actualizar_stock(self):
        """
        Actualiza el stock de los productos cuando el pedido se entrega.
        Resta la cantidad vendida del stock disponible.
        Se llama automáticamente cuando el estado cambia a 'delivered'.
        """
        if self.status == 'delivered':
            for item in self.items.all():
                producto = item.product
                producto.stock -= item.quantity
                if producto.stock < 0:
                    producto.stock = 0
                producto.save()
    
    # ============================================================
    # CONFIGURACIÓN
    # ============================================================
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"


# =============================================================================
# MODELO: OrderItem
# =============================================================================
# Propósito: Almacena los productos individuales dentro de un pedido.
# Cada item tiene una cantidad y un precio fijo (el precio al momento de la compra).
#
# Campos principales:
#   - order: Pedido al que pertenece
#   - product: Producto comprado
#   - quantity: Cantidad de unidades
#   - price: Precio unitario al momento de la compra
#
# Métodos:
#   - get_total_price(): Precio * cantidad
#
# Relaciones:
#   - order: Pedido asociado (ForeignKey)
#   - product: Producto asociado (ForeignKey)
# =============================================================================
class OrderItem(models.Model):
    """Modelo de items dentro del pedido"""
    
    # ============================================================
    # RELACIONES
    # ============================================================
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items',
        help_text="Pedido al que pertenece este item"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        help_text="Producto comprado"
    )
    
    # ============================================================
    # DATOS DEL ITEM
    # ============================================================
    quantity = models.PositiveIntegerField(
        default=1,
        help_text="Cantidad de unidades compradas"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Precio unitario al momento de la compra"
    )
    
    # ============================================================
    # MÉTODOS
    # ============================================================
    def __str__(self):
        """Representación legible del objeto"""
        return f"{self.quantity} x {self.product.name}"
    
    def get_total_price(self):
        """
        Devuelve el precio total del item.
        Calculo: precio_unitario * cantidad
        """
        return self.price * self.quantity
    
    # ============================================================
    # CONFIGURACIÓN
    # ============================================================
    class Meta:
        verbose_name = "Item del pedido"
        verbose_name_plural = "Items del pedido"