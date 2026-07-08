from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order

@receiver(post_save, sender=Order)
def actualizar_stock_al_completar(sender, instance, created, **kwargs):
    """
    Cuando un pedido se marca como 'delivered' (Entregado - Pago realizado),
    actualiza automáticamente el stock de los productos.
    """
    # Solo ejecutar si el pedido está en estado 'delivered'
    if instance.status == 'delivered':
        instance.actualizar_stock()