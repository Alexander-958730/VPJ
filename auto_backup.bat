@echo off
cd C:\Users\DELL\Desktop\cosecha_directa
call venv\Scripts\activate
python manage.py auto_backup
echo %date% %time% - Backup ejecutado >> backup_log.txt
echo.
echo Presiona una tecla para cerrar...
pause > nul