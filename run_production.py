#!/usr/bin/env python
"""Script de producción para VPJ - Venta Precio Justo con Daphne."""
import os
import sys

def main():
    # Configurar variables de entorno
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    
    # Agregar el directorio actual al path
    current_path = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, current_path)
    
    # Ejecutar Daphne
    from daphne.cli import CommandLineInterface
    sys.argv = ['daphne', '-b', '127.0.0.1', '-p', '8000', 'core.asgi:application']
    CommandLineInterface.entrypoint()

if __name__ == '__main__':
    main()