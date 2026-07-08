"""
APPS.COMPLAINTS.MODELS
======================
Modelos de datos para el sistema de denuncias y gestión de ONPECO.

Este módulo contiene los modelos que gestionan:
- Denuncias (Complaint): Reportes de consumidores sobre productores
- Seguimiento de denuncias (ComplaintUpdate): Historial de cambios de estado
- Historial de backups (BackupHistory): Registro de puntos de restauración
- Reputación (Reputacion): Nivel de confianza de productores/suplidores

Relaciones:
    - Complaint → User (complainant, complained_against)
    - ComplaintUpdate → Complaint (historial)
    - Reputacion → User (productor)
    - BackupHistory → User (creado_por)
"""

from django.db import models
from django.conf import settings


# =============================================================================
# MODELO: Complaint
# =============================================================================
# Propósito: Almacena las denuncias realizadas por consumidores contra
# productores o suplidores.
#
# Campos principales:
#   - complainant: Usuario que realiza la denuncia
#   - complained_against: Usuario denunciado (productor/suplidor)
#   - producto: Producto específico relacionado con la denuncia (opcional)
#   - ticket_number: Código único de seguimiento (ej: CD-000001)
#   - title: Título breve de la denuncia
#   - complaint_type: Tipo de denuncia (precio, calidad, entrega, otro)
#   - description: Descripción detallada
#   - status: Estado actual (pending, investigating, resolved, rejected)
#   - priority: Prioridad (low, medium, high)
#   - created_at: Fecha de creación
#   - updated_at: Fecha de última actualización
#
# Estados del sistema:
#   - pending: Pendiente de revisión por ONPECO
#   - investigating: En investigación activa
#   - resolved: Resuelta (caso cerrado)
#   - rejected: Rechazada (sin fundamento)
#
# Tipos de denuncia:
#   - price: Precio abusivo
#   - quality: Calidad del producto
#   - delivery: Problema con entrega
#   - other: Otro tipo de problema
#
# Generación de ticket:
#   - Se genera automáticamente al guardar si no existe
#   - Formato: CD-XXXXXX (ej: CD-000001, CD-000002)
#
# Métodos:
#   - save(): Genera ticket_number automáticamente
#   - __str__(): Representación legible del objeto
# =============================================================================
class Complaint(models.Model):
    """
    Modelo de denuncias con sistema de seguimiento
    """
    
    # ============================================================
    # ESTADOS DE LA DENUNCIA
    # ============================================================
    STATUS_CHOICES = (
        ('pending', 'Pendiente'),
        ('investigating', 'En investigación'),
        ('resolved', 'Resuelto'),
        ('rejected', 'Rechazado'),
    )
    
    # ============================================================
    # PRIORIDADES
    # ============================================================
    PRIORITY_CHOICES = (
        ('low', 'Baja'),
        ('medium', 'Media'),
        ('high', 'Alta'),
    )
    
    # ============================================================
    # TIPOS DE DENUNCIA
    # ============================================================
    TYPE_CHOICES = (
        ('price', 'Precio abusivo'),
        ('quality', 'Calidad del producto'),
        ('delivery', 'Problema con entrega'),
        ('other', 'Otro'),
    )
    
    # ============================================================
    # RELACIONES
    # ============================================================
    # Usuario que realiza la denuncia (consumidor generalmente)
    complainant = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='complaints_made',
        help_text="Usuario que realiza la denuncia"
    )
    
    # Usuario denunciado (productor o suplidor)
    complained_against = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='complaints_received',
        help_text="Usuario denunciado (productor o suplidor)"
    )
    
    # Producto específico relacionado con la denuncia (opcional)
    producto = models.ForeignKey(
        'marketplace.Product',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='denuncias',
        help_text="Producto relacionado con la denuncia (opcional)"
    )
    
    # ============================================================
    # DATOS DE LA DENUNCIA
    # ============================================================
    ticket_number = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
        help_text="Número de ticket único de seguimiento (ej: CD-000001)"
    )
    title = models.CharField(
        max_length=200,
        help_text="Título breve de la denuncia"
    )
    complaint_type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        default='other',
        help_text="Tipo de denuncia"
    )
    description = models.TextField(
        help_text="Descripción detallada de la denuncia"
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        help_text="Estado actual de la denuncia"
    )
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='medium',
        help_text="Nivel de prioridad de la denuncia"
    )
    
    # ============================================================
    # FECHAS
    # ============================================================
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Fecha y hora de creación de la denuncia"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Fecha y hora de la última actualización"
    )
    
    # ============================================================
    # MÉTODOS
    # ============================================================
    def save(self, *args, **kwargs):
        """
        Genera automáticamente el ticket_number si no existe.
        Formato: CD-000001, CD-000002, etc.
        """
        if not self.ticket_number:
            last_complaint = Complaint.objects.all().order_by('id').last()
            if last_complaint:
                new_id = last_complaint.id + 1
            else:
                new_id = 1
            self.ticket_number = f'CD-{new_id:06d}'
        super().save(*args, **kwargs)
    
    def __str__(self):
        """Representación legible del objeto"""
        return f"{self.ticket_number} - {self.title}"


# =============================================================================
# MODELO: ComplaintUpdate
# =============================================================================
# Propósito: Almacena el historial de cambios de estado de una denuncia.
# Permite auditar quién, cuándo y por qué se cambió el estado.
#
# Campos principales:
#   - complaint: Denuncia asociada
#   - comment: Comentario del cambio (justificación)
#   - old_status: Estado anterior
#   - new_status: Nuevo estado
#   - created_by: Usuario que realizó el cambio (ONPECO)
#   - created_at: Fecha del cambio
#
# Relaciones:
#   - Pertenece a una denuncia (Complaint)
#   - Creado por un usuario (User)
#
# Uso:
#   - ONPECO registra cada cambio de estado
#   - Los comentarios sirven como evidencia
#   - Historial visible en el detalle de la denuncia
# =============================================================================
class ComplaintUpdate(models.Model):
    """
    Historial de seguimiento de cada denuncia
    """
    
    # ============================================================
    # RELACIONES
    # ============================================================
    complaint = models.ForeignKey(
        Complaint,
        on_delete=models.CASCADE,
        related_name='updates',
        help_text="Denuncia asociada a esta actualización"
    )
    
    # ============================================================
    # DATOS DEL CAMBIO
    # ============================================================
    comment = models.TextField(
        help_text="Comentario o justificación del cambio de estado"
    )
    old_status = models.CharField(
        max_length=20,
        choices=Complaint.STATUS_CHOICES,
        help_text="Estado anterior de la denuncia"
    )
    new_status = models.CharField(
        max_length=20,
        choices=Complaint.STATUS_CHOICES,
        help_text="Nuevo estado asignado a la denuncia"
    )
    
    # ============================================================
    # QUIÉN Y CUÁNDO
    # ============================================================
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        help_text="Usuario de ONPECO que realizó el cambio"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Fecha y hora del cambio de estado"
    )
    
    def __str__(self):
        """Representación legible del objeto"""
        return f"Actualización de {self.complaint.ticket_number}"


# =============================================================================
# MODELO: BackupHistory
# =============================================================================
# Propósito: Registra todos los backups (puntos de restauración) realizados
# por ONPECO. Permite llevar un control de cuándo y por qué se crearon.
#
# Campos principales:
#   - fecha: Fecha y hora del backup
#   - tipo: Tipo de backup (automático, manual, previo a actualización)
#   - estado: Estado del proceso (exitoso, fallido, en proceso)
#   - error: Mensaje de error si falló
#   - descripcion: Descripción del motivo del backup
#   - nombre_archivo: Nombre del archivo generado
#
# Tipos de backup:
#   - automatico: 🤖 Diario automático
#   - manual: 👤 Punto de restauración manual
#   - previo_actualizacion: ⚠️ Antes de una actualización
#
# Estados:
#   - exitoso: ✅ Backup completado correctamente
#   - fallido: ❌ Error durante el proceso
#   - en_proceso: 🔄 Proceso en curso
#
# Uso:
#   - ONPECO puede ver el historial de backups
#   - Útil para auditoría y seguimiento
# =============================================================================
class BackupHistory(models.Model):
    """Registro de todos los backups realizados (puntos de restauración)"""
    
    # ============================================================
    # TIPOS DE BACKUP
    # ============================================================
    TIPOS = [
        ('automatico', '🤖 Automático diario'),
        ('manual', '👤 Punto de restauración manual'),
        ('previo_actualizacion', '⚠️ Previo a actualización'),
    ]
    
    # ============================================================
    # ESTADOS DEL BACKUP
    # ============================================================
    ESTADOS = [
        ('exitoso', '✅ Exitoso'),
        ('fallido', '❌ Fallido'),
        ('en_proceso', '🔄 En proceso'),
    ]
    
    # ============================================================
    # CAMPOS
    # ============================================================
    fecha = models.DateTimeField(
        auto_now_add=True,
        help_text="Fecha y hora en que se realizó el backup"
    )
    tipo = models.CharField(
        max_length=30,
        choices=TIPOS,
        help_text="Tipo de backup realizado"
    )
    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default='en_proceso',
        help_text="Estado actual del proceso de backup"
    )
    error = models.TextField(
        blank=True,
        null=True,
        help_text="Mensaje de error en caso de fallo"
    )
    descripcion = models.CharField(
        max_length=200,
        blank=True,
        help_text="Descripción del motivo del backup (ej: Antes de actualizar precios)"
    )
    nombre_archivo = models.CharField(
        max_length=200,
        blank=True,
        help_text="Nombre del archivo de backup generado"
    )
    
    # ============================================================
    # CONFIGURACIÓN
    # ============================================================
    class Meta:
        ordering = ['-fecha']
        verbose_name = 'Historial de Backup'
        verbose_name_plural = 'Historial de Backups'
    
    def __str__(self):
        """Representación legible del objeto"""
        return f"{self.fecha.strftime('%Y-%m-%d %H:%M')} - {self.get_tipo_display()}"


# =============================================================================
# MODELO: Reputacion
# =============================================================================
# Propósito: Gestiona la reputación de productores y suplidores.
# Solo ONPECO puede asignar y modificar la reputación.
#
# Campos principales:
#   - productor: Usuario productor/suplidor calificado
#   - nivel: Nivel de reputación asignado
#   - comentario: Justificación de ONPECO
#   - creado_por: Usuario de ONPECO que asignó
#   - created_at: Fecha de asignación
#   - updated_at: Fecha de última actualización
#
# Niveles de reputación:
#   - excelente: 🌟 Productor ejemplar
#   - bueno: 👍 Cumple con lo pactado
#   - regular: ⚠️ Presenta quejas ocasionales
#   - malo: 👎 Múltiples quejas justificadas
#   - critico: 🚨 Riesgo para consumidores
#
# Restricciones:
#   - Solo se puede asignar a productores (limit_choices_to)
#   - Solo ONPECO puede crear/modificar
#
# Uso:
#   - ONPECO asigna reputación desde el portal
#   - Los consumidores ven la reputación en los perfiles
#   - Influye en la confianza del productor
# =============================================================================
class Reputacion(models.Model):
    """
    Modelo para gestionar la reputación de productores y suplidores
    Solo ONPECO puede gestionar esto
    """
    
    # ============================================================
    # NIVELES DE REPUTACIÓN
    # ============================================================
    NIVELES_REPUTACION = (
        ('excelente', '🌟 Excelente - Productor ejemplar'),
        ('bueno', '👍 Bueno - Cumple con lo pactado'),
        ('regular', '⚠️ Regular - Presenta quejas ocasionales'),
        ('malo', '👎 Malo - Múltiples quejas justificadas'),
        ('critico', '🚨 Crítico - Riesgo para consumidores'),
    )
    
    # ============================================================
    # RELACIONES
    # ============================================================
    # Productor/suplidor calificado (solo usuarios con rol productor)
    productor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reputacion_registros',
        limit_choices_to={'role': 'productor'},
        help_text="Productor o suplidor al que se le asigna la reputación"
    )
    
    # ============================================================
    # DATOS DE LA REPUTACIÓN
    # ============================================================
    nivel = models.CharField(
        max_length=20,
        choices=NIVELES_REPUTACION,
        default='bueno',
        help_text="Nivel de reputación asignado por ONPECO"
    )
    comentario = models.TextField(
        help_text="Justificación detallada del nivel asignado por ONPECO"
    )
    
    # ============================================================
    # QUIÉN Y CUÁNDO
    # ============================================================
    creado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='reputaciones_asignadas',
        help_text="Usuario de ONPECO que asignó la reputación"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Fecha y hora de asignación de la reputación"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Fecha y hora de la última actualización de la reputación"
    )
    
    # ============================================================
    # CONFIGURACIÓN
    # ============================================================
    class Meta:
        verbose_name = 'Reputación'
        verbose_name_plural = 'Reputaciones'
        ordering = ['-created_at']
    
    def __str__(self):
        """Representación legible del objeto"""
        return f"{self.productor.business_name} - {self.get_nivel_display()}"