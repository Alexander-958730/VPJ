from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.conf import settings
from datetime import datetime
import os
import glob

class Command(BaseCommand):
    help = 'Realiza backup automático de la base de datos y archivos media'

    def handle(self, *args, **kwargs):
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        # 1. Backup de base de datos
        backup_name = f'backup_auto_{timestamp}.json'
        backup_path = os.path.join('backups', backup_name)
        
        self.stdout.write(f'🔄 Creando backup de BD: {backup_path}')
        
        # Asegurar que la carpeta backups existe
        os.makedirs('backups', exist_ok=True)
        
        with open(backup_path, 'w', encoding='utf-8') as f:
            call_command('dumpdata', stdout=f)
        
        self.stdout.write(self.style.SUCCESS(f'✅ Backup BD creado: {backup_name}'))
        
        # 2. Backup de archivos media (opcional)
        media_backup = f'backup_media_{timestamp}.zip'
        media_backup_path = os.path.join('backups', media_backup)
        
        if os.path.exists('media'):
            self.stdout.write(f'📁 Creando backup de archivos media...')
            import zipfile
            import shutil
            
            with zipfile.ZipFile(media_backup_path, 'w') as zipf:
                for root, dirs, files in os.walk('media'):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, 'media')
                        zipf.write(file_path, arcname)
            
            self.stdout.write(self.style.SUCCESS(f'✅ Backup media creado: {media_backup}'))
        
        # 3. Limpiar backups antiguos (mantener últimos 10)
        backup_files = sorted(glob.glob('backups/backup_auto_*.json'))
        if len(backup_files) > 10:
            for old_file in backup_files[:-10]:
                os.remove(old_file)
                self.stdout.write(f'🗑️ Backup antiguo eliminado: {os.path.basename(old_file)}')
        
        # 4. Registrar en log
        log_entry = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Backup completado: {backup_name}\n"
        with open('backup_log.txt', 'a') as log_file:
            log_file.write(log_entry)
        
        self.stdout.write(self.style.SUCCESS('✅ Backup automático completado'))