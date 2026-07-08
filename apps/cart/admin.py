"""
APPS.CART.ADMIN
===============
Configuración del panel de administración de Django para la app cart.

Este módulo contiene las configuraciones de admin para:
- Cart (Carrito de compras): Visualización y gestión de carritos
- CartItem (Items del carrito): Productos dentro de cada carrito

Características:
- Listado de carritos con total de items y precio total
- Inline para ver items dentro del carrito
- Búsqueda por usuario y email
- Filtros por fecha de actualización
"""

from django.contrib import admin
from .models import Cart, CartItem


# =============================================================================
# INLINE: CartItemInline
# =============================================================================
# Propósito: Permite ver y gestionar los items de un carrito directamente
# desde la página de detalle del carrito en el admin.
#
# Configuración:
#   - model: CartItem
#   - extra: 0 (no muestra filas vacías adicionales)
#   - readonly_fields: ('added_at',) (la fecha de adición no es editable)
#
# Uso:
#   - Se muestra como tabla dentro de la página de edición de Cart
# =============================================================================
class CartItemInline(admin.TabularInline):
    """Inline para mostrar los items de un carrito"""
    model = CartItem
    extra = 0
    readonly_fields = ('added_at',)


# =============================================================================
# ADMIN: CartAdmin
# =============================================================================
# Propósito: Configuración del panel de administración para el modelo Cart.
#
# Configuración:
#   - list_display: Columnas mostradas en la lista de carritos
#   - list_filter: Filtros laterales (por fecha de actualización)
#   - search_fields: Campos de búsqueda (usuario, email)
#   - inlines: Inline para CartItem
#   - readonly_fields: Campos de solo lectura (fechas)
#
# Métodos personalizados:
#   - get_total_items(): Retorna la cantidad total de items en el carrito
#   - get_total_price(): Retorna el precio total formateado en RD$
#
# Uso en admin:
#   - Ver carritos de usuarios
#   - Inspeccionar items en cada carrito
#   - Filtrar por actividad reciente
# =============================================================================
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    """Configuración del admin para carritos de compras"""
    
    # ============================================================
    # CONFIGURACIÓN DE LISTADO
    # ============================================================
    list_display = (
        'id',
        'user',
        'get_total_items',
        'get_total_price',
        'updated_at'
    )
    list_filter = ('updated_at',)
    search_fields = ('user__username', 'user__email')
    inlines = [CartItemInline]
    readonly_fields = ('created_at', 'updated_at')
    
    # ============================================================
    # MÉTODOS PERSONALIZADOS
    # ============================================================
    
    def get_total_items(self, obj):
        """
        Retorna la cantidad total de items en el carrito.
        
        Parámetros:
            - obj: Instancia de Cart
            
        Retorna:
            - int: Total de items en el carrito
        """
        return obj.get_total_items()
    get_total_items.short_description = 'Total Items'
    
    def get_total_price(self, obj):
        """
        Retorna el precio total del carrito formateado en RD$.
        
        Parámetros:
            - obj: Instancia de Cart
            
        Retorna:
            - str: Precio total con formato RD$ XXX.XX
        """
        return f"RD$ {obj.get_total_price():.2f}"
    get_total_price.short_description = 'Total'


# =============================================================================
# ADMIN: CartItemAdmin
# =============================================================================
# Propósito: Configuración del panel de administración para el modelo CartItem.
#
# Configuración:
#   - list_display: Columnas mostradas en la lista de items
#   - list_filter: Filtros por fecha de adición
#   - search_fields: Búsqueda por nombre de producto o usuario
#
# Métodos personalizados:
#   - get_total_price(): Retorna el subtotal del item formateado en RD$
#
# Uso en admin:
#   - Ver items individuales en el carrito
#   - Buscar productos específicos
#   - Monitorear qué productos se agregan al carrito
# =============================================================================
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    """Configuración del admin para items del carrito"""
    
    # ============================================================
    # CONFIGURACIÓN DE LISTADO
    # ============================================================
    list_display = (
        'id',
        'cart',
        'product',
        'quantity',
        'get_total_price',
        'added_at'
    )
    list_filter = ('added_at',)
    search_fields = ('product__name', 'cart__user__username')
    
    # ============================================================
    # MÉTODOS PERSONALIZADOS
    # ============================================================
    
    def get_total_price(self, obj):
        """
        Retorna el subtotal del item formateado en RD$.
        
        Parámetros:
            - obj: Instancia de CartItem
            
        Retorna:
            - str: Subtotal con formato RD$ XXX.XX
        """
        return f"RD$ {obj.get_total_price():.2f}"
    get_total_price.short_description = 'Subtotal'