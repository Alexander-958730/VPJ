from django.contrib import admin
from .models import BackupHistory

@admin.register(BackupHistory)
class BackupHistoryAdmin(admin.ModelAdmin):
    list_display = ('filename', 'size', 'created_at', 'backup_type')
    list_filter = ('backup_type', 'created_at')
    search_fields = ('filename',)
    readonly_fields = ('filename', 'size', 'created_at', 'backup_type')
    
    def has_add_permission(self, request):
        return False