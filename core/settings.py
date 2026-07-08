"""
Django settings for VPJ - Venta Precio Justo project.
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# ====================== NOMBRE DEL PROYECTO ======================
PROJECT_NAME = "VPJ - Venta Precio Justo"

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-tu-clave-secreta-aqui'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', 'whacky-deceiver-motive.ngrok-free.dev']
CSRF_TRUSTED_ORIGINS = ['https://whacky-deceiver-motive.ngrok-free.dev']


# Application definition

INSTALLED_APPS = [
    'daphne',  # ← IMPORTANTE: Debe ir primero para WebSockets
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',  # ← AGREGADO PARA FORMATO DE NÚMEROS
    
    # Terceros
    'channels',
    'dbbackup',  # ← BACKUP Y RESTAURACIÓN DEL SISTEMA
    
    # Aplicaciones del proyecto
    'apps.users',
    'apps.marketplace',
    'apps.chat',
    'apps.complaints',
    'apps.core',
    'apps.backups_manager',  # ← GESTIÓN DE BACKUPS
    'apps.reviews',  # ← SISTEMA DE CALIFICACIONES
    'apps.export',  # ← EXPORTACIONES A EXCEL Y PDF
    'apps.cart',  # ← CARRITO DE COMPRAS
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'core.middleware.block_admin.BlockAdminForOnpeco',  # ← Bloquea admin para ONPECO
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.chat.context_processors.chat_notifications',  # ← AGREGADA
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'
ASGI_APPLICATION = 'core.asgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Channel layers (WebSockets)
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",
    },
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# ====================== CONFIGURACIÓN DE LOCALIZACIÓN (REPÚBLICA DOMINICANA) ======================
# Esto asegura que los números se muestren con punto para decimales y coma para miles

LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'America/Santo_Domingo'
USE_I18N = True

# ========== ¡IMPORTANTE! Configuración de formato numérico ==========
# USE_L10N = False para usar el formato personalizado
USE_L10N = False

# Formato de números personalizado para República Dominicana
# Usamos DECIMAL_SEPARATOR = '.' (punto para decimales)
# Usamos THOUSAND_SEPARATOR = ',' (coma para miles)
DECIMAL_SEPARATOR = '.'
THOUSAND_SEPARATOR = ','
NUMBER_GROUPING = 3  # Agrupar de a 3 dígitos (ej: 1,000.00)

# Formato de fechas
DATE_FORMAT = 'd/m/Y'
SHORT_DATE_FORMAT = 'd/m/Y'
DATE_INPUT_FORMATS = ['%d/%m/%Y', '%d-%m-%Y']

# Formato de hora
TIME_FORMAT = 'H:i'
SHORT_TIME_FORMAT = 'H:i'

# Formato de fecha y hora
DATETIME_FORMAT = 'd/m/Y H:i'
SHORT_DATETIME_FORMAT = 'd/m/Y H:i'

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom user model
AUTH_USER_MODEL = 'users.User'

# Login URLs
LOGIN_URL = '/users/login/'  # ← Corregido: apunta a la URL correcta
LOGIN_REDIRECT_URL = '/'  # ← Redirige al inicio después de login
LOGOUT_REDIRECT_URL = '/'

# ========== CONFIGURACIÓN DE BACKUPS (versión 4.2.1) ==========
# Sistema de restauración tipo "Windows" para ONPECO

# Directorio donde se guardarán los backups
DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location': str(BASE_DIR / 'backups')}

# Formato del nombre del archivo (incluye timestamp para múltiples puntos)
DBBACKUP_FILENAME_TEMPLATE = '{databasename}-{servername}-{datetime}.{extension}'

# Incluir archivos media en el backup
DBBACKUP_INCLUDE_MEDIA = True

# Mantener solo los últimos 10 backups (limpieza automática)
DBBACKUP_CLEANUP_KEEP = 10

# Comprimir backups (gzip)
DBBACKUP_GZIP = True

# Conectar señales para registrar backups automáticamente
DBBACKUP_CONNECT_SIGNALS = True


# ====================== CONFIGURACIÓN DE CORREO ELECTRÓNICO ======================
# Para restablecimiento de contraseña y notificaciones

# ========== PARA PRODUCCIÓN (ENVÍO REAL CON GMAIL) ==========
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'vpj.proyecto@gmail.com'
EMAIL_HOST_PASSWORD = 'awut htdr iwry ixxu'
DEFAULT_FROM_EMAIL = 'VPJ - Venta Precio Justo <vpj.proyecto@gmail.com>'

# ========== PARA DESARROLLO (PRUEBAS) - Comentado ==========
# EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
# EMAIL_FILE_PATH = BASE_DIR / 'sent_emails'

# Tiempo de validez del enlace de restablecimiento (en segundos)
PASSWORD_RESET_TIMEOUT = 86400  # 24 horas