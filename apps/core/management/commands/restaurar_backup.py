from django.core.management.base import BaseCommand
from django.core.management import call_command
from datetime import datetime
import os
import glob

class Command(BaseCommand):
    help = 'Restaura el sistema desde un backup'

    def add_arguments(self, parser):
        parser.add_argument(
            '--backup-file',
            type=str,
            help='Nombre del archivo de backup a restaurar (ej: backup_auto_20250608_143022.json)'
        )
        parser.add_argument(
            '--list',
            action='store_true',
            help='Lista los backups disponibles'
        )

    def handle(self, *args, **options):
        
        if options['list']:
            self.list_backups()
            return
        
        backup_file = options.get('backup-file')
        
        if not backup_file:
            # Buscar el backup más reciente
            backup_files = sorted(glob.glob('backups/backup_auto_*.json'))
            if not backup_files:
                self.stdout.write(self.style.ERROR('❌ No hay backups disponibles'))
                return
            backup_file = os.path.basename(backup_files[-1])
            self.stdout.write(f'📋 Usando backup más reciente: {backup_file}')
        
        backup_path = os.path.join('backups', backup_file)
        
        if not os.path.exists(backup_path):
            self.stdout.write(self.style.ERROR(f'❌ Backup no encontrado: {backup_file}'))
            return
        
        self.stdout.write(self.style.WARNING('⚠️ ATENCIÓN: Esto sobrescribirá TODOS los datos actuales.'))
        confirm = input('¿Estás seguro de continuar? (s/n): ')
        
        if confirm.lower() != 's':
            self.stdout.write('❌ Restauración cancelada.')
            return
        
        try:
            self.stdout.write(f'🔄 Restaurando desde {backup_file}...')
            
            # Leer y restaurar datos
            with open(backup_path, 'r', encoding='utf-8') as f:
                call_command('loaddata', backup_path, stdout=f)
            
            # Registrar en log
            log_entry = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Restauración desde: {backup_file}\n"
            with open('backup_log.txt', 'a') as log_file:
                log_file.write(log_entry)
            
            self.stdout.write(self.style.SUCCESS('✅ Restauración completada exitosamente'))
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'❌ Error en restauración: {str(e)}'))

    def list_backups(self):
        """Lista todos los backups disponibles"""
        backup_files = sorted(glob.glob('backups/backup_auto_*.json'))
        
        if not backup_files:
            self.stdout.write('📂 No hay backups disponibles')
            return
        
        self.stdout.write('\n📋 Backups disponibles:')
        self.stdout.write('-' * 50)
        for i, backup in enumerate(backup_files, 1):
            filename = os.path.basename(backup)
            size = os.path.getsize(backup) / 1024  # KB
            modified = datetime.fromtimestamp(os.path.getmtime(backup)).strftime('%Y-%m-%d %H:%M:%S')
            self.stdout.write(f'{i}. {filename} ({size:.1f} KB) - {modified}')
        self.stdout.write('-' * 50)