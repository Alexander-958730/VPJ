from django.db import models

class BackupHistory(models.Model):
    """Historial de backups del sistema"""
    filename = models.CharField(max_length=255)
    size = models.FloatField(help_text="Tamaño en KB")
    created_at = models.DateTimeField(auto_now_add=True)
    backup_type = models.CharField(max_length=20, choices=[
        ('auto', 'Automático'),
        ('manual', 'Manual'),
    ], default='manual')
    
    def __str__(self):
        return f"{self.filename} - {self.created_at}"
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Backup"
        verbose_name_plural = "Historial de Backups"