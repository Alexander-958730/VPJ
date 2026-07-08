@echo off
cd C:\Users\DELL\Desktop\cosecha_directa
call venv\Scripts\activate
python manage.py diarybackup
echo Backup completado el %date% %time% >> backups\log.txt