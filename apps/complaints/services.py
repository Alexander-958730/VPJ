"""
APPS.COMPLAINTS.SERVICES
========================
Servicios para la app complaints (ONPECO).

Este módulo contiene la lógica de negocio reutilizable para el cálculo
de estadísticas y métricas utilizadas en el portal ONPECO.

Beneficios de usar servicios:
- Centraliza la lógica de negocio en un solo lugar
- Reduce la duplicación de código en las vistas
- Facilita las pruebas unitarias
- Mejora la mantenibilidad del código

Roles de usuario:
- regulador (ONPECO): Usa estos servicios para obtener estadísticas
- No hay restricciones de acceso ya que es un servicio interno
"""

from django.db.models import Count, Q
from apps.marketplace.models import Product
from django.contrib.auth import get_user_model
from .models import Complaint

User = get_user_model()


# =============================================================================
# CLASE: EstadisticasONPECO
# =============================================================================
# Propósito: Servicio centralizado para obtener estadísticas del sistema
# para ONPECO. Contiene métodos estáticos que realizan consultas y cálculos.
#
# Métodos disponibles:
#   - get_resumen_general(): Estadísticas generales del sistema
#   - get_denuncias_por_estado(): Conteo de denuncias agrupadas por estado
#   - get_top_productores_denunciados(): Productores más denunciados
#   - get_estadisticas_usuarios(): Estadísticas detalladas de usuarios
#
# Uso en vistas:
#   from apps.complaints.services import EstadisticasONPECO
#   
#   stats = EstadisticasONPECO.get_resumen_general()
#   context = {
#       'total_denuncias': stats['total_denuncias'],
#       'total_productores': stats['total_productores'],
#   }
# =============================================================================
class EstadisticasONPECO:
    """
    Servicio para obtener estadísticas del sistema para ONPECO.
    Centraliza todos los conteos y cálculos en un solo lugar.
    """
    
    # ============================================================
    # MÉTODO: get_resumen_general
    # ============================================================
    # Propósito: Obtiene un resumen general de todas las estadísticas del sistema.
    # Es el método principal utilizado en el dashboard de ONPECO.
    #
    # Retorna:
    #   - dict: Diccionario con todas las estadísticas del sistema
    #
    # Métricas incluidas:
    #   - Denuncias: total, pendientes, investigando, aprobadas, rechazadas
    #   - Productos: total en el marketplace
    #   - Usuarios: total, productores, consumidores, suplidores, reguladores
    #   - Productores: aprobados vs pendientes
    #
    # Uso en portal_onpeco:
    #   stats = EstadisticasONPECO.get_resumen_general()
    # ============================================================
    @staticmethod
    def get_resumen_general():
        """
        Obtiene un resumen general de todas las estadísticas del sistema.
        
        Returns:
            dict: Diccionario con todas las estadísticas
        """
        return {
            # ============================================================
            # DENUNCIAS
            # ============================================================
            'total_denuncias': Complaint.objects.count(),
            'denuncias_pendientes': Complaint.objects.filter(status='pending').count(),
            'denuncias_investigando': Complaint.objects.filter(status='investigating').count(),
            'denuncias_aprobadas': Complaint.objects.filter(status='resolved').count(),
            'denuncias_rechazadas': Complaint.objects.filter(status='rejected').count(),
            
            # ============================================================
            # PRODUCTOS
            # ============================================================
            'total_productos': Product.objects.count(),
            
            # ============================================================
            # USUARIOS
            # ============================================================
            'total_usuarios': User.objects.count(),
            'total_productores': User.objects.filter(role='productor').count(),
            'total_consumidores': User.objects.filter(role='consumidor').count(),
            'total_suplidores': User.objects.filter(role='suplidor').count(),
            'total_reguladores': User.objects.filter(role='regulador').count(),
            
            # ============================================================
            # PRODUCTORES: APROBADOS VS PENDIENTES
            # ============================================================
            'productores_aprobados': User.objects.filter(role='productor', is_approved=True).count(),
            'productores_pendientes': User.objects.filter(role='productor', is_approved=False).count(),
        }
    
    # ============================================================
    # MÉTODO: get_denuncias_por_estado
    # ============================================================
    # Propósito: Obtiene el conteo de denuncias agrupadas por estado.
    # Útil para gráficos y reportes detallados.
    #
    # Retorna:
    #   - dict: Diccionario con {estado: cantidad}
    #
    # Estados posibles:
    #   - pending: Pendiente de revisión
    #   - investigating: En investigación
    #   - resolved: Resuelta
    #   - rejected: Rechazada
    # ============================================================
    @staticmethod
    def get_denuncias_por_estado():
        """
        Obtiene el conteo de denuncias agrupadas por estado.
        
        Returns:
            dict: Diccionario con {estado: cantidad}
        """
        return {
            'pending': Complaint.objects.filter(status='pending').count(),
            'investigating': Complaint.objects.filter(status='investigating').count(),
            'resolved': Complaint.objects.filter(status='resolved').count(),
            'rejected': Complaint.objects.filter(status='rejected').count(),
        }
    
    # ============================================================
    # MÉTODO: get_top_productores_denunciados
    # ============================================================
    # Propósito: Obtiene los productores más denunciados.
    # Retorna una lista de productores con el conteo de denuncias.
    #
    # Parámetros:
    #   - limite (int): Número máximo de productores a retornar (default: 10)
    #
    # Retorna:
    #   - list: Lista de productores con su conteo de denuncias
    #
    # Algoritmo:
    #   1. Agrupar denuncias por complained_against
    #   2. Ordenar de mayor a menor
    #   3. Obtener los N productores más denunciados
    #   4. Agregar el atributo 'total_denuncias' a cada objeto
    #
    # Uso en productores_mas_denunciados:
    #   productores = EstadisticasONPECO.get_top_productores_denunciados(limite=20)
    # ============================================================
    @staticmethod
    def get_top_productores_denunciados(limite=10):
        """
        Obtiene los productores más denunciados.
        
        Args:
            limite (int): Número máximo de productores a retornar
            
        Returns:
            list: Lista de productores con su conteo de denuncias
        """
        from collections import defaultdict
        
        # ============================================================
        # 1. CONTAR DENUNCIAS POR PRODUCTOR
        # ============================================================
        denuncias_por_productor = defaultdict(int)
        denuncias = Complaint.objects.filter(complained_against__isnull=False)
        
        for denuncia in denuncias:
            if denuncia.complained_against:
                user_id = denuncia.complained_against.id
                denuncias_por_productor[user_id] += 1
        
        # ============================================================
        # 2. ORDENAR Y OBTENER LOS MÁS DENUNCIADOS
        # ============================================================
        productores_ids = sorted(
            denuncias_por_productor.keys(),
            key=lambda x: denuncias_por_productor[x],
            reverse=True
        )[:limite]
        
        productores = User.objects.filter(id__in=productores_ids, role='productor')
        
        # ============================================================
        # 3. AGREGAR CONTEO A CADA OBJETO
        # ============================================================
        for productor in productores:
            productor.total_denuncias = denuncias_por_productor.get(productor.id, 0)
        
        return sorted(productores, key=lambda x: x.total_denuncias, reverse=True)
    
    # ============================================================
    # MÉTODO: get_estadisticas_usuarios
    # ============================================================
    # Propósito: Obtiene estadísticas detalladas de usuarios.
    # Útil para reportes y análisis de crecimiento.
    #
    # Retorna:
    #   - dict: Diccionario con estadísticas de usuarios
    #
    # Métricas incluidas:
    #   - total: Todos los usuarios
    #   - por_rol: Distribución por rol
    #   - activos: Usuarios activos
    #   - inactivos: Usuarios inactivos
    # ============================================================
    @staticmethod
    def get_estadisticas_usuarios():
        """
        Obtiene estadísticas detalladas de usuarios.
        
        Returns:
            dict: Diccionario con estadísticas de usuarios
        """
        return {
            'total': User.objects.count(),
            'por_rol': {
                'productor': User.objects.filter(role='productor').count(),
                'consumidor': User.objects.filter(role='consumidor').count(),
                'suplidor': User.objects.filter(role='suplidor').count(),
                'regulador': User.objects.filter(role='regulador').count(),
                'acopio': User.objects.filter(role='acopio').count(),
            },
            'activos': User.objects.filter(is_active=True).count(),
            'inactivos': User.objects.filter(is_active=False).count(),
        }