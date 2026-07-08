¡Perfecto! Vamos con el **Manual de Instalación** completo y paso a paso.

---

# MANUAL DE INSTALACIÓN - VPJ (Venta Precio Justo)

**Plataforma de Comercio Justo para ONPECO**

Desarrollado por el Grupo #5 - Monográfico #59
Escuela de Informática - Universidad Autónoma de Santo Domingo (UASD)

---

## 📋 CONTENIDO

1. [Requisitos del Sistema](#1-requisitos-del-sistema)
2. [Instalación de Python](#2-instalación-de-python)
3. [Instalación de PostgreSQL](#3-instalación-de-postgresql)
4. [Clonar o Descargar el Proyecto](#4-clonar-o-descargar-el-proyecto)
5. [Crear y Activar Entorno Virtual](#5-crear-y-activar-entorno-virtual)
6. [Instalar Dependencias](#6-instalar-dependencias)
7. [Configurar Base de Datos](#7-configurar-base-de-datos)
8. [Ejecutar Migraciones](#8-ejecutar-migraciones)
9. [Crear Superusuario](#9-crear-superusuario)
10. [Cargar Datos de Prueba](#10-cargar-datos-de-prueba)
11. [Levantar el Servidor](#11-levantar-el-servidor)
12. [Acceder a la Aplicación](#12-acceder-a-la-aplicación)
13. [Solución de Problemas Comunes](#13-solución-de-problemas-comunes)

---

## 1. REQUISITOS DEL SISTEMA

### 1.1 Hardware

| Componente | Mínimo | Recomendado |
|------------|--------|-------------|
| Procesador | Intel Core i3 / AMD Ryzen 3 | Intel Core i5 / AMD Ryzen 5 |
| RAM | 4 GB | 8 GB o más |
| Disco duro | 10 GB libres | 20 GB libres |
| Conexión a Internet | Banda ancha | Fibra óptica |

### 1.2 Software

| Software | Versión | Descarga |
|----------|---------|----------|
| **Python** | 3.11 o superior | [python.org](https://www.python.org/downloads/) |
| **PostgreSQL** | 14 o superior | [postgresql.org](https://www.postgresql.org/download/) |
| **Git** | 2.30 o superior | [git-scm.com](https://git-scm.com/downloads) |
| **Navegador** | Chrome, Firefox o Edge | Última versión |

### 1.3 Estructura del Proyecto

```
cosecha_directa/
├── apps/               # Aplicaciones Django
│   ├── cart/          # Carrito de compras
│   ├── chat/          # Chat en tiempo real
│   ├── complaints/    # Denuncias
│   ├── marketplace/   # Productos
│   ├── reviews/       # Calificaciones
│   └── users/         # Autenticación y usuarios
├── core/              # Configuración principal
├── templates/         # Plantillas HTML
├── static/            # Archivos estáticos (CSS, JS, imágenes)
├── media/             # Archivos subidos por usuarios
├── capturas/          # Capturas de pantalla (opcional)
├── manage.py          # Script de gestión de Django
├── requirements.txt   # Dependencias del proyecto
└── README.md          # Documentación general
```

---

## 2. INSTALACIÓN DE PYTHON

### 2.1 Descargar Python

1. Ve a: https://www.python.org/downloads/
2. Haz clic en **"Download Python 3.12.X"** (la versión más reciente estable)
3. Descarga el instalador para Windows

### 2.2 Instalar Python

1. **Ejecuta el instalador** descargado
2. **IMPORTANTE:** Marca la opción **"Add Python to PATH"**
3. Haz clic en **"Install Now"**
4. Espera a que termine la instalación
5. Haz clic en **"Close"**

### 2.3 Verificar Instalación

**Abre una terminal (CMD) y escribe:**

```bash
python --version
```

**Deberías ver:**
```
Python 3.12.X
```

**Verifica pip:**

```bash
pip --version
```

**Deberías ver:**
```
pip 24.X.X from ...
```

---

## 3. INSTALACIÓN DE POSTGRESQL

### 3.1 Descargar PostgreSQL

1. Ve a: https://www.postgresql.org/download/windows/
2. Haz clic en **"Download the installer"**
3. Selecciona la versión más reciente para Windows (ej: 16.2)

### 3.2 Instalar PostgreSQL

1. **Ejecuta el instalador** descargado
2. Haz clic en **"Next"** en todas las pantallas
3. **Configuración importante:**
   - **Installation Directory:** `C:\Program Files\PostgreSQL\16`
   - **Data Directory:** `C:\Program Files\PostgreSQL\16\data`
   - **Password:** `postgres` (anótala)
   - **Port:** `5432`
4. Haz clic en **"Next"** hasta que termine
5. **NO DESMARQUES** la opción de instalar pgAdmin (herramienta de administración)

### 3.3 Verificar Instalación

1. **Abre pgAdmin** desde el menú Inicio
2. **Conéctate** al servidor local
3. **Crea una base de datos** para el proyecto:

```sql
CREATE DATABASE cosecha_db_postgres;
```

---

## 4. CLONAR O DESCARGAR EL PROYECTO

### 4.1 Opción A: Clonar con Git (Recomendado)

**Abre la terminal (CMD) y escribe:**

```bash
cd C:\Users\DELL\Desktop
git clone https://github.com/[tu-usuario]/cosecha_directa.git
cd cosecha_directa
```

### 4.2 Opción B: Descargar ZIP

1. Ve a la página del repositorio
2. Haz clic en **"Code"** → **"Download ZIP"**
3. **Extrae** el archivo ZIP en `C:\Users\DELL\Desktop\cosecha_directa`

### 4.3 Verificar Estructura

**Asegúrate de que tengas estos archivos:**

```bash
dir
```

**Deberías ver:**
```
apps/
core/
templates/
static/
media/
manage.py
requirements.txt
```

---

## 5. CREAR Y ACTIVAR ENTORNO VIRTUAL

### 5.1 Crear Entorno Virtual

**Desde la raíz del proyecto, escribe:**

```bash
python -m venv venv
```

**Esto crea una carpeta `venv/` con el entorno virtual.**

### 5.2 Activar Entorno Virtual

**En Windows (CMD):**

```bash
venv\Scripts\activate
```

**Verás que el prompt cambia a:**

```
(venv) C:\Users\DELL\Desktop\cosecha_directa>
```

**En Windows (PowerShell):**

```bash
venv\Scripts\Activate.ps1
```

### 5.3 Verificar Activación

**El entorno virtual está activo si ves `(venv)` al inicio del prompt.**

```bash
(venv) C:\Users\DELL\Desktop\cosecha_directa>
```

---

## 6. INSTALAR DEPENDENCIAS

### 6.1 Instalar Django y Dependencias

**Con el entorno virtual activado, ejecuta:**

```bash
pip install -r requirements.txt
```

### 6.2 Verificar Instalación

**Lista de dependencias principales:**

| Paquete | Versión | Propósito |
|---------|---------|-----------|
| Django | 4.2.7 | Framework web |
| daphne | 4.0.0 | Servidor ASGI (WebSockets) |
| channels | 4.0.0 | Soporte para WebSockets |
| psycopg2-binary | 2.9.9 | Conector PostgreSQL |
| Pillow | 10.1.0 | Manejo de imágenes |
| openpyxl | 3.1.2 | Exportación a Excel |
| django-dbbackup | 4.0.0 | Sistema de backups |
| django-cors-headers | 4.3.0 | CORS (para Ngrok) |

### 6.3 Verificar Instalación

```bash
pip list
```

**Debes ver todos los paquetes listados.**

---

## 7. CONFIGURAR BASE DE DATOS

### 7.1 Crear Base de Datos en PostgreSQL

**Abre pgAdmin y ejecuta:**

```sql
CREATE DATABASE cosecha_db_postgres;
```

**O desde la terminal (CMD):**

```bash
psql -U postgres
```

**Luego escribe:**

```sql
CREATE DATABASE cosecha_db_postgres;
\q
```

### 7.2 Configurar `settings.py`

**Abre el archivo `core/settings.py` y busca `DATABASES`:**

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'cosecha_db_postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

**IMPORTANTE:** Asegúrate de que `PASSWORD` sea la que configuraste al instalar PostgreSQL.

### 7.3 Verificar Conexión

**Desde la terminal (con venv activado):**

```bash
python manage.py dbshell
```

**Si funciona, verás el prompt de PostgreSQL:**

```
psql (16.2)
WARNING: Console code page (437) differs from Windows code page (1252)
...
cosecha_db_postgres=#
```

**Para salir:**

```sql
\q
```

---

## 8. EJECUTAR MIGRACIONES

### 8.1 Crear Migraciones

**Con el entorno virtual activado:**

```bash
python manage.py makemigrations
```

**Deberías ver:**

```
Migrations for 'users':
  apps/users/migrations/0001_initial.py
    - Create model User
Migrations for 'marketplace':
  apps/marketplace/migrations/0001_initial.py
    - Create model Product
...
```

### 8.2 Ejecutar Migraciones

```bash
python manage.py migrate
```

**Deberías ver:**

```
Operations to perform:
  Apply all migrations: admin, auth, cart, chat, complaints, contenttypes, marketplace, reviews, sessions, users
Running migrations:
  Applying users.0001_initial... OK
  Applying marketplace.0001_initial... OK
  ...
```

### 8.3 Verificar Migraciones

```bash
python manage.py showmigrations
```

**Todos los migrations deben tener `[X]` (aplicados).**

---

## 9. CREAR SUPERUSUARIO

### 9.1 Crear Usuario Administrador

```bash
python manage.py createsuperuser
```

**Completa los datos:**

| Campo | Valor | Ejemplo |
|-------|-------|---------|
| Username | Tu cédula | `00112345678` |
| Email | Tu correo | `admin@onpeco.gob.do` |
| Password | Tu contraseña | `admin123` |

### 9.2 Verificar Creación

**Inicia el servidor y ve a:**

```
http://127.0.0.1:8000/admin/
```

**Debes poder iniciar sesión con el superusuario.**

---

## 10. CARGAR DATOS DE PRUEBA

### 10.1 Opción A: Cargar Fixture (Datos de demostración)

**Si tienes un archivo de datos de prueba:**

```bash
python manage.py loaddata datos_prueba.json
```

### 10.2 Opción B: Crear Usuarios de Prueba Manualmente

**Abre una terminal y ejecuta:**

```bash
python manage.py shell
```

**Copia y pega:**

```python
from apps.users.models import User

# Consumidor
consumidor = User.objects.create_user(
    username='bartolo',
    password='bartolo123',
    first_name='Bartolo',
    last_name='Pérez',
    role='consumidor'
)

# Productor
productor = User.objects.create_user(
    username='nancy',
    password='nancy123',
    first_name='Nancy',
    last_name='García',
    role='productor',
    business_name='Finca Los Limones',
    is_approved=True
)

# ONPECO Regulador
regulador = User.objects.create_user(
    username='onpeco_regulador',
    password='regulador123',
    first_name='ONPECO',
    last_name='Regulador',
    role='regulador'
)
regulador.is_staff = True
regulador.save()

# Centro de Acopio
acopio = User.objects.create_user(
    username='centro_acopio',
    password='acopio123',
    first_name='Centro',
    last_name='Acopio',
    role='acopio'
)

print("✅ Usuarios creados correctamente")
```

### 10.3 Usuarios de Prueba

| Rol | Usuario | Contraseña |
|-----|---------|------------|
| Consumidor | bartolo | bartolo123 |
| Productor | nancy | nancy123 |
| ONPECO | onpeco_regulador | regulador123 |
| Centro de Acopio | centro_acopio | acopio123 |

---

## 11. LEVANTAR EL SERVIDOR

### 11.1 Con Daphne (Recomendado)

**El servidor Daphne permite WebSockets (chat en tiempo real).**

```bash
daphne -b 127.0.0.1 -p 8000 core.asgi:application
```

**O usando la ruta completa:**

```bash
venv\Scripts\daphne.exe -b 127.0.0.1 -p 8000 core.asgi:application
```

**Deberías ver:**

```
2026-07-07 10:00:00,000 INFO     Starting server at tcp:port=8000:interface=127.0.0.1
2026-07-07 10:00:00,000 INFO     HTTP/2 support enabled
2026-07-07 10:00:00,000 INFO     Configuring endpoint tcp:port=8000:interface=127.0.0.1
2026-07-07 10:00:00,000 INFO     Listening on TCP address 127.0.0.1:8000
```

### 11.2 Con Runserver (Alternativa)

**Si no necesitas chat en tiempo real:**

```bash
python manage.py runserver
```

### 11.3 Verificar que el Servidor Está Corriendo

**Abre tu navegador y ve a:**

```
http://127.0.0.1:8000/
```

**Debes ver la página de inicio de VPJ.**

---

## 12. ACCEDER A LA APLICACIÓN

### 12.1 Página de Inicio

**URL:** `http://127.0.0.1:8000/`

**Desde aquí puedes:**
- Registrarte como consumidor o productor
- Iniciar sesión
- Ver productos
- Acceder al portal ONPECO

### 12.2 Panel de Administración

**URL:** `http://127.0.0.1:8000/admin/`

**Acceso:** Usuario y contraseña del superusuario creado.

### 12.3 Portal ONPECO

**URL:** `http://127.0.0.1:8000/denuncias/portal/`

**Acceso:** Usuario `onpeco_regulador` / `regulador123`

### 12.4 Ngrok (Para Presentaciones)

**Si necesitas exponer la aplicación a internet:**

1. **Regístrate en** https://ngrok.com/
2. **Descarga ngrok** https://ngrok.com/download
3. **Autentica:**

```bash
ngrok config add-authtoken [TU_TOKEN]
```

4. **Inicia el túnel:**

```bash
ngrok http 8000
```

5. **Obtendrás una URL pública:**

```
https://xxxx-xx-xx-xxx-xx.ngrok-free.dev
```

**Agrega esta URL a `settings.py`:**

```python
ALLOWED_HOSTS = ['*', 'xxxx-xx-xx-xxx-xx.ngrok-free.dev']
CSRF_TRUSTED_ORIGINS = ['https://xxxx-xx-xx-xxx-xx.ngrok-free.dev']
```

---

## 13. SOLUCIÓN DE PROBLEMAS COMUNES

### 13.1 Error: `python no se reconoce como un comando`

| Problema | Solución |
|----------|----------|
| Python no está instalado | Instala Python desde python.org |
| Python no está en PATH | Reinstala Python marcando "Add to PATH" |

### 13.2 Error: `ModuleNotFoundError: No module named 'django'`

| Problema | Solución |
|----------|----------|
| Django no está instalado | `pip install django==4.2.7` |
| Entorno virtual no activado | Activa venv: `venv\Scripts\activate` |

### 13.3 Error: `psycopg2.OperationalError: FATAL: password authentication failed`

| Problema | Solución |
|----------|----------|
| Contraseña incorrecta | Verifica `PASSWORD` en `settings.py` |
| PostgreSQL no está corriendo | Inicia el servicio desde pgAdmin |

### 13.4 Error: `daphne: command not found`

| Problema | Solución |
|----------|----------|
| Daphne no instalado | `pip install daphne` |
| Usa ruta completa | `venv\Scripts\daphne.exe` |

### 13.5 Error: `ModuleNotFoundError: No module named 'core'`

| Problema | Solución |
|----------|----------|
| No estás en la raíz del proyecto | Ve a `cosecha_directa/` |
| El proyecto no está configurado | Verifica la estructura de carpetas |

### 13.6 Error: `CSRF token missing or incorrect` (Ngrok)

| Problema | Solución |
|----------|----------|
| Ngrok no está en `CSRF_TRUSTED_ORIGINS` | Agrega la URL en `settings.py` |

### 13.7 El Chat no funciona (WebSockets)

| Problema | Solución |
|----------|----------|
| Usaste `runserver` en lugar de `daphne` | Usa `daphne -b 127.0.0.1 -p 8000 core.asgi:application` |
| WebSockets no configurados | Verifica `CHANNEL_LAYERS` en `settings.py` |

---

## 14. COMANDOS RÁPIDOS (RESUMEN)

**Copia y pega estos comandos en orden para una instalación rápida:**

```bash
# 1. Navegar al proyecto
cd C:\Users\DELL\Desktop\cosecha_directa

# 2. Activar entorno virtual
venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar migraciones
python manage.py makemigrations
python manage.py migrate

# 5. Crear superusuario
python manage.py createsuperuser

# 6. Levantar servidor (Daphne)
daphne -b 127.0.0.1 -p 8000 core.asgi:application
```

---

## 15. CONTACTO Y SOPORTE

| Contacto | Información |
|----------|-------------|
| ONPECO | https://onpeco.org/ |
| Equipo de desarrollo | Grupo #5 - Monográfico #59 - UASD |

---

**Fin del Manual de Instalación**

*Última actualización: 07 de julio de 2026*

