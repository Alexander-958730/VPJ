"""
APPS.COMPLAINTS.ADMIN
=====================
Configuración del panel de administración de Django para la app complaints.

Este módulo contiene las configuraciones de admin para:
- Complaint (Denuncias): Gestión y visualización en el admin
- ComplaintUpdate (Actualizaciones de denuncias): Historial de cambios

Características:
- Listado personalizado con campos clave
- Filtros por estado, prioridad y tipo
- Búsqueda por ticket, título y usuarios
- Gráfico de denuncias por mes integrado en el admin
- Inline para ver el historial de actualizaciones
"""

from django.contrib import admin
from django.db.models import Count
from django.db.models.functions import TruncMonth
from django.http import JsonResponse
from django.urls import path
from django.shortcuts import render
from .models import Complaint, ComplaintUpdate


# =============================================================================
# INLINE: ComplaintUpdateInline
# =============================================================================
# Propósito: Permite ver y gestionar el historial de actualizaciones de una
# denuncia directamente desde la página de detalle de la denuncia en el admin.
#
# Configuración:
#   - model: ComplaintUpdate
#   - extra: 1 (muestra 1 fila vacía para agregar nuevas actualizaciones)
#   - readonly_fields: ('created_at',) (la fecha de creación no es editable)
#
# Uso:
#   - Se muestra como tabla dentro de la página de edición de Complaint
# =============================================================================
class ComplaintUpdateInline(admin.TabularInline):
    """Inline para mostrar el historial de actualizaciones de una denuncia"""
    model = ComplaintUpdate
    extra = 1
    readonly_fields = ('created_at',)


# =============================================================================
# ADMIN: ComplaintAdmin
# =============================================================================
# Propósito: Configuración del panel de administración para el modelo Complaint.
#
# Configuración:
#   - list_display: Columnas mostradas en la lista de denuncias
#   - list_filter: Filtros laterales
#   - search_fields: Campos de búsqueda
#   - readonly_fields: Campos de solo lectura
#   - inlines: Inline para ComplaintUpdate
#
# URLs personalizadas:
#   - /admin/complaints/complaint/grafico-denuncias/ → Vista del gráfico
#   - /admin/complaints/complaint/datos-denuncias/ → API para datos del gráfico
#
# Métodos:
#   - get_urls(): Agrega URLs personalizadas para el gráfico
#   - grafico_view(): Renderiza el template del gráfico
#   - datos_grafico(): API interna que devuelve datos en JSON para Chart.js
# =============================================================================
class ComplaintAdmin(admin.ModelAdmin):
    """Configuración del admin para denuncias"""
    
    # ============================================================
    # CONFIGURACIÓN DE LISTADO
    # ============================================================
    list_display = (
        'ticket_number',
        'title',
        'complainant',
        'complained_against',
        'status',
        'priority',
        'created_at'
    )
    list_filter = ('status', 'priority', 'complaint_type')
    search_fields = (
        'ticket_number',
        'title',
        'complainant__username',
        'complained_against__username'
    )
    readonly_fields = ('ticket_number', 'created_at', 'updated_at')
    inlines = [ComplaintUpdateInline]
    
    # ============================================================
    # URLS PERSONALIZADAS
    # ============================================================
    def get_urls(self):
        """
        Agrega URLs personalizadas al admin de Complaint.
        - grafico-denuncias/: Vista para el gráfico de denuncias por mes
        - datos-denuncias/: API que devuelve datos JSON para Chart.js
        """
        urls = super().get_urls()
        custom_urls = [
            path(
                'grafico-denuncias/',
                self.admin_site.admin_view(self.grafico_view),
                name='complaints_grafico'
            ),
            path(
                'datos-denuncias/',
                self.admin_site.admin_view(self.datos_grafico),
                name='complaints_data'
            ),
        ]
        return custom_urls + urls
    
    # ============================================================
    # VISTA DEL GRÁFICO
    # ============================================================
    def grafico_view(self, request):
        """
        Renderiza el template del gráfico de denuncias por mes.
        
        Parámetros:
            - request: Objeto HttpRequest
            
        Retorna:
            - HttpResponse: Renderiza 'admin/complaints/grafico.html'
            
        Contexto:
            - title: Título de la página
            - Otros contextos del admin (each_context)
        """
        context = dict(
            self.admin_site.each_context(request),
            title="Denuncias por Mes",
        )
        return render(request, "admin/complaints/grafico.html", context)
    
    # ============================================================
    # API PARA DATOS DEL GRÁFICO
    # ============================================================
    def datos_grafico(self, request):
        """
        API interna que devuelve los datos en JSON para Chart.js.
        
        Parámetros:
            - request: Objeto HttpRequest
            
        Retorna:
            - JsonResponse: Datos para tres gráficos:
                1. Denuncias por mes (línea/barra)
                2. Denuncias por estado (pastel)
                3. Denuncias por prioridad (pastel)
                
        Estructura de respuesta:
            {
                'labels': ['Ene 2026', 'Feb 2026', ...],
                'datasets': [{
                    'label': 'Denuncias por Mes',
                    'data': [5, 8, 12, ...],
                    'backgroundColor': 'rgba(54, 162, 235, 0.5)',
                    'borderColor': 'rgba(54, 162, 235, 1)',
                    'borderWidth': 2,
                    'tension': 0.3,
                    'fill': True
                }],
                'status_labels': ['pending', 'investigating', ...],
                'status_counts': [10, 5, ...],
                'priority_labels': ['low', 'medium', 'high'],
                'priority_counts': [3, 7, 5]
            }
        """
        # ============================================================
        # 1. DENUNCIAS POR MES
        # ============================================================
        data = (
            Complaint.objects
            .annotate(month=TruncMonth('created_at'))
            .values('month')
            .annotate(count=Count('id'))
            .order_by('month')
        )
        
        labels = [item['month'].strftime("%b %Y") for item in data if item['month']]
        counts = [item['count'] for item in data if item['month']]
        
        # ============================================================
        # 2. DENUNCIAS POR ESTADO
        # ============================================================
        status_data = (
            Complaint.objects
            .values('status')
            .annotate(count=Count('id'))
        )
        
        status_labels = [item['status'] for item in status_data]
        status_counts = [item['count'] for item in status_data]
        
        # ============================================================
        # 3. DENUNCIAS POR PRIORIDAD
        # ============================================================
        priority_data = (
            Complaint.objects
            .values('priority')
            .annotate(count=Count('id'))
        )
        
        priority_labels = [item['priority'] for item in priority_data if item['priority']]
        priority_counts = [item['count'] for item in priority_data if item['priority']]
        
        return JsonResponse({
            'labels': labels,
            'datasets': [{
                'label': 'Denuncias por Mes',
                'data': counts,
                'backgroundColor': 'rgba(54, 162, 235, 0.5)',
                'borderColor': 'rgba(54, 162, 235, 1)',
                'borderWidth': 2,
                'tension': 0.3,
                'fill': True
            }],
            'status_labels': status_labels,
            'status_counts': status_counts,
            'priority_labels': priority_labels,
            'priority_counts': priority_counts
        })


# ============================================================
# REGISTRO EN EL ADMIN
# ============================================================
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(ComplaintUpdate)