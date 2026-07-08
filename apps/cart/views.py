"""
APPS.CART.VIEWS
===============
Vistas para el sistema de carrito de compras, pedidos, ventas y centro de acopio.

Este módulo contiene todas las vistas relacionadas con:
- Carrito de compras (agregar, eliminar, actualizar)
- Checkout y creación de pedidos
- Gestión de pedidos para consumidores
- Gestión de ventas para productores
- Balance de ventas para productores
- Centro de acopio (gestión de pedidos y pagos)

Roles de usuario:
- consumidor: Puede comprar, ver pedidos
- productor: Puede vender, ver ventas, balance
- suplidor: Puede vender, ver ventas, balance (desactivado)
- regulador (ONPECO): Supervisión general
- acopio (Centro de Acopio): Gestión de pedidos y pagos
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from apps.marketplace.models import Product
from .models import Cart, CartItem


# =============================================================================
# FUNCIÓN AUXILIAR: get_or_create_cart
# =============================================================================
# Propósito: Obtiene el carrito del usuario o lo crea si no existe.
# 
# Parámetros:
#   - user: Usuario autenticado
#
# Retorna:
#   - Cart: Objeto del carrito del usuario
#
# Uso:
#   - Llamada interna desde todas las vistas del carrito
#   - Garantiza que el usuario siempre tenga un carrito asociado
# =============================================================================
def get_or_create_cart(user):
    """Obtiene o crea el carrito para un usuario"""
    cart, created = Cart.objects.get_or_create(user=user)
    return cart


# =============================================================================
# VISTA: ver_carrito
# =============================================================================
# Propósito: Muestra el contenido del carrito de compras del usuario.
#
# Parámetros:
#   - request: Objeto HttpRequest
#
# Retorna:
#   - HttpResponse: Renderiza 'cart/ver_carrito.html' con los items del carrito
#
# URLs asociadas:
#   - /cart/ver/
#
# Roles permitidos:
#   - ✅ Consumidor
#   - ✅ Productor (puede comprar productos de otras subcategorías)
#   - ❌ Regulador (no tiene carrito)
#   - ❌ Centro de Acopio (no tiene carrito)
# =============================================================================
@login_required
def ver_carrito(request):
    """Vista para ver el carrito de compras"""
    cart = get_or_create_cart(request.user)
    context = {
        'cart': cart,
        'items': cart.items.all().select_related('product'),
        'total_items': cart.get_total_items(),
        'total_price': cart.get_total_price(),
    }
    return render(request, 'cart/ver_carrito.html', context)


# =============================================================================
# VISTA: agregar_al_carrito
# =============================================================================
# Propósito: Agrega un producto al carrito con validaciones de:
#   1. Stock disponible
#   2. Productos en común (productores no pueden comprar productos de su misma subcategoría)
#   3. Cantidad válida
#
# Parámetros:
#   - request: Objeto HttpRequest (POST)
#   - product_id: ID del producto a agregar
#
# Retorna:
#   - HttpResponse: Redirige a la URL 'next' o a 'lista_productos'
#
# URLs asociadas:
#   - /cart/agregar/<product_id>/
#
# Roles permitidos:
#   - ✅ Consumidor
#   - ✅ Productor (con restricciones de subcategoría)
#   - ❌ Regulador (bloqueado)
#   - ❌ Centro de Acopio (bloqueado)
#
# Validaciones:
#   1. Producto disponible (available=True)
#   2. Productor no puede comprar productos de su misma subcategoría
#   3. Cantidad > 0
#   4. Cantidad solicitada <= stock disponible
#   5. Cantidad total (actual + nueva) <= stock disponible
# =============================================================================
@login_required
def agregar_al_carrito(request, product_id):
    """Agrega un producto al carrito con validación de stock y productos en común"""
    product = get_object_or_404(Product, id=product_id, available=True)
    
    # ============================================================
    # 1. VALIDACIÓN POR SUBCATEGORÍA (PRODUCTORES)
    # ============================================================
    if request.user.role in ['productor', 'suplidor']:
        # Obtener subcategorías de productos que vende el usuario
        mis_subcategorias = []
        for p in request.user.products.all():
            if p.subcategory:
                mis_subcategorias.append(p.subcategory)
        
        # Subcategoría del producto a comprar
        subcategoria_a_comprar = product.subcategory if product.subcategory else ''
        
        # Debug en consola
        print("=" * 50)
        print("🔍 DEBUG - VALIDACIÓN POR SUBCATEGORÍA")
        print(f"   Usuario: {request.user.username} ({request.user.role})")
        print(f"   Subcategorías que vende: {mis_subcategorias}")
        print(f"   Subcategoría a comprar: {subcategoria_a_comprar}")
        print(f"   ¿Coincide? {subcategoria_a_comprar in mis_subcategorias}")
        print("=" * 50)
        
        if subcategoria_a_comprar in mis_subcategorias:
            print("🚨 VALIDACIÓN ACTIVADA - BLOQUEANDO COMPRA")
            messages.error(
                request, 
                f'❌ No puedes comprar "{product.name}" porque tú también vendes productos en la subcategoría "{product.get_subcategory_display()}". '
                f'Puedes comprar productos de otras subcategorías.'
            )
            next_url = request.POST.get('next') or request.GET.get('next') or 'marketplace:lista_productos'
            return redirect(next_url)
    # ============================================================
    # FIN VALIDACIÓN POR SUBCATEGORÍA
    # ============================================================
    
    # ============================================================
    # 2. OBTENER CARRITO
    # ============================================================
    cart = get_or_create_cart(request.user)
    
    # ============================================================
    # 3. OBTENER Y VALIDAR CANTIDAD
    # ============================================================
    cantidad = 1
    try:
        cantidad = int(request.POST.get('cantidad', 1))
    except (ValueError, TypeError):
        cantidad = 1
    
    if cantidad <= 0:
        messages.error(request, '❌ La cantidad debe ser mayor a 0.')
        return redirect('marketplace:detalle_producto', product_id=product.id)
    
    # ============================================================
    # 4. OBTENER CANTIDAD ACTUAL EN EL CARRITO
    # ============================================================
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={'quantity': 0}
    )
    cantidad_actual = cart_item.quantity if not created else 0
    
    # ============================================================
    # 5. VALIDAR STOCK
    # ============================================================
    # Validación 1: La cantidad solicitada no puede superar el stock total
    if cantidad > product.stock:
        messages.error(
            request, 
            f'❌ No hay suficiente stock de "{product.name}". '
            f'Disponible: {product.stock}, Solicitado: {cantidad}'
        )
        return redirect('marketplace:detalle_producto', product_id=product.id)
    
    # Validación 2: La cantidad total (actual + nueva) no puede superar el stock
    nueva_cantidad_total = cantidad_actual + cantidad
    if nueva_cantidad_total > product.stock:
        messages.error(
            request, 
            f'❌ No puedes agregar "{product.name}". '
            f'Disponible: {product.stock}, Ya tienes en carrito: {cantidad_actual}'
        )
        return redirect('marketplace:detalle_producto', product_id=product.id)
    
    # ============================================================
    # 6. AGREGAR O ACTUALIZAR EL CARRITO
    # ============================================================
    if created:
        cart_item.quantity = cantidad
        cart_item.save()
        messages.success(request, f'✅ {cantidad}x {product.name} agregado al carrito')
    else:
        cart_item.quantity = nueva_cantidad_total
        cart_item.save()
        messages.success(
            request, 
            f'✅ {cantidad}x {product.name} agregado al carrito. '
            f'Total en carrito: {nueva_cantidad_total}x'
        )
    
    next_url = request.POST.get('next') or request.GET.get('next') or 'marketplace:lista_productos'
    return redirect(next_url)


# =============================================================================
# VISTA: actualizar_cantidad
# =============================================================================
# Propósito: Actualiza la cantidad de un item en el carrito.
# Si la cantidad es 0 o negativa, elimina el item del carrito.
#
# Parámetros:
#   - request: Objeto HttpRequest (POST)
#   - item_id: ID del item del carrito a actualizar
#
# Retorna:
#   - HttpResponse: Redirige a 'ver_carrito'
#
# URLs asociadas:
#   - /cart/actualizar/<item_id>/
# =============================================================================
@login_required
def actualizar_cantidad(request, item_id):
    """Actualiza la cantidad de un item en el carrito"""
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    
    if request.method == 'POST':
        cantidad = int(request.POST.get('cantidad', 1))
        
        if cantidad <= 0:
            cart_item.delete()
            messages.info(request, f'✅ {cart_item.product.name} eliminado del carrito')
        else:
            cart_item.quantity = cantidad
            cart_item.save()
            messages.success(request, f'✅ Cantidad actualizada: {cart_item.product.name} x{cantidad}')
    
    return redirect('cart:ver_carrito')


# =============================================================================
# VISTA: eliminar_del_carrito
# =============================================================================
# Propósito: Elimina un producto específico del carrito.
#
# Parámetros:
#   - request: Objeto HttpRequest
#   - item_id: ID del item del carrito a eliminar
#
# Retorna:
#   - HttpResponse: Redirige a 'ver_carrito'
#
# URLs asociadas:
#   - /cart/eliminar/<item_id>/
# =============================================================================
@login_required
def eliminar_del_carrito(request, item_id):
    """Elimina un producto del carrito"""
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    product_name = cart_item.product.name
    cart_item.delete()
    messages.info(request, f'🗑️ {product_name} eliminado del carrito')
    return redirect('cart:ver_carrito')


# =============================================================================
# VISTA: vaciar_carrito
# =============================================================================
# Propósito: Vacía completamente el carrito del usuario.
#
# Parámetros:
#   - request: Objeto HttpRequest
#
# Retorna:
#   - HttpResponse: Redirige a 'ver_carrito'
#
# URLs asociadas:
#   - /cart/vaciar/
# =============================================================================
@login_required
def vaciar_carrito(request):
    """Vacía completamente el carrito"""
    cart = get_or_create_cart(request.user)
    cart.clear_cart()
    messages.info(request, '🗑️ Carrito vaciado completamente')
    return redirect('cart:ver_carrito')


# =============================================================================
# CHECKOUT Y PEDIDOS
# =============================================================================

# =============================================================================
# VISTA: checkout
# =============================================================================
# Propósito: Paso 1 del proceso de compra. Permite al consumidor confirmar
# su pedido, seleccionar tipo de entrega y generar el pedido formal.
#
# Parámetros:
#   - request: Objeto HttpRequest (GET, POST)
#
# Retorna:
#   - GET: Renderiza 'cart/checkout.html' con el resumen del pedido
#   - POST: Crea el pedido y redirige a 'order_confirmation'
#
# URLs asociadas:
#   - /cart/checkout/
#
# Roles permitidos:
#   - ✅ Consumidor
#   - ❌ Productor (no puede comprar en checkout)
#   - ❌ Regulador
#   - ❌ Centro de Acopio
#
# Flujo de trabajo:
#   1. Verificar que el carrito no esté vacío
#   2. Validar stock de todos los productos
#   3. Agrupar productos por vendedor
#   4. Procesar POST: crear pedido, items, reducir stock
#   5. Vaciar carrito
#   6. Mostrar confirmación
# =============================================================================
@login_required
def checkout(request):
    """Paso 1: Confirmar pedido con pago contra entrega - Centro de Acopio"""
    from apps.users.models import User
    from .models import Order, OrderItem
    
    cart = get_or_create_cart(request.user)
    items = cart.items.all().select_related('product')
    
    # ============================================================
    # 1. VERIFICAR QUE EL CARRITO NO ESTÉ VACÍO
    # ============================================================
    if not items:
        messages.warning(request, '🛒 Tu carrito está vacío. Agrega productos antes de continuar.')
        return redirect('cart:ver_carrito')
    
    # ============================================================
    # 2. VALIDACIÓN DE STOCK
    # ============================================================
    for item in items:
        if item.product.stock < item.quantity:
            messages.error(
                request, 
                f'❌ No hay suficiente stock de "{item.product.name}". '
                f'Disponible: {item.product.stock}, Solicitado: {item.quantity}'
            )
            return redirect('cart:ver_carrito')
        
        if item.product.stock <= 0:
            messages.error(
                request, 
                f'❌ "{item.product.name}" no está disponible. Stock: 0'
            )
            return redirect('cart:ver_carrito')
    
    # ============================================================
    # 3. AGRUPAR PRODUCTOS POR VENDEDOR
    # ============================================================
    productores = {}
    for item in items:
        vendedor = item.product.vendedor
        if vendedor.id not in productores:
            productores[vendedor.id] = {
                'id': vendedor.id,
                'nombre': vendedor.business_name or vendedor.username,
                'total': 0,
                'items': [],
                'pagado': 0,
                'paid': False
            }
        productores[vendedor.id]['total'] += float(item.get_total_price())
        productores[vendedor.id]['items'].append({
            'producto': item.product.name,
            'cantidad': item.quantity,
            'precio': float(item.product.price),
            'subtotal': float(item.get_total_price())
        })
    
    # ============================================================
    # 4. OBTENER EL CENTRO DE ACOPIO
    # ============================================================
    try:
        centro_acopio = User.objects.get(username='centro_acopio')
    except User.DoesNotExist:
        messages.error(request, '❌ Error: Centro de Acopio no configurado. Contacta al administrador.')
        return redirect('cart:ver_carrito')
    
    # ============================================================
    # 5. PROCESAR POST
    # ============================================================
    if request.method == 'POST':
        delivery_type = request.POST.get('delivery_type', 'delivery')
        shipping_address = request.POST.get('shipping_address', '')
        pickup_location = request.POST.get('pickup_location', '')
        phone_number = request.POST.get('phone_number', '')
        delivery_instructions = request.POST.get('delivery_instructions', '')
        
        # Validar según el tipo de entrega
        if delivery_type == 'delivery' and not shipping_address:
            messages.error(request, '❌ Por favor ingresa tu dirección de entrega.')
            return redirect('cart:checkout')
        
        if delivery_type == 'pickup' and not pickup_location:
            messages.error(request, '❌ Por favor selecciona dónde pasarás a recoger.')
            return redirect('cart:checkout')
        
        if not phone_number:
            messages.error(request, '❌ Por favor ingresa tu número de teléfono para la entrega.')
            return redirect('cart:checkout')
        
        # Convertir valores a float antes de guardar
        for prod_id, prod_data in productores.items():
            prod_data['total'] = float(prod_data['total'])
            prod_data['pagado'] = float(prod_data.get('pagado', 0))
        
        # Crear el pedido
        order = Order.objects.create(
            user=request.user,
            seller=centro_acopio,
            acopio=centro_acopio,
            delivery_type=delivery_type,
            shipping_address=shipping_address if delivery_type == 'delivery' else '',
            pickup_location=pickup_location if delivery_type == 'pickup' else '',
            phone_number=phone_number,
            delivery_instructions=delivery_instructions,
            total_amount=float(cart.get_total_price()),
            status='pending',
            payment_breakdown=productores
        )
        
        # Crear los items del pedido
        for item in items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )
        
        # Reducir stock y desactivar automáticamente
        for item in items:
            producto = item.product
            producto.stock -= item.quantity
            
            if producto.stock <= 0:
                producto.available = False
                producto.save()
                messages.info(request, f'🔒 "{producto.name}" se ha desactivado automáticamente por falta de stock.')
            else:
                producto.save()
        
        # Vaciar el carrito
        cart.clear_cart()
        
        messages.success(request, f'✅ ¡Pedido #{order.id} creado con éxito! El Centro de Acopio recibió tu pedido y te contactará para coordinar la entrega.')
        return redirect('cart:order_confirmation', order_id=order.id)
    
    # ============================================================
    # 6. GET: MOSTRAR FORMULARIO
    # ============================================================
    user_phone = request.user.phone if hasattr(request.user, 'phone') else ''
    
    context = {
        'cart': cart,
        'items': items,
        'total_items': cart.get_total_items(),
        'total_price': cart.get_total_price(),
        'user_phone': user_phone,
        'productores': productores,
        'total_productores': len(productores),
    }
    return render(request, 'cart/checkout.html', context)


# =============================================================================
# VISTA: order_confirmation
# =============================================================================
# Propósito: Paso 2 del proceso de compra. Muestra la confirmación del pedido.
#
# Parámetros:
#   - request: Objeto HttpRequest
#   - order_id: ID del pedido creado
#
# Retorna:
#   - HttpResponse: Renderiza 'cart/order_confirmation.html'
#
# URLs asociadas:
#   - /cart/confirmacion/<order_id>/
# =============================================================================
@login_required
def order_confirmation(request, order_id):
    """Paso 2: Confirmación del pedido"""
    from .models import Order
    order = get_object_or_404(Order, id=order_id, user=request.user)
    items = order.items.all().select_related('product')
    
    context = {
        'order': order,
        'items': items,
    }
    return render(request, 'cart/order_confirmation.html', context)


# =============================================================================
# VISTA: mis_pedidos
# =============================================================================
# Propósito: Muestra todos los pedidos realizados por el consumidor.
#
# Parámetros:
#   - request: Objeto HttpRequest
#
# Retorna:
#   - HttpResponse: Renderiza 'cart/mis_pedidos.html'
#
# URLs asociadas:
#   - /cart/mis-pedidos/
#
# Roles permitidos:
#   - ✅ Consumidor
# =============================================================================
@login_required
def mis_pedidos(request):
    """Ver todos los pedidos del consumidor"""
    from .models import Order
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    
    context = {
        'orders': orders,
    }
    return render(request, 'cart/mis_pedidos.html', context)


# =============================================================================
# VISTA: detalle_pedido
# =============================================================================
# Propósito: Muestra el detalle de un pedido específico.
#
# Parámetros:
#   - request: Objeto HttpRequest
#   - order_id: ID del pedido a consultar
#
# Retorna:
#   - HttpResponse: Renderiza 'cart/detalle_pedido.html'
#
# URLs asociadas:
#   - /cart/pedido/<order_id>/
# =============================================================================
@login_required
def detalle_pedido(request, order_id):
    """Ver detalle de un pedido específico"""
    from .models import Order
    order = get_object_or_404(Order, id=order_id, user=request.user)
    items = order.items.all().select_related('product')
    
    context = {
        'order': order,
        'items': items,
    }
    return render(request, 'cart/detalle_pedido.html', context)


# =============================================================================
# VISTAS PARA PRODUCTORES (VENTAS)
# =============================================================================

# =============================================================================
# VISTA: mis_ventas
# =============================================================================
# Propósito: Muestra los pedidos que contienen productos del productor.
#
# Parámetros:
#   - request: Objeto HttpRequest
#
# Retorna:
#   - HttpResponse: Renderiza 'cart/mis_ventas.html'
#
# URLs asociadas:
#   - /cart/mis-ventas/
#
# Roles permitidos:
#   - ✅ Productor
#   - ✅ Suplidor
#   - ❌ Consumidor
#   - ❌ Regulador
# =============================================================================
@login_required
def mis_ventas(request):
    """Vista para que los productores/suplidores vean SOLO los pedidos que contienen sus productos"""
    from .models import Order
    
    # Solo productores y suplidores pueden ver esto
    if request.user.role not in ['productor', 'suplidor']:
        messages.error(request, 'No tienes permiso para acceder a esta sección.')
        return redirect('inicio')
    
    # Filtrar pedidos que contienen productos del productor
    orders = Order.objects.filter(
        items__product__vendedor=request.user
    ).distinct().order_by('-created_at')
    
    context = {
        'orders': orders,
    }
    return render(request, 'cart/mis_ventas.html', context)


# =============================================================================
# VISTA: detalle_venta
# =============================================================================
# Propósito: Muestra el detalle de un pedido específico para el productor.
# Solo muestra los productos que pertenecen a ese productor.
#
# Parámetros:
#   - request: Objeto HttpRequest
#   - order_id: ID del pedido a consultar
#
# Retorna:
#   - HttpResponse: Renderiza 'cart/detalle_venta.html'
#
# URLs asociadas:
#   - /cart/detalle-venta/<order_id>/
# =============================================================================
@login_required
def detalle_venta(request, order_id):
    """Vista para que el productor vea SOLO los detalles de SUS productos en el pedido"""
    from .models import Order
    
    order = get_object_or_404(Order, id=order_id)
    
    # Verificar que el pedido contenga productos del productor
    tiene_mis_productos = order.items.filter(product__vendedor=request.user).exists()
    
    if not tiene_mis_productos:
        messages.error(request, '❌ No tienes permiso para ver este pedido. Este pedido no contiene productos tuyos.')
        return redirect('cart:mis_ventas')
    
    # Filtrar SOLO los productos del productor
    items = order.items.filter(product__vendedor=request.user).select_related('product')
    
    # Calcular el subtotal de los productos del productor
    subtotal = sum(item.get_total_price() for item in items)
    
    context = {
        'order': order,
        'items': items,
        'subtotal': subtotal,
        'total_productos': items.count(),
    }
    return render(request, 'cart/detalle_venta.html', context)


# =============================================================================
# VISTAS PARA CENTRO DE ACOPIO
# =============================================================================

# =============================================================================
# VISTA: pedidos_acopio
# =============================================================================
# Propósito: Muestra todos los pedidos gestionados por el Centro de Acopio.
# Incluye buscador por número de pedido o nombre del comprador.
#
# Parámetros:
#   - request: Objeto HttpRequest con GET (search)
#
# Retorna:
#   - HttpResponse: Renderiza 'cart/pedidos_acopio.html'
#
# URLs asociadas:
#   - /cart/pedidos-acopio/
#
# Roles permitidos:
#   - ✅ Centro de Acopio (acopio)
# =============================================================================
@login_required
def pedidos_acopio(request):
    """Vista para que el Centro de Acopio vea todos los pedidos con buscador"""
    from .models import Order
    from django.db.models import Q
    
    # Solo el centro de acopio puede ver esto
    if request.user.role != 'acopio' and request.user.username != 'centro_acopio':
        messages.error(request, 'No tienes permiso para acceder a esta sección.')
        return redirect('inicio')
    
    # Buscador por número de pedido o nombre
    search_query = request.GET.get('search', '').strip()
    
    # Base de la consulta: pedidos del centro de acopio
    orders = Order.objects.filter(acopio=request.user)
    
    if search_query:
        if search_query.isdigit():
            orders = orders.filter(id=int(search_query))
        else:
            orders = orders.filter(
                Q(user__username__icontains=search_query) |
                Q(user__first_name__icontains=search_query) |
                Q(user__last_name__icontains=search_query)
            )
    
    orders = orders.order_by('-created_at')
    
    context = {
        'orders': orders,
        'search_query': search_query,
        'total_pedidos': orders.count(),
    }
    return render(request, 'cart/pedidos_acopio.html', context)


# =============================================================================
# VISTA: detalle_acopio
# =============================================================================
# Propósito: Muestra el detalle de un pedido para el Centro de Acopio,
# incluyendo el desglose de pagos por productor.
#
# Parámetros:
#   - request: Objeto HttpRequest
#   - order_id: ID del pedido a consultar
#
# Retorna:
#   - HttpResponse: Renderiza 'cart/detalle_acopio.html'
#
# URLs asociadas:
#   - /cart/detalle-acopio/<order_id>/
# =============================================================================
@login_required
def detalle_acopio(request, order_id):
    """Vista para que el Centro de Acopio vea detalles del pedido"""
    from .models import Order
    
    order = get_object_or_404(Order, id=order_id, acopio=request.user)
    items = order.items.all().select_related('product')
    
    # Obtener el desglose de pagos
    payment_breakdown = order.payment_breakdown or {}
    
    # Calcular el pendiente para cada productor
    for prod_id, prod_data in payment_breakdown.items():
        prod_data['pendiente'] = prod_data.get('total', 0) - prod_data.get('pagado', 0)
    
    context = {
        'order': order,
        'items': items,
        'productores': payment_breakdown,
    }
    return render(request, 'cart/detalle_acopio.html', context)


# =============================================================================
# VISTA: actualizar_estado_pedido
# =============================================================================
# Propósito: Permite al productor o al Centro de Acopio actualizar el estado
# de un pedido (pendiente, confirmado, preparando, entregado, cancelado).
#
# Parámetros:
#   - request: Objeto HttpRequest (POST)
#   - order_id: ID del pedido a actualizar
#
# Retorna:
#   - HttpResponse: Redirige al detalle correspondiente
#
# URLs asociadas:
#   - /cart/actualizar-estado/<order_id>/
# =============================================================================
@login_required
def actualizar_estado_pedido(request, order_id):
    """Vista para que el productor o el Centro de Acopio actualice el estado del pedido"""
    from .models import Order
    
    order = get_object_or_404(Order, id=order_id)
    
    # Verificar permisos
    es_productor = (order.seller == request.user)
    es_acopio = (order.acopio == request.user) or (request.user.username == 'centro_acopio')
    
    if not es_productor and not es_acopio:
        messages.error(request, 'No tienes permiso para realizar esta acción.')
        return redirect('inicio')
    
    if request.method == 'POST':
        nuevo_estado = request.POST.get('status')
        if nuevo_estado in ['pending', 'confirmed', 'preparing', 'delivered', 'cancelled']:
            order.status = nuevo_estado
            order.save()
            messages.success(request, f'✅ Estado del pedido #{order.id} actualizado a: {order.get_status_display()}')
        else:
            messages.error(request, '❌ Estado no válido')
    
    # Redirigir según quien hizo la acción
    if es_acopio:
        return redirect('cart:detalle_acopio', order_id=order.id)
    else:
        return redirect('cart:detalle_venta', order_id=order.id)


# =============================================================================
# VISTA: balance_ventas
# =============================================================================
# Propósito: Muestra el balance de ventas del productor con tres métricas:
#   1. Total Vendido
#   2. Total Pagado
#   3. Pendiente de Pago
#
# Parámetros:
#   - request: Objeto HttpRequest
#
# Retorna:
#   - HttpResponse: Renderiza 'cart/balance_ventas.html'
#
# URLs asociadas:
#   - /cart/balance-ventas/
#
# Roles permitidos:
#   - ✅ Productor
#   - ✅ Suplidor
#   - ❌ Consumidor
#   - ❌ Regulador
#   - ❌ Centro de Acopio
#
# Cálculo:
#   - total_vendido: Suma de todos los subtotales de productos del productor
#   - total_pagado: Suma de los subtotales donde payment_status = 'paid'
#   - total_pendiente: total_vendido - total_pagado
# =============================================================================
@login_required
def balance_ventas(request):
    """Vista para que los productores vean su balance de ventas y lo que se les debe"""
    from .models import Order, OrderItem
    
    # Solo productores y suplidores pueden ver esto
    if request.user.role not in ['productor', 'suplidor']:
        messages.error(request, 'No tienes permiso para acceder a esta sección.')
        return redirect('inicio')
    
    # Obtener todos los pedidos que tienen productos de este productor
    orders_with_my_products = Order.objects.filter(
        items__product__vendedor=request.user
    ).distinct().order_by('-created_at')
    
    # Calcular totales
    total_vendido = 0.0
    total_pagado = 0.0
    
    ventas_detalle = []
    
    for order in orders_with_my_products:
        # Filtrar solo los items de este productor en este pedido
        mis_items = order.items.filter(product__vendedor=request.user)
        
        if mis_items.exists():
            subtotal = sum(item.get_total_price() for item in mis_items)
            total_vendido += float(subtotal)
            
            # Verificar si este productor ha sido pagado en este pedido
            payment_breakdown = order.payment_breakdown or {}
            productor_id_str = str(request.user.id)
            productor_data = payment_breakdown.get(productor_id_str, {})
            pagado_productor = productor_data.get('pagado', 0)
            
            # Si el pago está marcado como 'paid' o el pagado es mayor o igual al total
            if productor_data.get('paid', False) or pagado_productor >= subtotal:
                total_pagado += float(subtotal)
            
            # Obtener productos
            productos = []
            for item in mis_items:
                productos.append({
                    'nombre': item.product.name,
                    'cantidad': item.quantity,
                    'precio': float(item.price),
                    'subtotal': float(item.get_total_price())
                })
            
            ventas_detalle.append({
                'order_id': order.id,
                'order': order,
                'fecha': order.created_at,
                'status': order.status,
                'payment_status': order.payment_status,
                'payment_status_display': order.get_payment_status_display_icon(),
                'subtotal': float(subtotal),
                'pagado': float(pagado_productor),
                'productos': productos,
            })
    
    # Calcular pendiente de pago
    total_pendiente = total_vendido - total_pagado
    
    context = {
        'ventas_detalle': ventas_detalle,
        'total_vendido': float(total_vendido),
        'total_pagado': float(total_pagado),
        'total_pendiente': float(total_pendiente),
    }
    return render(request, 'cart/balance_ventas.html', context)


# =============================================================================
# VISTA: registrar_pago_productor
# =============================================================================
# Propósito: Permite al Centro de Acopio registrar el pago TOTAL a un productor.
# NO se permiten pagos parciales.
#
# Parámetros:
#   - request: Objeto HttpRequest (POST)
#   - order_id: ID del pedido
#   - productor_id: ID del productor a pagar
#
# Retorna:
#   - HttpResponse: Redirige a 'detalle_acopio'
#
# URLs asociadas:
#   - /cart/registrar-pago/<order_id>/<productor_id>/
#
# Roles permitidos:
#   - ✅ Centro de Acopio (acopio)
#
# Restricciones:
#   - El pedido debe estar entregado (status='delivered')
#   - Solo se permite pago total, no parcial
# =============================================================================
@login_required
def registrar_pago_productor(request, order_id, productor_id):
    """
    El Centro de Acopio registra el pago TOTAL a un productor.
    NO se permiten pagos parciales.
    """
    from .models import Order
    
    # Verificar que el usuario sea el centro de acopio
    if request.user.role != 'acopio' and request.user.username != 'centro_acopio':
        messages.error(request, 'No tienes permiso para realizar esta acción.')
        return redirect('inicio')
    
    # Obtener el pedido
    order = get_object_or_404(Order, id=order_id, acopio=request.user)
    
    # Verificar que el pedido esté entregado
    if order.status != 'delivered':
        messages.error(request, '❌ Este pedido aún no ha sido entregado. No se puede pagar hasta que esté entregado.')
        return redirect('cart:detalle_acopio', order_id=order.id)
    
    # Obtener el desglose de pagos
    payment_breakdown = order.payment_breakdown or {}
    productor_id_str = str(productor_id)
    
    if productor_id_str not in payment_breakdown:
        messages.error(request, '❌ Productor no encontrado en este pedido.')
        return redirect('cart:detalle_acopio', order_id=order.id)
    
    # Obtener datos del productor
    productor_data = payment_breakdown[productor_id_str]
    total_debe = productor_data.get('total', 0)
    
    # FORZAR PAGO TOTAL
    productor_data['pagado'] = float(total_debe)
    productor_data['paid'] = True
    
    # Guardar
    payment_breakdown[productor_id_str] = productor_data
    order.payment_breakdown = payment_breakdown
    
    # Verificar si todos los productores han sido pagados completamente
    todos_pagados = all(item.get('paid', False) for item in payment_breakdown.values())
    if todos_pagados:
        order.payment_status = 'paid'
    else:
        algun_pagado = any(item.get('pagado', 0) > 0 for item in payment_breakdown.values())
        if algun_pagado:
            order.payment_status = 'partial'
        else:
            order.payment_status = 'pending'
    
    order.save()
    
    messages.success(
        request, 
        f'✅ Pago TOTAL de RD$ {total_debe:.2f} registrado para {productor_data["nombre"]}'
    )
    
    return redirect('cart:detalle_acopio', order_id=order.id)