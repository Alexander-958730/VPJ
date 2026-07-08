from django import template

register = template.Library()

@register.filter
def format_rd(value):
    """Formatea un número con el formato de República Dominicana: miles con coma, decimales con punto"""
    try:
        # Convertir a float
        value = float(value)
        # Formatear con 2 decimales
        formatted = f"{value:,.2f}"
        return formatted
    except (ValueError, TypeError):
        return "0.00"