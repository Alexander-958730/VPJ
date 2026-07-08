"""
APPS.MARKETPLACE.VIEWS
======================
Vistas para el marketplace de productos, gestión de categorías y búsquedas.

Este módulo contiene todas las vistas relacionadas con:
- Lista y detalle de productos (público)
- Gestión de productos (crear, editar, eliminar) para productores/suplidores
- Productos más consultados (ONPECO)
- Búsqueda en tiempo real (API)
- Gestión de categorías (ONPECO)
- Productos en común (validación entre productores)

Roles de usuario:
- consumidor: Puede ver productos y detalles
- productor: Puede gestionar sus productos (CRUD)
- suplidor: Puede gestionar sus productos (CRUD)
- regulador (ONPECO): Acceso a productos más consultados, gestión de categorías
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import F, Q
from django.http import JsonResponse
from .models import Product
from .forms import ProductoForm
from apps.complaints.views import onpeco_required


# =============================================================================
# VISTAS PÚBLICAS DE PRODUCTOS
# =============================================================================

# =============================================================================
# VISTA: lista_productos
# =============================================================================
# Propósito: Muestra la lista de productos disponibles para compra.
# Incluye búsqueda por nombre/descripción y filtro por categoría.
#
# Parámetros:
#   - request: Objeto HttpRequest con GET (q, categoria)
#
# Retorna:
#   - HttpResponse: Renderiza 'marketplace/lista_productos.html'
#
# URLs asociadas:
#   - /productos/
#
# Roles permitidos:
#   - ✅ Todos los visitantes
#
# Características:
#   - Solo muestra productos disponibles (available=True, stock>0)
#   - Búsqueda por nombre o descripción
#   - Filtro por categoría
# =============================================================================
def lista_productos(request):
    """
    Vista para que los consumidores vean todos los productos disponibles
    Con búsqueda y filtrado por categoría
    """
    # ============================================================
    # 1. FILTRAR PRODUCTOS DISPONIBLES
    # ============================================================
    productos = Product.objects.filter(available=True, stock__gt=0)
    
    # ============================================================
    # 2. OBTENER PARÁMETROS DE BÚSQUEDA
    # ============================================================
    query = request.GET.get('q', '')
    categoria = request.GET.get('categoria', '')
    
    # Filtrar por búsqueda (nombre o descripción)
    if query:
        productos = productos.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )
    
    # Filtrar por categoría
    if categoria and categoria != 'todos':
        productos = productos.filter(category=categoria)
    
    # ============================================================
    # 3. OBTENER CATEGORÍAS DISPONIBLES PARA EL FILTRO
    # ============================================================
    from .constants import CATEGORIAS
    categorias_traduccion = dict(CATEGORIAS)
    
    categorias_raw = Product.objects.filter(available=True).values_list('category', flat=True).distinct()
    
    categorias_opciones = []
    for cat in categorias_raw:
        if cat:
            categorias_opciones.append({
                'valor': cat,
                'nombre': categorias_traduccion.get(cat, cat.capitalize())
            })
    
    context = {
        'productos': productos,
        'query': query,
        'categoria_seleccionada': categoria,
        'categorias': categorias_opciones,
        'total_productos': productos.count(),
    }
    return render(request, 'marketplace/lista_productos.html', context)


# =============================================================================
# VISTA: detalle_producto
# =============================================================================
# Propósito: Muestra el detalle completo de un producto específico.
# Incrementa automáticamente el contador de visitas.
#
# Parámetros:
#   - request: Objeto HttpRequest
#   - producto_id: ID del producto a mostrar
#
# Retorna:
#   - HttpResponse: Renderiza 'marketplace/detalle_producto.html'
#
# URLs asociadas:
#   - /productos/<producto_id>/
#
# Roles permitidos:
#   - ✅ Todos los visitantes
#
# Características:
#   - Incrementa view_count al visitar la página
#   - Muestra trazabilidad si el vendedor es suplidor
# =============================================================================
def detalle_producto(request, producto_id):
    """
    Vista para ver el detalle de un producto específico
    """
    producto = get_object_or_404(Product, id=producto_id, available=True)
    
    # Incrementar contador de visitas
    Product.objects.filter(pk=producto.pk).update(view_count=F('view_count') + 1)
    
    # Mostrar información de trazabilidad si el vendedor es suplidor
    mostrar_trazabilidad = (
        producto.vendedor.role == 'suplidor' and 
        hasattr(producto, 'precio_compra_productor') and 
        producto.precio_compra_productor
    )
    
    return render(request, 'marketplace/detalle_producto.html', {
        'producto': producto,
        'mostrar_trazabilidad': mostrar_trazabilidad
    })


# =============================================================================
# GESTIÓN DE PRODUCTOS (PRODUCTORES/SUPLIDORES)
# =============================================================================

# =============================================================================
# VISTA: mis_productos
# =============================================================================
# Propósito: Muestra los productos que ha publicado el productor/suplidor.
#
# Parámetros:
#   - request: Objeto HttpRequest
#
# Retorna:
#   - HttpResponse: Renderiza 'marketplace/mis_productos.html'
#
# URLs asociadas:
#   - /productos/mis-productos/
#
# Roles permitidos:
#   - ✅ Productor
#   - ✅ Suplidor
#   - ❌ Consumidor
#   - ❌ Regulador
# =============================================================================
@login_required
def mis_productos(request):
    """
    Vista para que productores y suplidores vean sus productos
    """
    if request.user.role not in ['productor', 'suplidor']:
        messages.error(request, 'Solo productores y suplidores pueden acceder a esta página.')
        return redirect('inicio')
    
    productos = Product.objects.filter(vendedor=request.user)
    return render(request, 'marketplace/mis_productos.html', {'productos': productos})


# =============================================================================
# VISTA: crear_producto
# =============================================================================
# Propósito: Permite a un productor/suplidor crear un nuevo producto.
#
# Parámetros:
#   - request: Objeto HttpRequest (GET, POST)
#
# Retorna:
#   - GET: Renderiza 'marketplace/crear_producto.html' con el formulario
#   - POST: Valida, crea el producto y redirige a 'mis_productos'
#
# URLs asociadas:
#   - /productos/crear/
#
# Roles permitidos:
#   - ✅ Productor (aprobado)
#   - ✅ Suplidor (aprobado)
#   - ❌ Consumidor
#   - ❌ Regulador
#
# Validaciones:
#   - Usuario debe estar aprobado (is_approved=True)
#   - Suplidores deben especificar productor_origen y precio_compra_productor
# =============================================================================
@login_required
def crear_producto(request):
    """
    Vista para que productores y suplidores creen nuevos productos
    """
    if request.user.role not in ['productor', 'suplidor']:
        messages.error(request, 'Solo productores y suplidores pueden crear productos.')
        return redirect('inicio')
    
    if not request.user.is_approved:
        messages.error(request, 'Tu cuenta está pendiente de aprobación. Espera la verificación de ONPECO.')
        return redirect('inicio')
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.vendedor = request.user
            
            # Validaciones específicas para suplidores
            if request.user.role == 'suplidor':
                producto.productor_origen = form.cleaned_data.get('productor_origen')
                producto.precio_compra_productor = form.cleaned_data.get('precio_compra_productor')
            
            producto.save()
            messages.success(request, f'✅ Producto "{producto.name}" creado exitosamente.')
            return redirect('marketplace:mis_productos')
        else:
            messages.error(request, '❌ Por favor corrige los errores en el formulario.')
    else:
        form = ProductoForm(user=request.user)
    
    return render(request, 'marketplace/crear_producto.html', {'form': form})


# =============================================================================
# VISTA: editar_producto
# =============================================================================
# Propósito: Permite a un productor/suplidor editar un producto existente.
#
# Parámetros:
#   - request: Objeto HttpRequest (GET, POST)
#   - producto_id: ID del producto a editar
#
# Retorna:
#   - GET: Renderiza 'marketplace/editar_producto.html' con el formulario
#   - POST: Valida, actualiza el producto y redirige a 'mis_productos'
#
# URLs asociadas:
#   - /productos/editar/<producto_id>/
#
# Roles permitidos:
#   - ✅ Productor (dueño del producto)
#   - ✅ Suplidor (dueño del producto)
#
# Seguridad:
#   - Solo el vendedor del producto puede editarlo
#   - Verificación de propiedad con get_object_or_404
# =============================================================================
@login_required
def editar_producto(request, producto_id):
    """
    Vista para que productores y suplidores editen sus productos
    """
    producto = get_object_or_404(Product, id=producto_id, vendedor=request.user)
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto, user=request.user)
        if form.is_valid():
            producto = form.save(commit=False)
            
            # Guardar campo "available" desde el formulario
            if 'available' in request.POST:
                producto.available = request.POST.get('available') == 'on'
            
            if request.user.role == 'suplidor':
                producto.productor_origen = form.cleaned_data.get('productor_origen')
                producto.precio_compra_productor = form.cleaned_data.get('precio_compra_productor')
            
            producto.save()
            messages.success(request, '✅ Producto actualizado exitosamente.')
            return redirect('marketplace:mis_productos')
        else:
            messages.error(request, '❌ Por favor corrige los errores en el formulario.')
    else:
        form = ProductoForm(instance=producto, user=request.user)
    
    return render(request, 'marketplace/editar_producto.html', {'form': form, 'producto': producto})


# =============================================================================
# VISTA: eliminar_producto
# =============================================================================
# Propósito: Permite a un productor/suplidor eliminar (ocultar) un producto.
# El producto no se elimina físicamente, solo se marca como no disponible.
#
# Parámetros:
#   - request: Objeto HttpRequest
#   - producto_id: ID del producto a eliminar
#
# Retorna:
#   - HttpResponse: Redirige a 'mis_productos'
#
# URLs asociadas:
#   - /productos/eliminar/<producto_id>/
#
# Roles permitidos:
#   - ✅ Productor (dueño del producto)
#   - ✅ Suplidor (dueño del producto)
# =============================================================================
@login_required
def eliminar_producto(request, producto_id):
    """
    Vista para que productores y suplidores eliminen (oculten) sus productos
    """
    producto = get_object_or_404(Product, id=producto_id, vendedor=request.user)
    producto.available = False
    producto.save()
    
    messages.success(request, f'✅ Producto "{producto.name}" eliminado.')
    return redirect('marketplace:mis_productos')


# =============================================================================
# VISTAS PARA ONPECO
# =============================================================================

# =============================================================================
# VISTA: productos_mas_vistos
# =============================================================================
# Propósito: Muestra a ONPECO el ranking de los 10 productos más consultados.
#
# Parámetros:
#   - request: Objeto HttpRequest
#
# Retorna:
#   - HttpResponse: Renderiza 'marketplace/productos_mas_vistos.html'
#
# URLs asociadas:
#   - /productos/top-vistos/
#
# Roles permitidos:
#   - ✅ Regulador (ONPECO)
# =============================================================================
@onpeco_required
def productos_mas_vistos(request):
    """
    Vista para ONPECO: Muestra los 10 productos más consultados
    """
    productos_top = Product.objects.filter(available=True).order_by('-view_count')[:10]
    return render(request, 'marketplace/productos_mas_vistos.html', {'productos_top': productos_top})


# =============================================================================
# BÚSQUEDA EN TIEMPO REAL (API)
# =============================================================================

# =============================================================================
# VISTA: buscar_productos_tiempo_real
# =============================================================================
# Propósito: API para búsqueda de productos en tiempo real.
# Devuelve resultados en formato JSON para consumo por JavaScript.
#
# Parámetros:
#   - request: Objeto HttpRequest con GET (q)
#
# Retorna:
#   - JsonResponse: Lista de productos encontrados
#
# URLs asociadas:
#   - /productos/api/buscar-productos/
#
# Roles permitidos:
#   - ✅ Todos los visitantes
#
# Características:
#   - Mínimo 2 caracteres para iniciar la búsqueda
#   - Busca en nombre, descripción y categoría
#   - Limita a 10 resultados
# =============================================================================
def buscar_productos_tiempo_real(request):
    """
    API para búsqueda de productos en tiempo real
    GET: ?q=texto
    """
    query = request.GET.get('q', '').strip()
    
    if len(query) < 2:
        return JsonResponse({'productos': [], 'total': 0, 'query': query})
    
    productos = Product.objects.filter(
        Q(name__icontains=query) |
        Q(description__icontains=query) |
        Q(category__icontains=query),
        available=True
    ).select_related('vendedor', 'productor_origen')[:10]
    
    data = []
    for p in productos:
        vendedor_nombre = p.vendedor.get_full_name() if p.vendedor else (p.vendedor.username if p.vendedor else '')
        productor_nombre = p.productor_origen.get_full_name() if p.productor_origen else (p.productor_origen.username if p.productor_origen else '')
        
        data.append({
            'id': p.id,
            'name': p.name,
            'price': float(p.price),
            'category': p.get_category_display(),
            'subcategory': p.get_subcategory_display(),
            'unit': p.get_unit_display(),
            'stock': p.stock,
            'image': p.image.url if p.image else '/static/images/no-image.png',
            'vendedor': vendedor_nombre,
            'productor': productor_nombre,
            'url': f'/productos/{p.id}/'
        })
    
    return JsonResponse({
        'productos': data,
        'total': len(data),
        'query': query
    })


# =============================================================================
# VISTA: buscar_suplidores_tiempo_real
# =============================================================================
# Propósito: API para búsqueda de suplidores en tiempo real.
# (Desactivado junto con el rol Suplidor)
#
# Parámetros:
#   - request: Objeto HttpRequest con GET (q)
#
# Retorna:
#   - JsonResponse: Lista de suplidores encontrados
#
# URLs asociadas:
#   - /productos/api/buscar-suplidores/
#
# Estado: ⛔ DESACTIVADO
# =============================================================================
def buscar_suplidores_tiempo_real(request):
    """
    API para búsqueda de suplidores en tiempo real (DESACTIVADO)
    GET: ?q=texto
    """
    from apps.users.models import User
    
    query = request.GET.get('q', '').strip()
    
    if len(query) < 2:
        return JsonResponse({'suplidores': [], 'total': 0, 'query': query})
    
    suplidores = User.objects.filter(
        Q(role='suplidor'),
        Q(username__icontains=query) |
        Q(first_name__icontains=query) |
        Q(last_name__icontains=query) |
        Q(email__icontains=query)
    )[:10]
    
    data = []
    for s in suplidores:
        data.append({
            'id': s.id,
            'nombre': s.get_full_name() or s.username,
            'business_name': getattr(s, 'business_name', ''),
            'email': s.email,
            'telefono': getattr(s, 'telefono', ''),
            'url': f'/users/perfil/{s.id}/'
        })
    
    return JsonResponse({
        'suplidores': data,
        'total': len(data),
        'query': query
    })


# =============================================================================
# VISTA: busqueda_tiempo_real_view
# =============================================================================
# Propósito: Vista principal para la página de búsqueda en tiempo real.
#
# Parámetros:
#   - request: Objeto HttpRequest
#
# Retorna:
#   - HttpResponse: Renderiza 'marketplace/busqueda_tiempo_real.html'
#
# URLs asociadas:
#   - /productos/busqueda-tiempo-real/
# =============================================================================
def busqueda_tiempo_real_view(request):
    """
    Vista principal de búsqueda en tiempo real
    """
    return render(request, 'marketplace/busqueda_tiempo_real.html')


# =============================================================================
# GESTIÓN DE CATEGORÍAS (ONPECO)
# =============================================================================

from .models import CategoriaProducto, SubcategoriaProducto

# =============================================================================
# VISTA: gestion_categorias
# =============================================================================
# Propósito: Permite a ONPECO gestionar las categorías y subcategorías
# del marketplace.
#
# Parámetros:
#   - request: Objeto HttpRequest
#
# Retorna:
#   - HttpResponse: Renderiza 'marketplace/gestion_categorias.html'
#
# URLs asociadas:
#   - /productos/gestion-categorias/
#
# Roles permitidos:
#   - ✅ Regulador (ONPECO)
#
# Características:
#   - Lista todas las categorías existentes
#   - Permite crear, editar y eliminar categorías
#   - Permite gestionar subcategorías
# =============================================================================
@onpeco_required
def gestion_categorias(request):
    """Vista para que ONPECO gestione categorías y subcategorías"""
    categorias = CategoriaProducto.objects.all().order_by('nombre')
    context = {
        'categorias': categorias,
    }
    return render(request, 'marketplace/gestion_categorias.html', context)