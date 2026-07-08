# apps/export/views.py
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone
from django.db.models import Count, Q
from django.http import HttpResponse

from apps.users.models import User
from apps.complaints.models import Complaint
from apps.utils.export_utils import (
    export_complaints_to_excel,
    export_complaints_to_pdf,
    export_productores_to_pdf
)


@login_required
@staff_member_required
def exportar_denuncias_excel(request):
    """Exportar denuncias a Excel con filtros opcionales"""
    complaints = Complaint.objects.select_related('complained_against').all()
    
    estado = request.GET.get('estado')
    fecha_desde = request.GET.get('fecha_desde')
    fecha_hasta = request.GET.get('fecha_hasta')
    productor_id = request.GET.get('productor_id')
    
    if estado and estado != '':
        complaints = complaints.filter(status=estado)
    if fecha_desde:
        complaints = complaints.filter(created_at__date__gte=fecha_desde)
    if fecha_hasta:
        complaints = complaints.filter(created_at__date__lte=fecha_hasta)
    if productor_id:
        complaints = complaints.filter(complained_against_id=productor_id)
    
    filename = f"denuncias_{timezone.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    return export_complaints_to_excel(complaints, filename)


@login_required
@staff_member_required
def exportar_denuncias_pdf(request):
    """Exportar denuncias a PDF con filtros opcionales"""
    complaints = Complaint.objects.select_related('complained_against').all()
    
    estado = request.GET.get('estado')
    if estado and estado != '':
        complaints = complaints.filter(status=estado)
    
    filename = f"denuncias_{timezone.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    return export_complaints_to_pdf(complaints, filename)


@login_required
@staff_member_required
def exportar_productores_pdf(request):
    """Exportar lista de productores a PDF con sus denuncias"""
    # ========== CORRECCIÓN: Obtener todos los productores (aprobados y pendientes) ==========
    productores = User.objects.filter(
        Q(role='productor') | Q(role='PRODUCTOR')
    ).order_by('username')
    
    # ========== CORRECCIÓN: Contar denuncias recibidas ==========
    productores = productores.annotate(
        denuncias_count=Count('complaints_received', distinct=True),
        denuncias_pendientes=Count('complaints_received', filter=Q(complaints_received__status='pending'), distinct=True),
        denuncias_aprobadas=Count('complaints_received', filter=Q(complaints_received__status='approved'), distinct=True),
        denuncias_rechazadas=Count('complaints_received', filter=Q(complaints_received__status='rejected'), distinct=True),
    )
    
    # ========== CORRECCIÓN: Verificar que haya datos ==========
    if not productores.exists():
        return HttpResponse("No hay productores registrados para exportar.", status=404)
    
    filename = f"productores_{timezone.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    return export_productores_to_pdf(productores, filename)


@login_required
@staff_member_required
def panel_exportaciones(request):
    """Panel de exportaciones para ONPECO"""
    # ========== CORRECCIÓN: Obtener productores aprobados ==========
    productores_aprobados = User.objects.filter(
        Q(role='productor') | Q(role='PRODUCTOR'),
        is_approved=True
    ).order_by('username')
    
    # ========== CORRECCIÓN: Contar todos los productores ==========
    total_productores = User.objects.filter(
        Q(role='productor') | Q(role='PRODUCTOR')
    ).count()
    
    context = {
        'estados_denuncia': Complaint.STATUS_CHOICES,
        'productores': productores_aprobados,
        'total_denuncias': Complaint.objects.count(),
        'total_productores': total_productores,
    }
    return render(request, 'export/panel_exportaciones.html', context)