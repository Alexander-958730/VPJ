"""
Filtros personalizados para templates de la app marketplace
"""
from django import template

register = template.Library()

@register.filter
def stars(rating):
    """
    Convierte una calificación numérica (0-5) en HTML de estrellas.
    
    Args:
        rating: Número (float o int) entre 0 y 5
    
    Returns:
        str: HTML con estrellas llenas y vacías
    """
    if rating is None:
        rating = 0
    
    # Redondear al entero más cercano
    try:
        rating_int = int(round(float(rating)))
    except (ValueError, TypeError):
        rating_int = 0
    
    # Asegurar que esté entre 0 y 5
    rating_int = max(0, min(5, rating_int))
    
    stars_html = ''
    for i in range(1, 6):
        if i <= rating_int:
            stars_html += '<i class="fas fa-star text-warning"></i>'
        else:
            stars_html += '<i class="far fa-star text-warning"></i>'
    
    return stars_html


@register.filter
def stars_with_number(rating):
    """
    Convierte una calificación numérica (0-5) en HTML de estrellas + número.
    
    Args:
        rating: Número (float o int) entre 0 y 5
    
    Returns:
        str: HTML con estrellas y el número
    """
    if rating is None:
        rating = 0
    
    # Redondear al entero más cercano
    try:
        rating_int = int(round(float(rating)))
        rating_float = float(rating)
    except (ValueError, TypeError):
        rating_int = 0
        rating_float = 0
    
    # Asegurar que esté entre 0 y 5
    rating_int = max(0, min(5, rating_int))
    rating_float = max(0, min(5, rating_float))
    
    stars_html = ''
    for i in range(1, 6):
        if i <= rating_int:
            stars_html += '<i class="fas fa-star text-warning"></i>'
        else:
            stars_html += '<i class="far fa-star text-warning"></i>'
    
    return f'{stars_html} <span class="ms-1">{rating_float:.1f}</span>'