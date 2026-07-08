"""
APPS.REVIEWS.VIEWS
==================
Vistas para el sistema de reseñas y calificaciones de productores.

Este módulo contiene las vistas relacionadas con:
- Calificación de productores por parte de consumidores
- Actualización de calificaciones existentes
- Visualización de reseñas en perfiles públicos

Roles de usuario:
- consumidor: Puede calificar y comentar sobre productores
- productor: Recibe calificaciones (no puede calificar)
- regulador (ONPECO): Supervisa calificaciones
- acopio (Centro de Acopio): No tiene acceso a esta función
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from apps.users.models import User
from .models import Review
from .forms import ReviewForm


# =============================================================================
# FUNCIÓN: calificar_productor
# =============================================================================
# Propósito: Permite a un consumidor calificar a un productor.
# Si ya existe una calificación anterior, permite actualizarla.
#
# Parámetros:
#   - request: Objeto HttpRequest (GET, POST)
#   - productor_id: ID del productor a calificar
#
# Retorna:
#   - GET: Renderiza 'reviews/calificar_productor.html' con el formulario
#   - POST: Valida, guarda/actualiza la calificación y redirige al perfil
#
# URLs asociadas:
#   - /reviews/calificar/<productor_id>/
#
# Roles permitidos:
#   - ✅ Consumidor (puede calificar)
#   - ❌ Productor (no puede calificar a otros productores)
#   - ❌ Regulador
#   - ❌ Centro de Acopio
#
# Validaciones:
#   1. Solo consumidores pueden calificar
#   2. El productor debe estar aprobado (is_approved=True)
#   3. La calificación debe ser entre 1 y 5 estrellas
#
# Flujo de trabajo:
#   1. Verificar que el usuario sea consumidor
#   2. Verificar que el productor exista y esté aprobado
#   3. Buscar si ya existe una calificación previa
#   4. Si es POST: guardar o actualizar la calificación
#   5. Si es GET: mostrar formulario con datos existentes (si los hay)
# =============================================================================
@login_required
def calificar_productor(request, productor_id):
    """
    Vista para que un consumidor califique a un productor
    """
    # ============================================================
    # 1. VERIFICAR QUE EL USUARIO SEA CONSUMIDOR
    # ============================================================
    if request.user.role != 'consumidor':
        messages.error(request, '❌ Solo los consumidores pueden calificar productores.')
        return redirect('users:perfil_publico_productor', productor_id)
    
    # ============================================================
    # 2. OBTENER EL PRODUCTOR
    # ============================================================
    productor = get_object_or_404(
        User,
        id=productor_id,
        role='productor',
        is_approved=True
    )
    
    # ============================================================
    # 3. VERIFICAR SI YA EXISTE UNA CALIFICACIÓN
    # ============================================================
    review_existente = Review.objects.filter(
        productor=productor,
        consumidor=request.user
    ).first()
    
    # ============================================================
    # 4. PROCESAR POST (GUARDAR O ACTUALIZAR)
    # ============================================================
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            if review_existente:
                # Actualizar calificación existente
                review_existente.rating = form.cleaned_data['rating']
                review_existente.comment = form.cleaned_data['comment']
                review_existente.save()
                messages.success(request, '✅ Tu calificación ha sido actualizada.')
            else:
                # Crear nueva calificación
                review = form.save(commit=False)
                review.productor = productor
                review.consumidor = request.user
                review.save()
                messages.success(request, '✅ ¡Gracias por calificar a este productor!')
            return redirect('users:perfil_publico_productor', productor_id)
    else:
        # ============================================================
        # 5. GET: MOSTRAR FORMULARIO CON DATOS EXISTENTES
        # ============================================================
        form = ReviewForm(initial={
            'rating': review_existente.rating if review_existente else None,
            'comment': review_existente.comment if review_existente else ''
        })
    
    context = {
        'productor': productor,
        'form': form,
        'review_existente': review_existente,
    }
    return render(request, 'reviews/calificar_productor.html', context)