import os
from datetime import datetime
from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Crea un backup diario del sistema (sobrescribe el anterior si existe)'

    def handle(self, *args, **options):
        fecha = datetime.now().strftime('%Y-%m-%d')
        self.stdout.write(f'📦 Iniciando backup diario: {fecha}')
        
        try:
            # Backup de la base de datos
            call_command('dbbackup', '--clean', '-z')
            self.stdout.write(self.style.SUCCESS('✅ Backup de base de datos completado'))
            
            # Backup de archivos media
            call_command('mediabackup', '-z')
            self.stdout.write(self.style.SUCCESS('✅ Backup de archivos media completado'))
            
            # Registrar el backup en la base de datos (para el historial)
            from apps.complaints.models import BackupHistory  # Lo crearemos después
            BackupHistory.objects.create(
                fecha=fecha,
                tipo='automatico',
                estado='exitoso'
            )
            
            self.stdout.write(self.style.SUCCESS(f'🎉 Backup diario completado: {fecha}'))
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'❌ Error en backup: {str(e)}'))
            BackupHistory.objects.create(
                fecha=fecha,
                tipo='automatico',
                estado='fallido',
                error=str(e)
            )