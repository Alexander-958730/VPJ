"""
APPS.USERS.MODELS
=================
Modelo de usuario personalizado para el sistema VPJ - Venta Precio Justo.

Este módulo extiende el modelo AbstractUser de Django para agregar
campos y funcionalidades específicas del negocio:
- Roles de usuario (productor, consumidor, suplidor, regulador, acopio)
- Reputación de productores
- Gestión de contraseñas temporales
- Productos en común (validación para compras entre productores)

Relaciones:
    - User → Product (vendedor): Un usuario puede vender múltiples productos
    - User → Reputacion: Historial de reputaciones asignadas por ONPECO
    - User → Complaint (complainant): Denuncias realizadas
    - User → Complaint (complained_against): Denuncias recibidas
"""

from django.db import models
from django.contrib.auth.models import AbstractUser


# =============================================================================
# MODELO: User (Personalizado)
# =============================================================================
# Propósito: Extiende el modelo AbstractUser de Django para agregar campos
# específicos del dominio de VPJ.
#
# Campos base de AbstractUser (heredados):
#   - username: Cédula del usuario (se usa como identificador único)
#   - first_name: Nombre real del usuario
#   - last_name: Apellido real del usuario
#   - email: Correo electrónico
#   - password: Contraseña (almacenada de forma segura)
#   - is_staff: Acceso al admin de Django
#   - is_active: Cuenta activa
#   - date_joined: Fecha de registro
#   - last_login: Último inicio de sesión
#
# Campos adicionales:
#   - role: Rol del usuario (productor, consumidor, suplidor, regulador, acopio)
#   - phone: Número de teléfono
#   - address: Dirección física
#   - business_name: Nombre del negocio (para productores/suplidores)
#   - is_approved: Aprobado por ONPECO (para productores/suplidores)
#   - is_profile_public: Privacidad del perfil público
#   - reputacion_actual: Nivel de reputación actual
#   - must_change_password: Indica si debe cambiar contraseña temporal
#
# Roles de usuario:
#   - productor: Agricultor que vende productos
#   - consumidor: Comprador final
#   - suplidor: Intermediario (desactivado)
#   - regulador: ONPECO (supervisor del sistema)
#   - acopio: Centro de Acopio (gestión de pedidos y pagos)
#
# Niveles de reputación:
#   - excelente: 🌟 Productor ejemplar
#   - bueno: 👍 Cumple con lo pactado
#   - regular: ⚠️ Presenta quejas ocasionales
#   - malo: 👎 Múltiples quejas justificadas
#   - critico: 🚨 Riesgo para consumidores
#
# Métodos principales:
#   - get_full_name(): Retorna el nombre completo del usuario
#   - get_display_name(): Retorna nombre + cédula para mostrar en interfaz
#   - get_reputacion_display(): Retorna el texto del nivel de reputación
#   - tiene_productos_comunes_con(): Verifica si comparte productos con otro usuario
#   - productos_que_vende: Propiedad que lista los productos del usuario
# =============================================================================
class User(AbstractUser):
    """
    Modelo de usuario personalizado para VPJ - Venta Precio Justo
    """
    
    # ============================================================
    # ROLES DE USUARIO
    # ============================================================
    ROLES = (
        ('productor', 'Productor'),
        ('consumidor', 'Consumidor'),
        ('suplidor', 'Suplidor'),
        ('regulador', 'Regulador'),
        ('acopio', 'Centro de Acopio'),
    )
    
    # ============================================================
    # NIVELES DE REPUTACIÓN (Solo para productores y suplidores)
    # ============================================================
    NIVELES_REPUTACION = (
        ('excelente', '🌟 Excelente - Productor ejemplar'),
        ('bueno', '👍 Bueno - Cumple con lo pactado'),
        ('regular', '⚠️ Regular - Presenta quejas ocasionales'),
        ('malo', '👎 Malo - Múltiples quejas justificadas'),
        ('critico', '🚨 Crítico - Riesgo para consumidores'),
    )
    
    # ============================================================
    # CAMPOS ADICIONALES
    # ============================================================
    
    # Rol del usuario en el sistema
    role = models.CharField(
        max_length=20,
        choices=ROLES,
        default='consumidor',
        help_text="Rol del usuario en el sistema VPJ"
    )
    
    # Datos de contacto
    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        help_text="Número de teléfono del usuario"
    )
    address = models.TextField(
        blank=True,
        null=True,
        help_text="Dirección física del usuario o negocio"
    )
    
    # Datos del negocio (para productores y suplidores)
    business_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Nombre del negocio o finca (para productores/suplidores)"
    )
    
    # Aprobación por ONPECO
    is_approved = models.BooleanField(
        default=False,
        help_text="Indica si el productor/suplidor ha sido aprobado por ONPECO"
    )
    
    # Privacidad del perfil público
    is_profile_public = models.BooleanField(
        default=True,
        help_text="Si es True, el perfil público es visible para todos. Si es False, solo el productor y ONPECO pueden verlo."
    )
    
    # Reputación actual (última asignada por ONPECO)
    reputacion_actual = models.CharField(
        max_length=20,
        choices=NIVELES_REPUTACION,
        default='bueno',
        blank=True,
        null=True,
        help_text="Nivel de reputación asignado por ONPECO"
    )
    
    # Contraseña temporal (cuando ONPECO la restablece)
    must_change_password = models.BooleanField(
        default=False,
        help_text="Indica si el usuario debe cambiar su contraseña al iniciar sesión (contraseña temporal)"
    )
    
    # ============================================================
    # MÉTODOS
    # ============================================================
    
    def __str__(self):
        """Representación legible del objeto"""
        return f"{self.username} - {self.get_role_display()}"
    
    # ============================================================
    # REPUTACIÓN
    # ============================================================
    
    def get_reputacion_display(self):
        """
        Retorna el texto completo del nivel de reputación actual.
        Ejemplo: "🌟 Excelente - Productor ejemplar"
        """
        if self.reputacion_actual:
            for nivel_valor, nivel_nombre in self.NIVELES_REPUTACION:
                if nivel_valor == self.reputacion_actual:
                    return nivel_nombre
        return "Sin reputación asignada"
    
    # ============================================================
    # NOMBRE COMPLETO
    # ============================================================
    
    def get_full_name(self):
        """
        Retorna el nombre completo del usuario.
        Prioriza: first_name + last_name > first_name > last_name > username
        """
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name
        return self.username  # Si no tiene nombre, muestra la cédula
    
    def get_display_name(self):
        """
        Retorna el nombre para mostrar en la interfaz.
        Formato: "Nombre (Cédula)" si tiene nombre, o solo "Cédula"
        """
        nombre = self.get_full_name()
        if nombre != self.username:
            return f"{nombre} ({self.username})"
        return self.username
    
    # ============================================================
    # PRODUCTOS EN COMÚN
    # ============================================================
    
    def tiene_productos_comunes_con(self, otro_usuario):
        """
        Verifica si este usuario tiene AL MENOS UN producto en común con otro usuario.
        
        Retorna:
            - True: Si comparten al menos un producto (no son compatibles para comprar)
            - False: Si no comparten ningún producto (son compatibles para comprar)
        
        Uso:
            - Validar que productores no compren productos de su misma subcategoría
            - Bloquear compras entre productores que venden los mismos productos
        """
        # Solo aplica para productores y suplidores
        if self.role not in ['productor', 'suplidor'] or otro_usuario.role not in ['productor', 'suplidor']:
            return False
        
        # Obtener nombres de productos que vende cada uno
        mis_productos = set(self.productos_que_vende)
        sus_productos = set(otro_usuario.productos_que_vende)
        
        # Si hay intersección (al menos un producto en común), no son compatibles
        return len(mis_productos.intersection(sus_productos)) > 0
    
    @property
    def productos_que_vende(self):
        """
        Propiedad que retorna una lista de los nombres de productos que vende este usuario.
        
        Uso:
            - Validación de productos en común
            - Mostrar productos del productor en su perfil
            - Filtrar pedidos del productor
        """
        if self.role in ['productor', 'suplidor']:
            return list(self.products.values_list('name', flat=True))
        return []