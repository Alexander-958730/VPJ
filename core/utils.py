"""
CORE.UTILS
==========
Utilidades generales para el proyecto VPJ.

Este módulo contiene funciones auxiliares reutilizables en toda la aplicación.
Las funciones aquí definidas son de uso transversal y no dependen de una app específica.

Funciones:
    - obtener_fechas(): Obtiene y valida fechas desde la solicitud GET
"""

import datetime
from django.utils import timezone


# =============================================================================
# FUNCIÓN: obtener_fechas
# =============================================================================
# Propósito: Obtiene las fechas de inicio y fin desde los parámetros GET
# de la solicitud. Si no se proporcionan, usa el mes actual.
#
# Parámetros:
#   - request: Objeto HttpRequest con parámetros GET 'fecha_inicio' y 'fecha_fin'
#
# Retorna:
#   - tuple: (fecha_inicio, fecha_fin) como objetos date
#
# Uso:
#   - Reportes de ventas (apps/complaints/views.py)
#   - Exportaciones a Excel (apps/complaints/views.py)
#   - Cualquier vista que requiera filtro por fechas
#
# Formato esperado:
#   - GET: ?fecha_inicio=2026-05-01&fecha_fin=2026-07-05
#
# Comportamiento:
#   1. Si no hay fechas → primer día del mes actual hasta hoy
#   2. Si hay fechas válidas → las convierte a objetos date
#   3. Si las fechas no son válidas → usa el mes actual
#
# Ejemplo de uso:
#   ```python
#   from core.utils import obtener_fechas
#   
#   def mi_vista(request):
#       fecha_inicio, fecha_fin = obtener_fechas(request)
#       # Usar fecha_inicio y fecha_fin para filtrar consultas
#       pedidos = Pedido.objects.filter(
#           created_at__date__gte=fecha_inicio,
#           created_at__date__lte=fecha_fin
#       )
#   ```
# =============================================================================
def obtener_fechas(request):
    """
    Obtiene las fechas de inicio y fin desde la solicitud GET.
    Si no se proporcionan, usa el mes actual.
    
    Args:
        request: Objeto HttpRequest con parámetros GET 'fecha_inicio' y 'fecha_fin'
    
    Returns:
        tuple: (fecha_inicio, fecha_fin) como objetos date
    """
    # ============================================================
    # 1. OBTENER PARÁMETROS GET
    # ============================================================
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')
    
    # ============================================================
    # 2. PROCESAR FECHAS
    # ============================================================
    
    # Si no hay fechas, usar el mes actual
    if not fecha_inicio or not fecha_fin:
        hoy = timezone.now().date()
        fecha_inicio = hoy.replace(day=1)
        fecha_fin = hoy
    else:
        try:
            # Intentar convertir las fechas al formato YYYY-MM-DD
            fecha_inicio = datetime.datetime.strptime(fecha_inicio, '%Y-%m-%d').date()
            fecha_fin = datetime.datetime.strptime(fecha_fin, '%Y-%m-%d').date()
        except ValueError:
            # Si el formato no es válido, usar el mes actual
            hoy = timezone.now().date()
            fecha_inicio = hoy.replace(day=1)
            fecha_fin = hoy
    
    # ============================================================
    # 3. RETORNAR FECHAS
    # ============================================================
    return fecha_inicio, fecha_fin