from django.apps import AppConfig

class CartConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.cart'
    verbose_name = 'Carrito de Compras'
    
    def ready(self):
        """
        Registra las señales cuando la aplicación está lista.
        """
        import apps.cart.signals