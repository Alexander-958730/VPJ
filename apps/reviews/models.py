"""
APPS.REVIEWS.MODELS
===================
Modelos de datos para el sistema de reseñas y calificaciones de productores.

Este módulo contiene el modelo que gestiona:
- Reseñas (Review): Calificaciones y comentarios de consumidores sobre productores

Relaciones:
    - Review → User (productor): Productor calificado
    - Review → User (consumidor): Consumidor que califica

Roles de usuario:
- consumidor: Puede crear reseñas sobre productores
- productor: Recibe reseñas de consumidores
- regulador (ONPECO): Puede moderar reseñas (is_approved)
"""

from django.db import models
from django.conf import settings


# =============================================================================
# MODELO: Review
# =============================================================================
# Propósito: Almacena las calificaciones y comentarios que los consumidores
# realizan sobre los productores. Cada consumidor puede calificar a un productor
# una sola vez (unique_together).
#
# Campos principales:
#   - productor: Usuario productor que recibe la calificación
#   - consumidor: Usuario consumidor que realiza la calificación
#   - rating: Calificación en estrellas (1-5)
#   - comment: Comentario o reseña escrita (opcional)
#   - created_at: Fecha de creación
#   - updated_at: Fecha de última actualización
#   - is_approved: Indica si la reseña está aprobada (moderación)
#
# Restricciones:
#   - Un consumidor solo puede calificar una vez a un productor
#   - unique_together: ['productor', 'consumidor']
#
# Relaciones:
#   - productor: Usuario calificado (ForeignKey con limit_choices_to)
#   - consumidor: Usuario que califica (ForeignKey con limit_choices_to)
#
# Calificaciones (rating):
#   - 1: ⭐ 1 estrella (Muy malo)
#   - 2: ⭐⭐ 2 estrellas (Malo)
#   - 3: ⭐⭐⭐ 3 estrellas (Regular)
#   - 4: ⭐⭐⭐⭐ 4 estrellas (Bueno)
#   - 5: ⭐⭐⭐⭐⭐ 5 estrellas (Excelente)
#
# Uso:
#   - Mostrar calificación promedio en perfiles de productores
#   - Listar reseñas en el perfil público
#   - Moderación de contenido por ONPECO (is_approved)
# =============================================================================
class Review(models.Model):
    """
    Modelo de calificación/reseña para productores
    """
    
    # ============================================================
    # OPCIONES DE CALIFICACIÓN
    # ============================================================
    RATING_CHOICES = [
        (1, '⭐ 1'),
        (2, '⭐⭐ 2'),
        (3, '⭐⭐⭐ 3'),
        (4, '⭐⭐⭐⭐ 4'),
        (5, '⭐⭐⭐⭐⭐ 5'),
    ]
    
    # ============================================================
    # RELACIONES
    # ============================================================
    # Productor calificado (solo usuarios con rol productor)
    productor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reviews_recibidas',
        limit_choices_to={'role': 'productor'},
        help_text="Productor que recibe la calificación"
    )
    
    # Consumidor que realiza la calificación (solo usuarios con rol consumidor)
    consumidor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reviews_hechas',
        limit_choices_to={'role': 'consumidor'},
        help_text="Consumidor que realiza la calificación"
    )
    
    # ============================================================
    # DATOS DE LA RESEÑA
    # ============================================================
    rating = models.IntegerField(
        choices=RATING_CHOICES,
        help_text="Calificación en estrellas (1-5)"
    )
    comment = models.TextField(
        blank=True,
        null=True,
        help_text="Comentario o reseña escrita (opcional)"
    )
    
    # ============================================================
    # FECHAS
    # ============================================================
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Fecha y hora de creación de la reseña"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Fecha y hora de última actualización"
    )
    
    # ============================================================
    # MODERACIÓN
    # ============================================================
    is_approved = models.BooleanField(
        default=True,
        help_text="Indica si la reseña está aprobada por ONPECO (moderación)"
    )
    
    # ============================================================
    # CONFIGURACIÓN
    # ============================================================
    class Meta:
        # Un consumidor solo puede calificar una vez por productor
        unique_together = ['productor', 'consumidor']
        ordering = ['-created_at']
        verbose_name = 'Reseña'
        verbose_name_plural = 'Reseñas'
    
    # ============================================================
    # MÉTODOS
    # ============================================================
    def __str__(self):
        """Representación legible del objeto"""
        return f"{self.consumidor.username} → {self.productor.business_name}: {self.rating}★"