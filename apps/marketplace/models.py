"""
APPS.MARKETPLACE.MODELS
=======================
Modelos de datos para el marketplace de productos.

Este módulo contiene los modelos que gestionan:
- Categorías dinámicas de productos (gestionadas por ONPECO)
- Subcategorías dinámicas de productos
- Productos publicados por productores/suplidores

Relaciones:
    - CategoriaProducto → SubcategoriaProducto (uno a muchos)
    - Product → User (vendedor)
    - Product → User (productor_origen - solo para suplidores)
    - Product → CategoriaProducto (categoría)
    - Product → SubcategoriaProducto (subcategoría)

Roles de usuario:
- productor: Crea productos (puede tener subcategorías)
- suplidor: Crea productos (debe especificar productor_origen y precio_compra_productor)
- regulador (ONPECO): Gestiona categorías y subcategorías
"""

from django.db import models
from django.conf import settings
from .constants import CATEGORIAS, UNIDADES, SUBCATEGORIAS


# =============================================================================
# MODELO: CategoriaProducto
# =============================================================================
# Propósito: Almacena categorías dinámicas de productos que ONPECO puede
# gestionar (crear, editar, eliminar).
#
# Campos principales:
#   - nombre: Nombre de la categoría (único)
#   - icono: Emoji o ícono para la categoría (ej: 🍎, 🥬, 🌾)
#   - activo: Indica si la categoría está activa
#   - creado_por: Usuario de ONPECO que la creó
#   - creado_en: Fecha de creación
#   - actualizado_en: Fecha de última actualización
#
# Métodos:
#   - get_subcategorias_activas(): Retorna subcategorías activas
#
# Relaciones:
#   - subcategorias: Subcategorías asociadas (ForeignKey)
# =============================================================================
class CategoriaProducto(models.Model):
    """Modelo para categorías dinámicas que ONPECO puede gestionar"""
    
    # ============================================================
    # CAMPOS PRINCIPALES
    # ============================================================
    nombre = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Nombre de la categoría'
    )
    icono = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        help_text='Ej: 🍎, 🥬, 🌾'
    )
    activo = models.BooleanField(
        default=True,
        verbose_name='Categoría activa'
    )
    
    # ============================================================
    # AUDITORÍA
    # ============================================================
    creado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='categorias_creadas',
        help_text="Usuario de ONPECO que creó la categoría"
    )
    creado_en = models.DateTimeField(
        auto_now_add=True,
        help_text="Fecha y hora de creación"
    )
    actualizado_en = models.DateTimeField(
        auto_now=True,
        help_text="Fecha y hora de última actualización"
    )
    
    # ============================================================
    # MÉTODOS
    # ============================================================
    def __str__(self):
        """Representación legible del objeto"""
        return f"{self.icono or ''} {self.nombre}"
    
    def get_subcategorias_activas(self):
        """Retorna las subcategorías activas de esta categoría"""
        return self.subcategorias.filter(activo=True)
    
    # ============================================================
    # CONFIGURACIÓN
    # ============================================================
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['nombre']


# =============================================================================
# MODELO: SubcategoriaProducto
# =============================================================================
# Propósito: Almacena subcategorías dinámicas de productos que ONPECO puede
# gestionar. Cada subcategoría pertenece a una categoría.
#
# Campos principales:
#   - categoria: Categoría padre
#   - nombre: Nombre de la subcategoría
#   - icono: Emoji o ícono para la subcategoría
#   - activo: Indica si la subcategoría está activa
#   - creado_por: Usuario de ONPECO que la creó
#
# Restricciones:
#   - Una subcategoría no puede repetirse en la misma categoría (unique_together)
#
# Relaciones:
#   - categoria: Categoría asociada (ForeignKey)
# =============================================================================
class SubcategoriaProducto(models.Model):
    """Modelo para subcategorías dinámicas que ONPECO puede gestionar"""
    
    # ============================================================
    # RELACIONES
    # ============================================================
    categoria = models.ForeignKey(
        CategoriaProducto,
        on_delete=models.CASCADE,
        related_name='subcategorias',
        help_text="Categoría a la que pertenece esta subcategoría"
    )
    
    # ============================================================
    # CAMPOS PRINCIPALES
    # ============================================================
    nombre = models.CharField(
        max_length=50,
        verbose_name='Nombre de la subcategoría'
    )
    icono = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        help_text='Ej: 🍊, 🥕, 🌿'
    )
    activo = models.BooleanField(
        default=True,
        verbose_name='Subcategoría activa'
    )
    
    # ============================================================
    # AUDITORÍA
    # ============================================================
    creado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='subcategorias_creadas',
        help_text="Usuario de ONPECO que creó la subcategoría"
    )
    creado_en = models.DateTimeField(
        auto_now_add=True,
        help_text="Fecha y hora de creación"
    )
    actualizado_en = models.DateTimeField(
        auto_now=True,
        help_text="Fecha y hora de última actualización"
    )
    
    # ============================================================
    # MÉTODOS
    # ============================================================
    def __str__(self):
        """Representación legible del objeto"""
        return f"{self.icono or ''} {self.nombre} ({self.categoria.nombre})"
    
    # ============================================================
    # CONFIGURACIÓN
    # ============================================================
    class Meta:
        verbose_name = 'Subcategoría'
        verbose_name_plural = 'Subcategorías'
        ordering = ['nombre']
        unique_together = ['categoria', 'nombre']


# =============================================================================
# MODELO: Product
# =============================================================================
# Propósito: Almacena los productos publicados por productores y suplidores.
# Es el modelo principal del marketplace.
#
# Campos principales:
#   - vendedor: Usuario que vende el producto (productor/suplidor)
#   - productor_origen: Productor original (obligatorio para suplidores)
#   - name: Nombre del producto
#   - description: Descripción detallada
#   - category: Categoría del producto
#   - subcategory: Subcategoría del producto
#   - price: Precio de venta al consumidor
#   - precio_compra_productor: Precio de compra al productor (solo suplidores)
#   - unit: Unidad de medida
#   - stock: Cantidad disponible
#   - stock_minimo: Alerta de stock bajo
#   - image: Imagen del producto
#   - available: Disponible para venta
#   - view_count: Contador de visitas
#
# Validaciones:
#   - Suplidores deben especificar productor_origen y precio_compra_productor
#   - precio_venta debe ser mayor que precio_compra (para suplidores)
#   - Si stock <= 0, available = False automáticamente
#
# Propiedades:
#   - stock_bajo: True si stock <= stock_minimo
#   - margen_suplidor: Calcula margen de ganancia del suplidor
#
# Métodos:
#   - get_category_display(): Retorna nombre legible de categoría
#   - get_subcategory_display(): Retorna nombre legible de subcategoría
#   - get_unit_display(): Retorna nombre legible de unidad
#   - save(): Validaciones automáticas al guardar
# =============================================================================
class Product(models.Model):
    """
    Modelo de producto para el marketplace
    """
    
    # ============================================================
    # RELACIONES
    # ============================================================
    
    # Vendedor (productor o suplidor)
    vendedor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='products',
        help_text="Usuario que vende el producto (productor o suplidor)"
    )
    
    # Productor original (solo para suplidores)
    productor_origen = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='productos_origen',
        limit_choices_to={'role': 'productor', 'is_approved': True},
        help_text="Productor original del producto (obligatorio para suplidores)"
    )
    
    # ============================================================
    # DATOS DEL PRODUCTO
    # ============================================================
    name = models.CharField(
        max_length=100,
        verbose_name='Nombre del producto'
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Descripción'
    )
    
    # ============================================================
    # CATEGORÍAS (desde constants.py)
    # ============================================================
    category = models.CharField(
        max_length=50,
        choices=CATEGORIAS,
        default='frutas',
        verbose_name='Categoría'
    )
    subcategory = models.CharField(
        max_length=50,
        verbose_name='Subcategoría',
        help_text="Subcategoría específica del producto (obligatorio)"
    )
    
    # ============================================================
    # PRECIOS
    # ============================================================
    precio_compra_productor = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="Precio al que el suplidor compró al productor (solo para suplidores)"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Precio de venta al consumidor"
    )
    
    # ============================================================
    # UNIDADES (desde constants.py)
    # ============================================================
    unit = models.CharField(
        max_length=20,
        choices=UNIDADES,
        default='lb',
        verbose_name='Unidad de medida'
    )
    
    # ============================================================
    # STOCK Y DISPONIBILIDAD
    # ============================================================
    stock = models.PositiveIntegerField(
        default=0,
        verbose_name='Stock disponible'
    )
    stock_minimo = models.PositiveIntegerField(
        default=5,
        help_text="Stock mínimo para activar alerta"
    )
    
    # ============================================================
    # IMAGEN
    # ============================================================
    image = models.ImageField(
        upload_to='products/',
        blank=True,
        null=True,
        help_text="Imagen del producto (opcional)"
    )
    
    # ============================================================
    # ESTADO Y CONTADORES
    # ============================================================
    available = models.BooleanField(
        default=True,
        verbose_name='Disponible para venta'
    )
    view_count = models.IntegerField(
        default=0,
        help_text="Número de veces que se ha visto este producto"
    )
    
    # ============================================================
    # FECHAS
    # ============================================================
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Fecha y hora de creación del producto"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Fecha y hora de última actualización"
    )
    
    # ============================================================
    # PROPIEDADES
    # ============================================================
    
    @property
    def stock_bajo(self):
        """Verifica si el stock está por debajo del mínimo"""
        return self.stock <= self.stock_minimo
    
    @property
    def margen_suplidor(self):
        """
        Calcula el margen de ganancia del suplidor (si aplica).
        
        Retorna:
            - dict: {'margen': float, 'porcentaje': float} si aplica
            - None: si no aplica
        """
        if self.precio_compra_productor and self.precio_compra_productor > 0:
            margen = float(self.price) - float(self.precio_compra_productor)
            porcentaje = (margen / float(self.precio_compra_productor)) * 100
            return {'margen': margen, 'porcentaje': porcentaje}
        return None
    
    # ============================================================
    # MÉTODOS
    # ============================================================
    
    def get_category_display(self):
        """Retorna el nombre legible de la categoría"""
        for key, value in CATEGORIAS:
            if key == self.category:
                return value
        return self.category
    
    def get_subcategory_display(self):
        """Retorna el nombre legible de la subcategoría"""
        subcats = SUBCATEGORIAS.get(self.category, [])
        for key, value in subcats:
            if key == self.subcategory:
                return value
        return self.subcategory or 'Sin subcategoría'
    
    def get_unit_display(self):
        """Retorna el nombre legible de la unidad"""
        for key, value in UNIDADES:
            if key == self.unit:
                return value
        return self.unit
    
    def __str__(self):
        """Representación legible del objeto"""
        tipo_vendedor = "Suplidor" if self.vendedor.role == 'suplidor' else "Productor"
        return f"{self.name} - {tipo_vendedor}: {self.vendedor.username}"
    
    # ============================================================
    # VALIDACIONES AL GUARDAR
    # ============================================================
    
    def save(self, *args, **kwargs):
        """
        Validaciones automáticas al guardar el producto:
        1. Si stock <= 0, desactivar automáticamente
        2. Suplidores deben tener productor_origen y precio_compra_productor
        3. Suplidores: precio_venta debe ser mayor que precio_compra
        """
        # Si el stock llega a 0, desactivar automáticamente
        if self.stock <= 0:
            self.available = False
        
        # ============================================================
        # VALIDACIÓN PARA SUPLIDORES
        # ============================================================
        if self.vendedor.role == 'suplidor':
            if not self.productor_origen:
                raise ValueError("Los suplidores deben especificar el productor original del producto")
            if not self.precio_compra_productor:
                raise ValueError("Los suplidores deben especificar el precio de compra al productor")
            if self.precio_compra_productor >= self.price:
                raise ValueError("El precio de venta debe ser mayor al precio de compra al productor")
        
        super().save(*args, **kwargs)
    
    # ============================================================
    # CONFIGURACIÓN
    # ============================================================
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'