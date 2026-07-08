from django.apps import AppConfig

class BackupsManagerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.backups_manager'  # ← Cambiar a ruta completa
    verbose_name = 'Gestión de Backups'