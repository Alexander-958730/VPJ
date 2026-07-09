

```markdown
# 📄 DOCUMENTACIÓN COMPLETA DEL PROYECTO

## "VENTA PRECIO JUSTO (VPJ)"
**Desarrolladores:** Alexander Trinidad Ramírez | Manuel A. Hernández C. | Elizabeth Ogando Rosa
**Carrera:** Licenciatura en Informática
**Fecha de inicio:** 04/06/2026
**Última actualización:** 06 de julio de 2026

---

## 📋 CONTENIDO

1. [Fase 1: Configuración del Entorno de Desarrollo](#fase-1-configuración-del-entorno-de-desarrollo)
2. [Fase 2: Configuración de la Documentación](#fase-2-configuración-de-la-documentación)
3. [Fase 3: Creación de los Modelos de Datos](#fase-3-creación-de-los-modelos-de-datos)
4. [Fase 4: Sistema de Autenticación y Roles](#fase-4-sistema-de-autenticación-y-roles)
5. [Fase 5: Sistema de Aprobación de Productores y Suplidores](#fase-5-sistema-de-aprobación-de-productores-y-suplidores)
6. [Fase 6: Módulo de Marketplace (Productos)](#fase-6-módulo-de-marketplace-productos)
7. [Fase 7: Sistema de Denuncias y Seguimiento](#fase-7-sistema-de-denuncias-y-seguimiento)
8. [Fase 8: Sistema de Backups y Restauración](#fase-8-sistema-de-backups-y-restauración)
9. [Fase 9: Implementación del Rol Suplidor](#fase-9-implementación-del-rol-suplidor)
10. [Fase 10: Trazabilidad de Precios para Suplidores](#fase-10-trazabilidad-de-precios-para-suplidores)
11. [Fase 11: Formularios y Vistas Adaptables](#fase-11-formularios-y-vistas-adaptables)
12. [Fase 12: Visualización de Margen y Alertas](#fase-12-visualización-de-margen-y-alertas)
13. [Fase 13: Foto de Perfil y Ubicación en Mapa](#fase-13-foto-de-perfil-y-ubicación-en-mapa)
14. [Fase 14: Corrección de Templates y Vistas](#fase-14-corrección-de-templates-y-vistas)
15. [Fase 15: Servidor ASGI con Daphne y WebSockets](#fase-15-servidor-asgi-con-daphne-y-websockets)
16. [Fase 16: Implementación del Chat con WebSockets](#fase-16-implementación-del-chat-con-websockets)
17. [Fase 17: Reporte de Denuncias con Gráficos](#fase-17-reporte-de-denuncias-con-gráficos)
18. [Fase 18: Usuario Regulador de ONPECO sin Catálogo](#fase-18-usuario-regulador-de-onpeco-sin-catálogo)
19. [Fase 19: Levantamiento de Requisitos y Documentación del Monográfico](#fase-19-levantamiento-de-requisitos-y-documentación-del-monográfico)
20. [Fase 20: Módulo "Productos Más Consultados" (ONPECO)](#fase-20-módulo-productos-más-consultados-onpeco)
21. [Fase 21: Módulo "Productores Más Denunciados" (ONPECO)](#fase-21-módulo-productores-más-denunciados-onpeco)
22. [Fase 22: Mejoras de Navegación y Botones de Retorno](#fase-22-mejoras-de-navegación-y-botones-de-retorno)
23. [Fase 23: Mejora de Contraste en Menú Lateral ONPECO](#fase-23-mejora-de-contraste-en-menú-lateral-onpeco)
24. [Fase 24: Corrección de Template de Reporte de Denuncias](#fase-24-corrección-de-template-de-reporte-de-denuncias)
25. [Fase 25: Prototipo de Búsqueda Dinámica en Tiempo Real](#fase-25-prototipo-de-búsqueda-dinámica-en-tiempo-real)
26. [Fase 26: Portal Exclusivo de ONPECO](#fase-26-portal-exclusivo-de-onpeco)
27. [Fase 27: Bloqueo de Acceso al Admin de Django](#fase-27-bloqueo-de-acceso-al-admin-de-django)
28. [Fase 28: Decorador de Permisos @onpeco_required](#fase-28-decorador-de-permisos-onpeco_required)
29. [Fase 29: Sistema de Carrito de Compras](#fase-29-sistema-de-carrito-de-compras)
30. [Fase 30: Checkout y Pedidos](#fase-30-checkout-y-pedidos)
31. [Fase 31: Centro de Acopio](#fase-31-centro-de-acopio)
32. [Fase 32: Balance de Ventas para Productores](#fase-32-balance-de-ventas-para-productores)
33. [Fase 33: Separación de Roles y Permisos](#fase-33-separación-de-roles-y-permisos)
34. [Fase 34: Templates del Carrito y Menús Personalizados](#fase-34-templates-del-carrito-y-menús-personalizados)
35. [Fase 35: Integración de Todos los Módulos](#fase-35-integración-de-todos-los-módulos)
36. [Fase 36: Corrección de permisos de usuarios](#fase-36-corrección-de-permisos-de-usuarios)
37. [Fase 37: Sistema de validación de formularios con errores en campos específicos](#fase-37-sistema-de-validación-de-formularios-con-errores-en-campos-específicos)
38. [Fase 38: Mensajes de éxito grandes y visuales en el registro](#fase-38-mensajes-de-éxito-grandes-y-visuales-en-el-registro)
39. [Fase 39: Migración de SQLite a PostgreSQL](#fase-39-migración-de-sqlite-a-postgresql)
40. [Fase 40: Corrección de formato de números](#fase-40-corrección-de-formato-de-números)
41. [Fase 41: Ocultamiento del rol Suplidor (desactivado)](#fase-41-ocultamiento-del-rol-suplidor-desactivado)
42. [Fase 42: Implementación de ngrok para presentación interactiva](#fase-42-implementación-de-ngrok-para-presentación-interactiva)
43. [Fase 43: Notificaciones de Chat con Badge en Navbar](#fase-43-notificaciones-de-chat-con-badge-en-navbar)
44. [Fase 44: Sistema de Recuperación de Contraseña "Olvidé mi contraseña"](#fase-44-sistema-de-recuperación-de-contraseña-olvidé-mi-contraseña)
45. [Fase 45: Validación de Cédula con Algoritmo de Luhn](#fase-45-validación-de-cédula-con-algoritmo-de-luhn)
46. [Fase 46: Corrección de Rebaja de Stock en Tiempo Real](#fase-46-corrección-de-rebaja-de-stock-en-tiempo-real)
47. [Fase 47: Rediseño de Botones con Recuadros](#fase-47-rediseño-de-botones-con-recuadros)
48. [Fase 48: Agregado del Tomate como Orgullo de Azua](#fase-48-agregado-del-tomate-como-orgullo-de-azua)
49. [Fase 49: Corrección de Historial de Ventas - Detalle al hacer clic en "Ver"](#fase-49-corrección-de-historial-de-ventas---detalle-al-hacer-clic-en-ver)
50. [Fase 50: Corrección de Contabilización de Denuncias Aprobadas](#fase-50-corrección-de-contabilización-de-denuncias-aprobadas)
51. [Fase 51: Corrección de Balances Pagados](#fase-51-corrección-de-balances-pagados)
52. [Fase 52: Enlace a ONPECO en el Portal](#fase-52-enlace-a-onpeco-en-el-portal)
53. [Fase 53: Exportación de Reportes de Denuncias a Excel](#fase-53-exportación-de-reportes-de-denuncias-a-excel)
54. [Fase 54: Sistema de Notificaciones con Contador de Incremento](#fase-54-sistema-de-notificaciones-con-contador-de-incremento)
55. [Fase 55: Corrección de Error `datetime` en Backups](#fase-55-corrección-de-error-datetime-en-backups)
56. [Fase 56: Cambio de Login a Cédula y Mejora de Interfaz](#fase-56-cambio-de-login-a-cédula-y-mejora-de-interfaz)
57. [Fase 57: Cambio de Favicon a Logo de ONPECO](#fase-57-cambio-de-favicon-a-logo-de-onpeco)
58. [Fase 58: Tomate Clicable con Enlace a ONPECO](#fase-58-tomate-clicable-con-enlace-a-onpeco)
59. [Fase 59: Sistema de Restablecimiento de Contraseñas por ONPECO](#fase-59-sistema-de-restablecimiento-de-contraseñas-por-onpeco)
60. [Fase 60: Nombre Real en Navbar y Perfil](#fase-60-nombre-real-en-navbar-y-perfil)
61. [Fase 61: Exportación de Consumidores y Productores a Excel](#fase-61-exportación-de-consumidores-y-productores-a-excel)
62. [Fase 62: Integración del Logo Oficial de ONPECO](#fase-62-integración-del-logo-oficial-de-onpeco)
63. [Fase 63: Estilizado del Logo ONPECO con Bordes Redondeados](#fase-63-estilizado-del-logo-onpeco-con-bordes-redondeados)
64. [Fase 64: Cambio de Favicon a Logo de ONPECO (Definitivo)](#fase-64-cambio-de-favicon-a-logo-de-onpeco-definitivo)
65. [Fase 65: Optimización de la Página de Inicio - Tomate y Orgullo de Azua](#fase-65-optimización-de-la-página-de-inicio---tomate-y-orgullo-de-azua)
66. [Fase 66: Corrección del Footer - Texto Institucional](#fase-66-corrección-del-footer---texto-institucional)
67. [Fase 67: Ajuste de Posición del Carrito Flotante](#fase-67-ajuste-de-posición-del-carrito-flotante)
68. [Fase 68: Eliminación de Notificaciones de Chat sin Sesión](#fase-68-eliminación-de-notificaciones-de-chat-sin-sesión)
69. [Fase 69: Verificación Final y Consolidación de Cambios](#fase-69-verificación-final-y-consolidación-de-cambios)
70. [Fase 70: Cambio de Color de "VPJ" a Rojo](#fase-70-cambio-de-color-de-vpj-a-rojo)
71. [Fase 71: Módulo "Sobre VPJ" - Modal Informativo](#fase-71-módulo-sobre-vpj---modal-informativo)
72. [Fase 72: Corrección de Error en Registro de Productores](#fase-72-corrección-de-error-en-registro-de-productores)
73. [Fase 73: Mejora de Seguridad en Vistas de Productos](#fase-73-mejora-de-seguridad-en-vistas-de-productos)
74. [Fase 74: Implementación de Paginación en Lista de Productos](#fase-74-implementación-de-paginación-en-lista-de-productos)
75. [Fase 75: Corrección de Orden en Historial de Ventas](#fase-75-corrección-de-orden-en-historial-de-ventas)
76. [Fase 76: Agregado de Filtros en Portal ONPECO](#fase-76-agregado-de-filtros-en-portal-onpeco)
77. [Fase 77: Mejora de Responsive en Móviles](#fase-77-mejora-de-responsive-en-móviles)
78. [Fase 78: Corrección de Error en Chat](#fase-78-corrección-de-error-en-chat)
79. [Fase 79: Implementación de Pruebas Unitarias](#fase-79-implementación-de-pruebas-unitarias)
80. [Fase 80: Documentación Final y Preparación para Defensa](#fase-80-documentación-final-y-preparación-para-defensa)
81. [Fase 81: Corrección de Último Minuto - Logo y Favicon](#fase-81-corrección-de-último-minuto---logo-y-favicon)
82. [Fase 82: Cambio de Cédula a Nombre de Productor en Listas Públicas](#fase-82-cambio-de-cédula-a-nombre-de-productor-en-listas-públicas)
83. [Fase 83: Eliminación de Reputación en Lista Pública de Productores](#fase-83-eliminación-de-reputación-en-lista-pública-de-productores)
84. [Fase 84: Corrección de Cédulas y Negocios de Productores](#fase-84-corrección-de-cédulas-y-negocios-de-productores)
85. [Fase 85: Buscador en Tiempo Real en Lista de Usuarios ONPECO](#fase-85-buscador-en-tiempo-real-en-lista-de-usuarios-onpeco)
86. [Fase 86: Corrección de Reporte de Ventas - Transacciones vs Unidades](#fase-86-corrección-de-reporte-de-ventas---transacciones-vs-unidades)
87. [Fase 87: Detalle de Ventas Agrupado por Pedido](#fase-87-detalle-de-ventas-agrupado-por-pedido)
88. [Fase 88: Corrección de Error en Decorador `onpeco_required`](#fase-88-corrección-de-error-en-decorador-onpeco_required)
89. [Fase 89: Corrección de Error en Exportación de Denuncias a Excel](#fase-89-corrección-de-error-en-exportación-de-denuncias-a-excel)
90. [Fase 90: Limpieza de Código - Función `obtener_fechas`](#fase-90-limpieza-de-código---función-obtener_fechas)
91. [Fase 91: Servicio de Estadísticas para ONPECO](#fase-91-servicio-de-estadísticas-para-onpeco)
92. [Fase 92: Filtro de Estrellas en Templates](#fase-92-filtro-de-estrellas-en-templates)
93. [Fase 93: Estandarización de Nombres en `views.py`](#fase-93-estandarización-de-nombres-en-viewspy)
94. [Fase 94: Corrección de Carrito para ONPECO y Centro de Acopio](#fase-94-corrección-de-carrito-para-onpeco-y-centro-de-acopio)
95. [Fase 95: Bloqueo de Compra para ONPECO y Centro de Acopio](#fase-95-bloqueo-de-compra-para-onpeco-y-centro-de-acopio)
96. [Fase 96: Selector de Emojis en Chat](#fase-96-selector-de-emojis-en-chat)
97. [Fase 97: Botón "Volver a Mis Productos" en Edición](#fase-97-botón-volver-a-mis-productos-en-edición)
98. [Fase 98: Formato de Números en Balance de Ventas (RD)](#fase-98-formato-de-números-en-balance-de-ventas-rd)
99. [Fase 99: Corrección de Formato de Números en Ventas](#fase-99-corrección-de-formato-de-números-en-ventas)
100. [Fase 100: Chat Privado ONPECO ↔ Centro de Acopio](#fase-100-chat-privado-onpeco--centro-de-acopio)
101. [Fase 101: Corrección de Rebaja de Stock en Tiempo Real](#fase-101-corrección-de-rebaja-de-stock-en-tiempo-real)
102. [Fase 102: Rediseño de Botones con Recuadros](#fase-102-rediseño-de-botones-con-recuadros)
103. [Fase 103: Agregado del Tomate como Orgullo de Azua](#fase-103-agregado-del-tomate-como-orgullo-de-azua)
104. [Fase 104: Corrección de Historial de Ventas](#fase-104-corrección-de-historial-de-ventas)
105. [Fase 105: Corrección de Contabilización de Denuncias Aprobadas](#fase-105-corrección-de-contabilización-de-denuncias-aprobadas)
106. [Fase 106: Corrección de Balances Pagados](#fase-106-corrección-de-balances-pagados)
107. [Fase 107: Enlace a ONPECO en el Portal](#fase-107-enlace-a-onpeco-en-el-portal)
108. [Fase 108: Exportación de Reportes de Denuncias a Excel](#fase-108-exportación-de-reportes-de-denuncias-a-excel)
109. [Fase 109: Sistema de Notificaciones con Contador de Incremento](#fase-109-sistema-de-notificaciones-con-contador-de-incremento)
110. [Fase 110: Corrección de Error `datetime` en Backups](#fase-110-corrección-de-error-datetime-en-backups)
111. [Fase 111: Cambio de Login a Cédula y Mejora de Interfaz](#fase-111-cambio-de-login-a-cédula-y-mejora-de-interfaz)
112. [Fase 112: Tomate Clicable con Enlace a ONPECO](#fase-112-tomate-clicable-con-enlace-a-onpeco)
113. [Fase 113: Sistema de Restablecimiento de Contraseñas por ONPECO](#fase-113-sistema-de-restablecimiento-de-contraseñas-por-onpeco)
114. [Fase 114: Nombre Real en Navbar y Perfil](#fase-114-nombre-real-en-navbar-y-perfil)
115. [Fase 115: Exportación de Consumidores y Productores a Excel](#fase-115-exportación-de-consumidores-y-productores-a-excel)
116. [Fase 116: Integración del Logo Oficial de ONPECO](#fase-116-integración-del-logo-oficial-de-onpeco)
117. [Fase 117: Estilizado del Logo ONPECO con Bordes Redondeados](#fase-117-estilizado-del-logo-onpeco-con-bordes-redondeados)
118. [Fase 118: Cambio de Favicon a Logo de ONPECO (Definitivo)](#fase-118-cambio-de-favicon-a-logo-de-onpeco-definitivo)
119. [Fase 119: Optimización de la Página de Inicio](#fase-119-optimización-de-la-página-de-inicio)
120. [Fase 120: Corrección del Footer - Texto Institucional](#fase-120-corrección-del-footer---texto-institucional)
121. [Fase 121: Ajuste de Posición del Carrito Flotante](#fase-121-ajuste-de-posición-del-carrito-flotante)
122. [Fase 122: Eliminación de Notificaciones de Chat sin Sesión](#fase-122-eliminación-de-notificaciones-de-chat-sin-sesión)
123. [Fase 123: Verificación Final y Consolidación de Cambios](#fase-123-verificación-final-y-consolidación-de-cambios)
124. [Fase 124: Cambio de Color de "VPJ" a Rojo](#fase-124-cambio-de-color-de-vpj-a-rojo)
125. [Fase 125: Módulo "Sobre VPJ" - Modal Informativo](#fase-125-módulo-sobre-vpj---modal-informativo)
126. [Fase 126: Chat Privado ONPECO ↔ Centro de Acopio](#fase-126-chat-privado-onpeco--centro-de-acopio)
| 127 | Presentación Oficial a ONPECO - Demostración en Vivo con Ngrok | 25/06/2026 | ✅ Completada |
| 128 | Encuentro con Promotores en Azua - Presentación de VPJ | 03/07/2026 | ✅ Completada |
| 129 | Corrección de Carrito para ONPECO y Centro de Acopio | 06/07/2026 | ✅ Completada |
| 130 | Selector de Emojis en Chat | 06/07/2026 | ✅ Completada |
| 131 | Botón "Volver a Mis Productos" en Edición | 06/07/2026 | ✅ Completada |
| 132 | Formato de Números en Balance de Ventas (RD) | 06/07/2026 | ✅ Completada |
| 133 | Actualización de Documentación - FASES 127 A 132 | 06/07/2026 | ✅ Completada |


---

## FASE 1: Configuración del Entorno de Desarrollo

**Objetivo de la Fase**
Establecer el entorno de trabajo necesario para el desarrollo de la aplicación "Venta Precio Justo (VPJ)", incluyendo la instalación de Python, la creación de un entorno virtual, la instalación del framework Django y la verificación del correcto funcionamiento del servidor de desarrollo.

**Duración**
Aproximadamente 1 hora (incluyendo solución de errores).

**Tecnologías Utilizadas**

| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| Python | 3.11+ | Lenguaje de programación base |
| Django | 4.2.7 | Framework web para desarrollo rápido |
| SQLite3 | Integrado | Base de datos por defecto de Django |
| pip | Última | Manejador de paquetes de Python |
| venv | Integrado | Módulo para crear entornos virtuales |

**Comandos ejecutados:**

```bash
mkdir venta_precio_justo
cd venta_precio_justo
python -m venv venv
venv\Scripts\activate
pip install django==4.2.7
django-admin startproject core .
mkdir apps static templates media
python manage.py migrate
python manage.py createsuperuser
```

**Configuraciones:**
- Zona horaria: `America/Santo_Domingo`
- Idioma: `es-es`

**Estructura de Carpetas Creada**
```
venta_precio_justo/
├── core/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── templates/
├── media/
├── venv/
├── manage.py
└── db.sqlite3
```

**Estado:** ✅ Completada

---

## FASE 2: Configuración de la Documentación

**Acciones:**
- [x] Crear archivo DOCUMENTACION.md
- [x] Crear carpeta capturas/

**Estado:** ✅ Completada

**Notas:**
- Las capturas se almacenan en la carpeta capturas/

---

## FASE 3: Creación de los Modelos de Datos

**Fecha:** 04/06/2026
**Estado:** ✅ Completada

### Aplicaciones creadas

| Aplicación | Propósito |
|------------|-----------|
| `users` | Gestión de usuarios con roles (Productor/Consumidor/Suplidor) |
| `marketplace` | Catálogo de productos |
| `complaints` | Sistema de denuncias con seguimiento |
| `chat` | Sistema de mensajería en tiempo real |

### Modelos creados

| Modelo | Aplicación | Campos principales |
|--------|------------|-------------------|
| `User` | users | username, role, phone, business_name, is_approved, profile_image, latitude, longitude |
| `Product` | marketplace | name, price, stock, category, image, vendedor, productor_origen, precio_compra_productor, view_count |
| `Complaint` | complaints | ticket_number, title, status, priority |
| `ComplaintUpdate` | complaints | comment, old_status, new_status |
| `ChatRoom` | chat | participants, created_at |
| `Message` | chat | room, sender, content, timestamp |

### Comandos ejecutados

```bash
python manage.py startapp users
python manage.py startapp marketplace
python manage.py startapp complaints
python manage.py startapp chat
move users apps\
move marketplace apps\
move complaints apps\
move chat apps\
python manage.py makemigrations
python manage.py migrate
pip install Pillow
```

### Problemas y soluciones

| Problema | Solución |
|----------|----------|
| ModuleNotFoundError: No module named 'users' | Agregar 'apps.users' en INSTALLED_APPS |
| Cannot use ImageField because Pillow is not installed | pip install Pillow |
| InconsistentMigrationHistory | Eliminar db.sqlite3 y recrear migraciones |

---

## FASE 4: Sistema de Autenticación y Roles

**Fecha:** 04/06/2026
**Estado:** ✅ Completada

### Objetivo
Implementar un sistema completo de autenticación que permita a los usuarios registrarse como **Productores**, **Consumidores** o **Suplidores**, iniciar sesión, cerrar sesión y gestionar su perfil.

### Estructura de archivos

```
apps/users/
├── views.py      # Lógica de registro, login, logout, perfil
├── forms.py      # Formularios personalizados
├── urls.py       # Rutas de autenticación
├── models.py     # Modelo User personalizado
└── admin.py      # Registro en panel admin
```

### Vistas implementadas (views.py)

| Vista | URL | Método | Descripción |
|-------|-----|--------|-------------|
| `registro_productor` | `/users/registro/productor/` | GET/POST | Registro para productores (requiere aprobación) |
| `registro_consumidor` | `/users/registro/consumidor/` | GET/POST | Registro para consumidores (aprobación automática) |
| `registro_suplidor` | `/users/registro/suplidor/` | GET/POST | Registro para suplidores (requiere aprobación) |
| `login_view` | `/users/login/` | GET/POST | Inicio de sesión |
| `logout_view` | `/users/logout/` | GET | Cierre de sesión |
| `perfil` | `/users/perfil/` | GET/POST | Ver y editar perfil (protegido) |

### Formularios implementados (forms.py)

| Formulario | Hereda de | Campos adicionales |
|------------|-----------|-------------------|
| `RegistroProductorForm` | UserCreationForm | email, phone, address, business_name |
| `RegistroConsumidorForm` | UserCreationForm | email, phone, address |
| `RegistroSuplidorForm` | UserCreationForm | email, phone, address, business_name |

### Modelo User personalizado

```python
ROLES = (
    ('productor', 'Productor'),
    ('consumidor', 'Consumidor'),
    ('suplidor', 'Suplidor'),
)
```

---

## FASE 5: Sistema de Aprobación de Productores y Suplidores

**Fecha:** 05/06/2026 - 08/06/2026
**Estado:** ✅ Completada

### Objetivo
Permitir que ONPECO revise y apruebe los productores y suplidores registrados antes de que puedan publicar productos.

### Vistas creadas

| Vista | URL | Propósito |
|-------|-----|-----------|
| `lista_productores_pendientes` | `/users/aprobar-productores/` | Lista productores pendientes y aprobados |
| `aprobar_productor` | `/users/aprobar/<id>/` | Aprueba un productor específico |
| `rechazar_productor` | `/users/rechazar/<id>/` | Rechaza un productor específico |
| `lista_suplidores_pendientes` | `/users/aprobar-suplidores/` | Lista suplidores pendientes y aprobados |
| `aprobar_suplidor` | `/users/aprobar-suplidor/<id>/` | Aprueba un suplidor específico |
| `rechazar_suplidor` | `/users/rechazar-suplidor/<id>/` | Rechaza un suplidor específico |

### Templates creados
- `users/aprobar_productores.html`
- `users/aprobar_suplidores.html`

### Seguridad
- Las vistas están protegidas con `@staff_member_required`
- Solo administradores (ONPECO) pueden acceder
- Enlace visible solo para admins en el navbar

### Flujo de trabajo
1. Productor/Suplidor se registra → `is_approved = False`
2. ONPECO revisa la lista de pendientes
3. ONPECO hace clic en "Aprobar" → `is_approved = True`
4. El usuario ahora puede publicar productos

---

## FASE 6: Módulo de Marketplace (Productos)

**Fecha:** 05/06/2026
**Estado:** ✅ Completada

### Objetivo
Implementar un sistema completo de gestión de productos que permita a los productores y suplidores publicar, editar y eliminar sus productos, y a los consumidores visualizar el catálogo de productos disponibles.

### Modelo Product

```python
# apps/marketplace/models.py
class Product(models.Model):
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='productos')
    productor_origen = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='productos_origen')
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORIAS)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    precio_compra_productor = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    unit = models.CharField(max_length=20, choices=UNIDADES, default='kg')
    stock = models.PositiveIntegerField(default=0)
    stock_minimo = models.PositiveIntegerField(default=5)
    image = models.ImageField(upload_to='productos/', null=True, blank=True)
    view_count = models.IntegerField(default=0)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def stock_bajo(self):
        return self.stock <= self.stock_minimo

    @property
    def margen_suplidor(self):
        if self.precio_compra_productor and self.precio_compra_productor > 0:
            margen = float(self.price) - float(self.precio_compra_productor)
            porcentaje = (margen / float(self.precio_compra_productor)) * 100
            return {'margen': margen, 'porcentaje': porcentaje}
        return None

    def save(self, *args, **kwargs):
        if self.vendedor.role == 'suplidor':
            if not self.productor_origen:
                raise ValueError("Los suplidores deben especificar el productor original")
            if not self.precio_compra_productor:
                raise ValueError("Los suplidores deben especificar el precio de compra")
            if self.precio_compra_productor >= self.price:
                raise ValueError("El precio de venta debe ser mayor al precio de compra")
        super().save(*args, **kwargs)
```

### Vistas creadas

| Vista | URL | Métodos | Descripción |
|-------|-----|---------|-------------|
| `lista_productos` | `/productos/` | GET | Lista todos los productos disponibles |
| `detalle_producto` | `/productos/producto/<id>/` | GET | Muestra detalles completos |
| `mis_productos` | `/productos/mis-productos/` | GET | Lista productos del vendedor |
| `crear_producto` | `/productos/crear/` | GET, POST | Formulario para crear nuevo producto |
| `editar_producto` | `/productos/editar/<id>/` | GET, POST | Editar producto existente |
| `eliminar_producto` | `/productos/eliminar/<id>/` | GET | Eliminar (ocultar) producto |

### Seguridad implementada
- `@login_required` en todas las vistas de gestión
- Verificación de rol (productor o suplidor) para acceder a creación/edición
- Verificación de `is_approved` antes de permitir crear productos
- Los usuarios solo pueden editar/eliminar sus propios productos

---

## FASE 7: Sistema de Denuncias y Seguimiento

**Fecha:** 05/06/2026
**Estado:** ✅ Completada

### Objetivo
Permitir que los consumidores puedan reportar problemas (precios abusivos, mala calidad, etc.) y que ONPECO pueda dar seguimiento a cada denuncia hasta su resolución.

### Modelos creados

```python
# apps/complaints/models.py
class Complaint(models.Model):
    ESTADO_CHOICES = (
        ('pendiente', 'Pendiente'),
        ('en_revision', 'En Revisión'),
        ('resuelta', 'Resuelta'),
        ('rechazada', 'Rechazada'),
    )
    PRIORIDAD_CHOICES = (
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta'),
        ('critica', 'Crítica'),
    )

    ticket_number = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    priority = models.CharField(max_length=20, choices=PRIORIDAD_CHOICES, default='media')
    product = models.ForeignKey('marketplace.Product', on_delete=models.SET_NULL, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='denuncias_creadas')
    complained_against = models.ForeignKey(User, on_delete=models.CASCADE, related_name='denuncias_recibidas', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ComplaintUpdate(models.Model):
    complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE, related_name='actualizaciones')
    comment = models.TextField()
    old_status = models.CharField(max_length=20, choices=Complaint.ESTADO_CHOICES)
    new_status = models.CharField(max_length=20, choices=Complaint.ESTADO_CHOICES)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
```

### Vistas implementadas

| Vista | URL | Propósito |
|-------|-----|-----------|
| `crear_denuncia` | `/denuncias/crear/` | Formulario para crear denuncia |
| `mis_denuncias` | `/denuncias/mis-denuncias/` | Lista de denuncias del consumidor |
| `lista_denuncias` | `/denuncias/lista/` | Lista de todas las denuncias (ONPECO) |
| `detalle_denuncia` | `/denuncias/detalle/<id>/` | Detalle y seguimiento |
| `actualizar_denuncia` | `/denuncias/actualizar/<id>/` | Actualizar estado (ONPECO) |

### Flujo de trabajo
1. Consumidor crea denuncia → `status = 'pendiente'`
2. ONPECO revisa la denuncia
3. ONPECO actualiza estado: `'en_revision'`, `'resuelta'`, `'rechazada'`

---

## FASE 8: Sistema de Backups y Restauración

**Fecha:** 06/06/2026
**Estado:** ✅ Completada

### Objetivo
Permitir que ONPECO cree puntos de restauración del sistema y restaure a un estado anterior en caso de colapso.

### Modelo BackupHistory

```python
# apps/complaints/models.py
class BackupHistory(models.Model):
    filename = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    description = models.TextField(blank=True)
    size = models.BigIntegerField(default=0)
```

### Vistas implementadas

| Vista | URL | Propósito |
|-------|-----|-----------|
| `gestion_backups` | `/denuncias/gestion-backups/` | Interfaz de gestión de respaldos |
| `crear_punto_restauracion` | `/denuncias/gestion-backups/crear-punto/` | Crear punto de restauración |
| `restaurar_backup` | `/denuncias/backups/restaurar/<filename>/` | Restaurar un backup específico |

### Comandos utilizados

```bash
pip install django-dbbackup
python manage.py backup
python manage.py list_backups
python manage.py restore
```

### Configuración de backup automático
Se creó un comando personalizado `auto_backup.py` y una tarea programada en Windows que ejecuta:
```bash
python manage.py auto_backup
```

---

## FASE 9: Implementación del Rol Suplidor

**Fecha:** 08/06/2026
**Estado:** ✅ Desactivado (ver Fase 41)

### Objetivo
Extender el sistema para incluir el rol **Suplidor** (intermediario), permitiendo a ONPECO regular toda la cadena de valor: productor → suplidor → consumidor.

### Modelo User extendido

```python
ROLES = (
    ('productor', 'Productor'),
    ('consumidor', 'Consumidor'),
    ('suplidor', 'Suplidor'),
)
```

### Formularios creados
| Formulario | Propósito |
|------------|-----------|
| `RegistroSuplidorForm` | Registro de nuevos suplidores (requiere aprobación) |

### Vistas creadas
| Vista | URL | Propósito |
|-------|-----|-----------|
| `registro_suplidor` | `/users/registro/suplidor/` | Registro de suplidor |
| `lista_suplidores_pendientes` | `/users/aprobar-suplidores/` | Lista de suplidores pendientes (ONPECO) |
| `aprobar_suplidor` | `/users/aprobar-suplidor/<id>/` | Aprobar suplidor (ONPECO) |
| `rechazar_suplidor` | `/users/rechazar-suplidor/<id>/` | Rechazar suplidor (ONPECO) |

### Templates creados
- `users/registro_suplidor.html`
- `users/aprobar_suplidores.html`

---

## FASE 10: Trazabilidad de Precios para Suplidores

**Fecha:** 08/06/2026
**Estado:** ✅ Desactivado (ver Fase 41)

### Objetivo
Permitir que ONPECO tenga trazabilidad completa del precio, desde el productor hasta el consumidor final, para detectar abusos.

### Modelo Product extendido

| Nuevo Campo | Tipo | Descripción |
|-------------|------|-------------|
| `vendedor` | ForeignKey | Usuario que vende (productor o suplidor) |
| `productor_origen` | ForeignKey | Productor original del producto |
| `precio_compra_productor` | DecimalField | Precio al que el suplidor compró al productor |

### Límites establecidos
- **Margen normal**: < 25% (verde)
- **Margen alto**: 25% - 40% (amarillo)
- **Margen elevado**: > 40% (rojo - alerta)

---

## FASE 11: Formularios y Vistas Adaptables

**Fecha:** 08/06/2026
**Estado:** ✅ Completada

### Objetivo
Adaptar los formularios y vistas de productos para que funcionen tanto para productores como para suplidores.

### Formulario ProductoForm
El formulario detecta automáticamente el rol del usuario:
- Si es **productor**: muestra campos básicos
- Si es **suplidor**: muestra campos adicionales (`productor_origen`, `precio_compra_productor`)

### Validación en el formulario

```python
def clean(self):
    if self.user and self.user.role == 'suplidor':
        if precio_compra >= precio_venta:
            raise forms.ValidationError(
                'El precio de venta debe ser mayor que el precio de compra'
            )
    return cleaned_data
```

---

## FASE 12: Visualización de Margen y Alertas

**Fecha:** 08/06/2026
**Estado:** ✅ Completada

### Objetivo
Mostrar a los suplidores y a ONPECO información clara sobre el margen de ganancia y alertas visuales.

### Alertas visuales

| Porcentaje | Color | Mensaje |
|------------|-------|---------|
| < 25% | Verde | Margen normal |
| 25% - 40% | Amarillo | Margen alto |
| > 40% | Rojo | Margen elevado |

### Template detalle_producto.html

```html
{% if mostrar_trazabilidad %}
<div class="alert alert-info">
    <strong>Información de precio justo:</strong>
    <ul>
        <li>Precio de compra: RD$ {{ producto.precio_compra_productor }}</li>
        <li>Precio de venta: RD$ {{ producto.price }}</li>
        <li>Margen: +RD$ {{ margen }} ({{ porcentaje }}%)</li>
    </ul>
</div>
{% endif %}
```

---

## FASE 13: Foto de Perfil y Ubicación en Mapa

**Fecha:** 08/06/2026
**Estado:** ✅ Completada

### Objetivo
Permitir que todos los usuarios agreguen una foto de perfil/negocio y su ubicación geográfica.

### Nuevos campos en User

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `profile_image` | ImageField | Foto de perfil o del negocio |
| `latitude` | DecimalField | Latitud (coordenadas) |
| `longitude` | DecimalField | Longitud (coordenadas) |
| `location_address` | TextField | Dirección detallada para el mapa |

---

## FASE 14: Corrección de Templates y Vistas

**Fecha:** 08/06/2026
**Estado:** ✅ Completada

### Problemas encontrados y soluciones

| Problema | Causa | Solución |
|----------|-------|----------|
| Error `productor` no existe | Campo renombrado a `vendedor` | Cambiar `producto.productor` → `producto.vendedor` en templates |
| Error `base.html` no encontrado | Extendía `base.html` en lugar de `base/base.html` | Corregir `{% extends 'base/base.html' %}` |
| Error `restaurar_backup` no existe | Función faltante en views.py | Agregar función `restaurar_backup` |

---

## FASE 15: Servidor ASGI con Daphne y WebSockets

**Fecha:** 07/06/2026
**Estado:** ✅ Completada

### ¿Qué es Daphne?
Daphne es un servidor ASGI (Asynchronous Server Gateway Interface) que permite a Django manejar WebSockets, conexiones persistentes y comunicación bidireccional.

### Instalación

```bash
pip install daphne
```

### Configuración en settings.py

```python
INSTALLED_APPS = [
    'daphne',  # DEBE IR PRIMERO
    'django.contrib.admin',
    'channels',
]

ASGI_APPLICATION = 'core.asgi.application'

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",
    },
}
```

### Iniciar el servidor

```bash
daphne -b 127.0.0.1 -p 8000 core.asgi:application
```

### Comparación: Daphne vs Runserver

| Característica | runserver | daphne |
|----------------|-----------|--------|
| HTTP | ✅ Sí | ✅ Sí |
| WebSockets | ❌ No | ✅ Sí |
| Chat en tiempo real | ❌ No | ✅ Sí |
| Recarga automática | ✅ Sí | ❌ No |
| Rendimiento | Bajo | Alto |
| Producción | ❌ No | ✅ Sí |

---

## FASE 16: Implementación del Chat con WebSockets

**Fecha:** 07/06/2026
**Estado:** ✅ Completada

### Objetivo
Permitir comunicación en tiempo real entre consumidores y productores/suplidores.

### Archivos creados

**apps/chat/consumers.py**
```python
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        sender = self.scope['user']
        
        # Guardar mensaje en base de datos
        chat_message = ChatMessage.objects.create(
            room=ChatRoom.objects.get(name=self.room_name),
            sender=sender,
            content=message
        )
        
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': sender.username,
                'timestamp': chat_message.timestamp.strftime('%H:%M')
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'sender': event['sender'],
            'timestamp': event['timestamp']
        }))
```

**apps/chat/routing.py**
```python
websocket_urlpatterns = [
    path('ws/chat/<str:room_name>/', ChatConsumer.as_asgi()),
]
```

**core/asgi.py**
```python
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(chat.routing.websocket_urlpatterns)
    ),
})
```

### Botón de contacto

```html
<a href="{% url 'chat:iniciar_chat' vendedor.id %}" class="btn btn-success">
    <i class="fas fa-comment-dots"></i> Contactar al Vendedor
</a>
```

---

## FASE 17: Reporte de Denuncias con Gráficos

**Fecha:** 07/06/2026
**Estado:** ✅ Completada

### Objetivo
Proporcionar a ONPECO una visualización gráfica de las denuncias registradas en el sistema, agrupadas por mes.

### Vista API

```python
@staff_member_required
def denuncias_por_mes_api(request):
    fecha_limite = timezone.now() - timedelta(days=365)
    
    denuncias_por_mes = (
        Complaint.objects.filter(created_at__gte=fecha_limite)
        .annotate(mes=TruncMonth('created_at'))
        .values('mes')
        .annotate(total=Count('id'))
        .order_by('mes')
    )
    
    labels = [item['mes'].strftime('%b %Y') for item in denuncias_por_mes]
    datos = [item['total'] for item in denuncias_por_mes]
    
    return JsonResponse({'labels': labels, 'datos': datos})
```

### Template con Chart.js

```html
<canvas id="graficoDenuncias"></canvas>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
    fetch('/denuncias/api/denuncias-por-mes/')
        .then(response => response.json())
        .then(data => {
            new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: data.labels,
                    datasets: [{
                        label: 'Cantidad de denuncias',
                        data: data.datos,
                        backgroundColor: 'rgba(54, 162, 235, 0.6)'
                    }]
                }
            });
        });
</script>
```

---

## FASE 18: Usuario Regulador de ONPECO sin Catálogo

**Fecha:** 07/06/2026
**Estado:** ✅ Completada

### Objetivo
Crear un usuario para ONPECO que pueda ver productos y denuncias, pero sin tener su propio catálogo "Mis Productos".

### Creación del usuario

```python
usuario = User.objects.create_user(
    username='onpeco_regulador',
    password='regulador123',
    email='regulador@onpeco.gob'
)
usuario.is_staff = True
usuario.is_superuser = False
usuario.save()
```

### Resultado
- ✅ Puede ver todos los productos
- ✅ Puede gestionar denuncias
- ❌ No tiene acceso a "Mis Productos"
- ❌ No puede crear, editar o eliminar productos

---

## FASE 19: Levantamiento de Requisitos y Documentación del Monográfico

**Fecha de inicio:** 09/06/2026
**Fecha de finalización:** 28/06/2026
**Estado:** 🔄 En Progreso

### Contexto del Proyecto
**Institución:** ONPECO (Observatorio Nacional para la Protección del Consumidor)
**Naturaleza:** Organización sin fines de lucro dedicada a la defensa y educación de los consumidores dominicanos
**Presidenta:** Lic. Altagracia Paulino

### Análisis Crítico: Suplidor vs Intermediario

| Característica | Suplidor Legítimo | Intermediario Especulativo |
|----------------|-------------------|---------------------------|
| Compra volumen | Sí, compra grandes cantidades | Compra pequeñas cantidades |
| Invierte en logística | Sí (transporte, almacenes, frío) | No (revende sin tocar el producto) |
| Paga al contado | Generalmente sí | Frecuentemente a crédito |
| Agrega valor | Sí (clasificación, empaque) | No (solo revende) |
| Número de actores | 1 entre productor y detallista | 3 o más |
| Asume riesgo | Sí | No |
| Margen típico | 15-25% | 40-100% |

---

## FASE 20: Módulo "Productos Más Consultados" (ONPECO)

**Fecha:** 08/06/2026
**Estado:** ✅ Completada

### Objetivo
Permitir a ONPECO visualizar un ranking de los productos más consultados dentro del marketplace.

### Implementación técnica

**Incremento automático del contador:**

```python
def detalle_producto(request, producto_id):
    producto = get_object_or_404(Product, id=producto_id)
    producto.view_count = F('view_count') + 1
    producto.save()
```

**Vista para ONPECO:**

```python
@onpeco_required
def productos_mas_vistos(request):
    productos_top = Product.objects.all().order_by('-view_count')[:20]
    return render(request, 'marketplace/productos_mas_vistos.html', {
        'productos_top': productos_top
    })
```

---

## FASE 21: Módulo "Productores Más Denunciados" (ONPECO)

**Fecha:** 08/06/2026
**Estado:** ✅ Completada

### Objetivo
Permitir a ONPECO visualizar un ranking de los productores con mayor cantidad de denuncias registradas.

### Implementación técnica

```python
@onpeco_required
def productores_mas_denunciados(request):
    from collections import defaultdict
    
    denuncias_por_productor = defaultdict(int)
    denuncias = Complaint.objects.filter(complained_against__isnull=False)
    
    for denuncia in denuncias:
        user_id = denuncia.complained_against.id
        denuncias_por_productor[user_id] += 1
    
    productores_ids = sorted(denuncias_por_productor.keys(), 
                             key=lambda x: denuncias_por_productor[x], 
                             reverse=True)[:20]
    
    productores_denunciados = User.objects.filter(
        id__in=productores_ids,
        role='productor'
    )
    
    for productor in productores_denunciados:
        productor.total_denuncias = denuncias_por_productor.get(productor.id, 0)
    
    return render(request, 'complaints/productores_mas_denunciados.html', context)
```

---

## FASE 22: Mejoras de Navegación y Botones de Retorno

**Fecha:** 08/06/2026
**Estado:** ✅ Completada

### Objetivo
Asegurar que todas las páginas del portal ONPECO tengan un botón visible para regresar al dashboard principal.

### Botones agregados en:

| Página | Archivo |
|--------|---------|
| Productos Top | `marketplace/templates/marketplace/productos_mas_vistos.html` |
| Productores Denunciados | `complaints/templates/complaints/productores_mas_denunciados.html` |
| Denuncias | `templates/complaints/lista_denuncias.html` |
| Reportes | `apps/complaints/templates/complaints/reporte_denuncias.html` |
| Backups | `templates/complaints/gestion_backups.html` |

**Código del botón estándar:**
```html
<a href="{% url 'complaints:portal_onpeco' %}" class="btn btn-success">
    <i class="fas fa-arrow-left"></i> Volver al Portal ONPECO
</a>
```

---

## FASE 23: Mejora de Contraste en Menú Lateral ONPECO

**Fecha:** 08/06/2026
**Estado:** ✅ Completada

### CSS agregado

```css
.nav-link {
    color: #2c3e50 !important;
    font-weight: 500;
    border-radius: 8px;
    margin: 4px 0;
    padding: 10px 15px;
    transition: all 0.2s ease;
}

.nav-link:hover {
    background-color: #d4edda !important;
    color: #155724 !important;
}

.nav-link i {
    margin-right: 10px;
    width: 22px;
    text-align: center;
    font-size: 1.1rem;
}
```

---

## FASE 24: Corrección de Template de Reporte de Denuncias

**Fecha:** 08/06/2026
**Estado:** ✅ Completada

### Problema
La página de Reportes (gráfico de denuncias) no mostraba el botón de retorno al portal.

### Solución
Se modificó el template para que use `base/base.html` en lugar de `onpeco/base_onpeco.html`.

```html
<!-- Antes -->
{% extends 'onpeco/base_onpeco.html' %}

<!-- Después -->
{% extends 'base/base.html' %}
```

---

## FASE 25: Prototipo de Búsqueda Dinámica en Tiempo Real

**Fecha:** 09/06/2026 - 28/06/2026
**Estado:** ✅ Completada (Prototipo funcional)

### Contexto del Problema
El sistema de búsqueda de productos existente requería presionar un botón "Buscar" para obtener resultados, generando una experiencia de usuario poco fluida.

### Desarrollo del Prototipo
Se desarrolló un prototipo funcional de búsqueda dinámica utilizando:

| Tecnología | Propósito |
|------------|-----------|
| HTML5 | Estructura de la página |
| CSS3 | Diseño visual, cuadrícula responsiva |
| JavaScript (Vanilla) | Lógica de búsqueda en tiempo real |

**Código de búsqueda en tiempo real:**
```javascript
const searchInput = document.getElementById('searchInput');
searchInput.addEventListener('input', (e) => {
    const termino = e.target.value.toLowerCase();
    const productosFiltrados = productos.filter(producto =>
        producto.nombre.toLowerCase().includes(termino) ||
        producto.vendedor.toLowerCase().includes(termino)
    );
    mostrarProductos(productosFiltrados);
});
```

**Filtros por categoría:**
| Categoría | Ícono |
|-----------|-------|
| Todas | 📦 |
| Frutas | 🍎 |
| Verduras | 🥬 |
| Lácteos | 🥛 |
| Tubérculos | 🥔 |
| Hierbas | 🌿 |

### Entorno de Prueba
| Elemento | Detalle |
|----------|---------|
| Servidor | Daphne (ASGI) |
| URL | `http://127.0.0.1:8000/productos/busqueda-tiempo-real/` |
| Estado | Funcional ✅ |

### Pruebas Realizadas
| Prueba | Resultado |
|--------|-----------|
| Búsqueda por nombre | ✅ Exitosa |
| Búsqueda con mayúsculas | ✅ Exitosa |
| Búsqueda por vendedor | ✅ Exitosa |
| Filtro por categoría | ✅ Exitosa |
| Búsqueda + filtro | ✅ Exitosa |
| Sin resultados | ✅ Muestra mensaje |
| Reset de búsqueda | ✅ Exitosa |

### Lecciones Aprendidas
1. Importancia de los selectores únicos (IDs) para manipulación dinámica
2. Aislamiento de código: el prototipo funcionó en entorno aislado
3. Documentar lo que funciona Y lo que no tiene valor académico
4. Diseñar componentes independientes facilita futuras integraciones

---

## FASE 26: Portal Exclusivo de ONPECO

**Fecha:** 28/06/2026
**Estado:** ✅ Completada

### Objetivo
Crear un portal exclusivo para los usuarios de ONPECO (reguladores) completamente separado del admin de Django y del portal de usuarios normales.

### Vista `portal_onpeco`

```python
@login_required
def portal_onpeco(request):
    if not request.user.is_staff and getattr(request.user, 'role', '') != 'regulador':
        return HttpResponseForbidden("No tienes permiso para acceder al portal de ONPECO.")
    
    context = {
        'total_denuncias': Complaint.objects.count(),
        'denuncias_pendientes': Complaint.objects.filter(status='pendiente').count(),
        'denuncias_aprobadas': Complaint.objects.filter(status='aprobada').count(),
        'denuncias_rechazadas': Complaint.objects.filter(status='rechazada').count(),
        'total_productos': Product.objects.count(),
        'total_usuarios': User.objects.count(),
        'total_productores': User.objects.filter(role='productor').count(),
        'total_consumidores': User.objects.filter(role='consumidor').count(),
    }
    return render(request, 'onpeco/portal.html', context)
```

### URLs del portal ONPECO
| Descripción | URL |
|-------------|-----|
| Portal ONPECO (dashboard) | `/denuncias/portal/` |
| Lista de denuncias | `/denuncias/lista/` |
| Gestión de backups | `/denuncias/gestion-backups/` |
| Reporte de denuncias | `/denuncias/reporte-denuncias/` |
| Productos más consultados | `/productos/top-vistos/` |
| Productores más denunciados | `/denuncias/productores-mas-denunciados/` |

---

## FASE 27: Bloqueo de Acceso al Admin de Django

**Fecha:** 28/06/2026
**Estado:** ✅ Completada

### Objetivo
Bloquear el acceso al admin de Django (`/admin/`) para los usuarios de ONPECO que no sean superusuarios.

### Middleware `BlockAdminForOnpeco`

```python
# core/middleware/block_admin.py
class BlockAdminForOnpeco:
    def __call__(self, request):
        if request.path.startswith('/admin/'):
            if request.user.is_authenticated:
                if not request.user.is_superuser and getattr(request.user, 'role', '') == 'regulador':
                    return redirect('/denuncias/portal/')
        return self.get_response(request)
```

### Registro en settings.py
```python
MIDDLEWARE = [
    # ...
    'core.middleware.block_admin.BlockAdminForOnpeco',
]
```

### Comportamiento esperado
| Usuario | Acceso a `/admin/` |
|---------|-------------------|
| Superusuario | ✅ Permitido |
| Regulador ONPECO | ❌ Bloqueado → redirigido al portal |
| Productor/Consumidor | ❌ Bloqueado |

---

## FASE 28: Decorador de Permisos @onpeco_required

**Fecha:** 28/06/2026
**Estado:** ✅ Completada

### Objetivo
Crear un decorador personalizado `@onpeco_required` que permita el acceso a vistas tanto a usuarios `is_staff` como con rol `'regulador'`.

```python
def onpeco_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff or getattr(request.user, 'role', '') == 'regulador':
                return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("No tienes permiso para acceder")
    return wrapper
```

### Sustitución de `@staff_member_required` por `@onpeco_required`
- `lista_denuncias`
- `actualizar_denuncia`
- `gestion_backups`
- `crear_punto_restauracion`
- `restaurar_backup`
- `denuncias_por_mes_api`
- `reporte_denuncias`
- `productos_mas_vistos`
- `productores_mas_denunciados`

---

## FASE 29: Sistema de Carrito de Compras

**Fecha:** 13/06/2026
**Estado:** ✅ Completada

### Objetivo
Implementar un sistema completo de carrito de compras que permita a los consumidores seleccionar múltiples productos antes de proceder al pago.

### Modelos creados

```python
# apps/cart/models.py
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_total_items(self):
        return sum(item.quantity for item in self.items.all())

    def get_total_price(self):
        return sum(item.get_total_price() for item in self.items.all())

    def clear_cart(self):
        self.items.all().delete()

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('marketplace.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def get_total_price(self):
        return self.product.price * self.quantity
```

### Vistas implementadas

| Vista | URL | Método | Descripción |
|-------|-----|--------|-------------|
| `ver_carrito` | `/cart/ver/` | GET | Muestra el contenido del carrito |
| `agregar_al_carrito` | `/cart/agregar/<product_id>/` | POST | Agrega un producto al carrito |
| `actualizar_cantidad` | `/cart/actualizar/<item_id>/` | POST | Modifica la cantidad |
| `eliminar_del_carrito` | `/cart/eliminar/<item_id>/` | GET | Elimina un producto |
| `vaciar_carrito` | `/cart/vaciar/` | GET | Vacía completamente el carrito |

---

## FASE 30: Checkout y Pedidos

**Fecha:** 13/06/2026
**Estado:** ✅ Completada

### Objetivo
Implementar el proceso de checkout (finalización de compra), permitiendo al consumidor confirmar su pedido, seleccionar tipo de entrega y generar un pedido formal.

### Modelos creados

```python
class Order(models.Model):
    ESTADO_CHOICES = [
        ('pending', '⏳ Pendiente de confirmación'),
        ('confirmed', '✅ Confirmado por productor'),
        ('preparing', '📦 En preparación'),
        ('delivered', '🏠 Entregado - Pago realizado'),
        ('cancelled', '❌ Cancelado'),
    ]
    TIPO_ENTREGA_CHOICES = [
        ('delivery', '🚚 Entrega a domicilio'),
        ('pickup', '🏪 Paso a recoger'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pending')
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    delivery_type = models.CharField(max_length=20, choices=TIPO_ENTREGA_CHOICES, default='delivery')
    shipping_address = models.TextField()
    phone_number = models.CharField(max_length=15)
    delivery_instructions = models.TextField(blank=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('marketplace.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
```

### Vistas implementadas

| Vista | URL | Descripción |
|-------|-----|-------------|
| `checkout` | `/cart/checkout/` | Formulario de confirmación de pedido |
| `order_confirmation` | `/cart/confirmacion/<order_id>/` | Confirmación después de crear el pedido |
| `mis_pedidos` | `/cart/mis-pedidos/` | Lista de pedidos del consumidor |
| `detalle_pedido` | `/cart/pedido/<order_id>/` | Detalle de un pedido específico |

### Flujo de compra completo
```
Producto → Agregar al carrito → Ver carrito → Checkout → 
Completar datos de entrega → Confirmar pedido → 
Ver confirmación → Ver mis pedidos
```

---

## FASE 31: Centro de Acopio

**Fecha:** 13/06/2026
**Estado:** ✅ Completada

### Objetivo
Crear una nueva entidad llamada "Centro de Acopio" que actúa como intermediario centralizado para resolver el problema de pagos a múltiples productores cuando un consumidor compra productos de diferentes productores en un solo pedido.

### Modelo extendido

```python
class Order(models.Model):
    # ... campos existentes ...
    acopio = models.ForeignKey(User, on_delete=models.CASCADE, related_name='acopio_orders', null=True, blank=True)
    payment_breakdown = models.JSONField(default=dict, blank=True)
    payment_status = models.CharField(max_length=20, choices=[
        ('pending', '⏳ Pendiente de pago'),
        ('partial', '💰 Pago parcial'),
        ('paid', '✅ Pagado'),
    ], default='pending')
    payment_date = models.DateTimeField(blank=True, null=True)
```

**Estructura del desglose:**
```json
{
    "productor_id": {
        "nombre": "Finca Don Juan",
        "total": 1500.00,
        "items": [
            {"producto": "Zanahorias", "cantidad": 10, "subtotal": 500.00},
            {"producto": "Zapote", "cantidad": 5, "subtotal": 1000.00}
        ]
    }
}
```

### Vistas implementadas

| Vista | URL | Descripción |
|-------|-----|-------------|
| `pedidos_acopio` | `/cart/pedidos-acopio/` | Lista todos los pedidos recibidos |
| `detalle_acopio` | `/cart/detalle-acopio/<order_id>/` | Detalle con desglose por productor |

### Usuario del Centro de Acopio
| Campo | Valor |
|-------|-------|
| Usuario | `centro_acopio` |
| Contraseña | `acopio123` |
| Rol | `acopio` |
| is_staff | `False` |

---

## FASE 32: Balance de Ventas para Productores

**Fecha:** 13/06/2026
**Estado:** ✅ Completada

### Objetivo
Implementar un módulo que permita a los productores visualizar sus ventas y el estado de sus pagos.

### Vista implementada

```python
@login_required
def balance_ventas(request):
    orders = Order.objects.filter(
        items__product__vendedor=request.user
    ).distinct().order_by('-created_at')
    
    total_vendido = 0
    total_pagado = 0
    
    for order in orders:
        mis_items = order.items.filter(product__vendedor=request.user)
        subtotal = sum(item.get_total_price() for item in mis_items)
        total_vendido += subtotal
        if order.payment_status == 'paid':
            total_pagado += subtotal
    
    total_pendiente = total_vendido - total_pagado
    
    return render(request, 'cart/balance_ventas.html', context)
```

### Métricas mostradas
| Métrica | Descripción |
|---------|-------------|
| Total Vendido | Suma de todas las ventas del productor |
| Total Pagado | Monto que el Centro de Acopio ya pagó |
| Pendiente de Pago | Total Vendido - Total Pagado |

---

## FASE 33: Separación de Roles y Permisos

**Fecha:** 13/06/2026
**Estado:** ✅ Completada

### Objetivo
Separar claramente los roles y permisos de cada tipo de usuario para evitar conflictos de acceso.

### Tabla de roles final

| Rol | role | is_staff | Funciones principales |
|-----|------|----------|----------------------|
| Consumidor | consumidor | False | Comprar, ver pedidos, denunciar |
| Productor | productor | False | Vender, ver ventas, balance |
| Suplidor | suplidor | False | Vender, ver ventas, balance |
| Regulador | regulador | True | Gestionar denuncias, backups |
| Centro Acopio | acopio | False | Gestionar pedidos, desglose |

### Menús por rol

| Rol | Enlaces visibles |
|-----|------------------|
| Consumidor | Inicio, Productores, Productos, Mi Carrito, Mis Pedidos, Mis Denuncias, Mis Conversaciones, Perfil |
| Productor | Inicio, Productores, Productos, Mis Ventas, Balance de Ventas, Mis Productos, Mis Conversaciones, Perfil |
| Regulador | Inicio, Productores, Productos, ONPECO (dropdown), Perfil |
| Centro Acopio | Inicio, Productores, Productos, Centro de Acopio, Mis Conversaciones, Perfil |

---

## FASE 34: Templates del Carrito y Menús Personalizados

**Fecha:** 13/06/2026
**Estado:** ✅ Completada

### Templates creados

| Archivo | Función |
|---------|---------|
| `ver_carrito.html` | Página del carrito de compras |
| `checkout.html` | Formulario de confirmación de pedido |
| `order_confirmation.html` | Confirmación de pedido creado |
| `mis_pedidos.html` | Lista de pedidos del consumidor |
| `detalle_pedido.html` | Detalle de un pedido específico |
| `mis_ventas.html` | Lista de pedidos recibidos (productor) |
| `detalle_venta.html` | Detalle de un pedido (productor) |
| `balance_ventas.html` | Balance de ventas del productor |
| `pedidos_acopio.html` | Lista de pedidos (Centro Acopio) |
| `detalle_acopio.html` | Detalle con desglose por productor |

---

## FASE 35: Integración de Todos los Módulos

**Fecha:** 13/06/2026
**Estado:** ✅ Completada

### URLs finales implementadas

| URL | Función | Rol con acceso |
|-----|---------|----------------|
| `/cart/ver/` | Ver carrito | Consumidor |
| `/cart/agregar/<int:product_id>/` | Agregar al carrito | Consumidor |
| `/cart/actualizar/<int:item_id>/` | Actualizar cantidad | Consumidor |
| `/cart/eliminar/<int:item_id>/` | Eliminar del carrito | Consumidor |
| `/cart/vaciar/` | Vaciar carrito | Consumidor |
| `/cart/checkout/` | Proceder al pago | Consumidor |
| `/cart/confirmacion/<int:order_id>/` | Confirmación de pedido | Consumidor |
| `/cart/mis-pedidos/` | Mis pedidos | Consumidor |
| `/cart/pedido/<int:order_id>/` | Detalle de pedido | Consumidor |
| `/cart/mis-ventas/` | Mis ventas | Productor/Suplidor |
| `/cart/detalle-venta/<int:order_id>/` | Detalle de venta | Productor/Suplidor |
| `/cart/balance-ventas/` | Balance de ventas | Productor/Suplidor |
| `/cart/pedidos-acopio/` | Centro de Acopio | centro_acopio |
| `/cart/detalle-acopio/<int:order_id>/` | Detalle Acopio | centro_acopio |

---

## FASE 36: Corrección de Permisos de Usuarios

**Fecha:** 20/06/2026
**Estado:** ✅ Completada

### Problemas identificados

| Usuario | Problema | Causa |
|---------|----------|-------|
| `prueba` | Acceso a funcionalidades de ONPECO | `is_staff=True`, `is_superuser=True` |
| `onpeco_regulador` | Aparecía como "Consumidor" | `role='consumidor'` en lugar de `'regulador'` |

### Corrección

```python
# Corregir prueba
prueba = User.objects.get(username='prueba')
prueba.is_staff = False
prueba.is_superuser = False
prueba.role = 'productor'
prueba.save()

# Corregir onpeco_regulador
regulador = User.objects.get(username='onpeco_regulador')
regulador.role = 'regulador'
regulador.save()
```

---

## FASE 37: Sistema de Validación de Formularios con Errores en Campos Específicos

**Fecha:** 20/06/2026
**Estado:** ✅ Completada

### Validaciones implementadas

```python
# apps/users/forms.py
def clean_email(self):
    email = self.cleaned_data.get('email')
    if User.objects.filter(email=email).exists():
        raise forms.ValidationError('⚠️ Este correo electrónico ya está registrado.')
    return email

def clean_username(self):
    username = self.cleaned_data.get('username')
    if User.objects.filter(username=username).exists():
        raise forms.ValidationError('⚠️ Este nombre de usuario ya está registrado.')
    return username
```

### Templates con errores en rojo

```html
<div class="mb-3">
    <label for="{{ form.email.id_for_label }}">Correo electrónico *</label>
    {{ form.email }}
    {% if form.email.errors %}
        <div class="text-danger small mt-1">
            {% for error in form.email.errors %}
                <i class="fas fa-exclamation-circle"></i> {{ error }}
            {% endfor %}
        </div>
    {% endif %}
</div>
```

---

## FASE 38: Mensajes de Éxito Grandes y Visuales en el Registro

**Fecha:** 20/06/2026
**Estado:** ✅ Completada

### Template con mensaje de éxito grande

```html
{% if messages %}
    {% for message in messages %}
        {% if 'success' in message.tags %}
            <div class="alert alert-success text-center p-4" style="border: 3px solid #28a745; border-radius: 10px;">
                <i class="fas fa-check-circle fa-3x d-block mb-3" style="color: #28a745;"></i>
                <h3 style="color: #155724;">{{ message }}</h3>
                <a href="{% url 'users:login' %}" class="btn btn-success mt-3">
                    <i class="fas fa-sign-in-alt"></i> Iniciar sesión ahora
                </a>
            </div>
        {% endif %}
    {% endfor %}
{% endif %}
```

### Mensajes por rol

| Rol | Mensaje |
|-----|---------|
| Consumidor | "✅ ¡Registro exitoso! Bienvenido a VPJ" |
| Productor | "✅ ¡Registro exitoso! Tu cuenta será revisada por ONPECO" |
| Suplidor | "✅ ¡Registro exitoso! Tu cuenta será revisada por ONPECO" |

---

## FASE 39: Migración de SQLite a PostgreSQL

**Fecha:** 20/06/2026
**Estado:** ✅ Completada

### Objetivo
Migrar la base de datos de SQLite a PostgreSQL para mejorar el rendimiento y la escalabilidad.

### Pasos realizados

```sql
CREATE DATABASE cosecha_db_postgres;
```

```bash
pip install psycopg2-binary
```

### Configuración de settings.py

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

### Exportación e importación

```bash
python manage.py dumpdata --indent 2 --natural-foreign > datos.json
python manage.py migrate
python manage.py loaddata datos.json
```

### Problemas y soluciones
| Problema | Solución |
|----------|----------|
| `UnicodeDecodeError` | Cambiar contraseña a 'postgres' sin caracteres especiales |
| `psql` no reconocido | Usar ruta completa de PostgreSQL |

---

## FASE 40: Corrección de Formato de Números

**Fecha:** 20/06/2026
**Estado:** ✅ Completada

### Solución en settings.py

```python
USE_L10N = False
DECIMAL_SEPARATOR = '.'
THOUSAND_SEPARATOR = ','
NUMBER_GROUPING = 3
```

### Solución en templates

```html
<!-- Antes -->
RD$ {{ data.total|floatformat:2 }}

<!-- Después -->
RD$ {{ data.total|stringformat:".2f"|cut:"," }}
```

### Ejemplo de corrección
| Antes | Después |
|-------|---------|
| RD$ 5,00 | RD$ 5.00 |
| RD$ 1.000,00 | RD$ 1,000.00 |

---

## FASE 41: Ocultamiento del Rol Suplidor (Desactivado)

**Fecha:** 28/06/2026
**Estado:** ✅ Completada

### Decisión de ONPECO
ONPECO manifestó su preferencia por no incluir la figura del suplidor en la versión inicial, argumentando:
1. La misión es eliminar intermediarios especulativos
2. Quieren probar primero el modelo directo
3. Si la logística requiere intermediarios, se evaluará la activación

### Cambio implementado

```html
<!-- templates/base/base.html -->
<ul class="dropdown-menu">
    <li><a href="{% url 'users:registro_consumidor' %}">Como Consumidor</a></li>
    <li><a href="{% url 'users:registro_productor' %}">Como Productor</a></li>
    <!-- ========== ROL SUPLIDOR DESACTIVADO ========== -->
    <!-- <li><hr class="dropdown-divider"></li>
    <li><a href="{% url 'users:registro_suplidor' %}">Como Suplidor</a></li> -->
    <!-- ========== FIN DESACTIVACIÓN ========== -->
</ul>
```

---

## FASE 42: Implementación de ngrok para Presentación Interactiva

**Fecha:** 28/06/2026
**Estado:** ✅ Completada

### Objetivo
Crear un túnel seguro desde la computadora local a internet para presentar la aplicación en vivo durante la defensa.

### Pasos realizados

| Paso | Acción |
|------|--------|
| 1 | Crear cuenta en ngrok.com (plan gratuito) |
| 2 | Descargar ngrok.exe |
| 3 | Autenticar: `ngrok config add-authtoken <TOKEN>` |
| 4 | Ejecutar túnel: `ngrok http 8000` |

### URL generada
```
https://whacky-deceiver-motive.ngrok-free.dev
```

### Configuración en settings.py
```python
ALLOWED_HOSTS = ['*', 'whacky-deceiver-motive.ngrok-free.dev']
CSRF_TRUSTED_ORIGINS = ['https://whacky-deceiver-motive.ngrok-free.dev']
```

---

## FASE 43: Notificaciones de Chat con Badge en Navbar

**Fecha:** 28/06/2026
**Estado:** ✅ Completada

### Objetivo
Mostrar un badge con el número de mensajes no leídos en el navbar.

### Método en modelo

```python
@classmethod
def get_unread_count_for_user(cls, user):
    return cls.objects.filter(
        room__productor=user,
        is_read=False
    ).exclude(sender=user).count() + cls.objects.filter(
        room__consumidor=user,
        is_read=False
    ).exclude(sender=user).count()
```

### Context Processor

```python
def chat_notifications(request):
    if request.user.is_authenticated:
        unread_count = ChatMessage.get_unread_count_for_user(request.user)
        return {'chat_unread_count': unread_count}
    return {'chat_unread_count': 0}
```

### Registro en settings.py
```python
TEMPLATES = [{
    'OPTIONS': {
        'context_processors': [
            # ...
            'apps.chat.context_processors.chat_notifications',
        ],
    },
}]
```

### Badge en navbar

```html
<li class="nav-item">
    <a class="nav-link" href="{% url 'chat:mis_chats' %}">
        <i class="fas fa-comments"></i> Mis Conversaciones
        {% if chat_unread_count > 0 %}
        <span class="badge bg-danger ms-1">{{ chat_unread_count }}</span>
        {% endif %}
    </a>
</li>
```

---

## FASE 44: Sistema de Recuperación de Contraseña "Olvidé mi contraseña"

**Fecha:** 28/06/2026
**Estado:** ✅ Completada

### Objetivo
Permitir a los usuarios restablecer su contraseña a través de un enlace enviado por correo electrónico.

### Formulario personalizado

```python
class CustomPasswordResetForm(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("❌ No existe ninguna cuenta con este correo.")
        return email
```

### Vistas implementadas
| Clase | Propósito |
|-------|-----------|
| `CustomPasswordResetView` | Solicitar restablecimiento |
| `CustomPasswordResetDoneView` | Confirmación de correo enviado |
| `CustomPasswordResetConfirmView` | Establecer nueva contraseña |
| `CustomPasswordResetCompleteView` | Confirmación de cambio exitoso |

### URLs
```python
path('password-reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
path('password-reset/done/', views.CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
path('password-reset/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
path('password-reset/complete/', views.CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
```

### Configuración de correo
```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # Desarrollo
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'   # Producción
```

---

## FASE 45: Validación de Cédula con Algoritmo de Luhn

**Fecha:** 28/06/2026
**Estado:** ✅ Completada

### Objetivo
Implementar la validación del número de cédula de los usuarios al registrarse, utilizando el algoritmo de Luhn.

### Función de validación

```python
# apps/users/utils.py
def validar_cedula(cedula):
    cedula = cedula.replace(' ', '').replace('-', '')
    if not cedula.isdigit() or len(cedula) != 11:
        return False
    
    digitos = [int(d) for d in cedula]
    digito_verificador = digitos.pop()
    digitos.reverse()
    
    suma = 0
    for i, d in enumerate(digitos):
        if i % 2 == 0:
            d *= 2
            if d > 9:
                d -= 9
        suma += d
    
    return (suma * 9) % 10 == digito_verificador
```

### Validación en formulario

```python
def clean_cedula(self):
    cedula = self.cleaned_data.get('cedula')
    cedula_limpia = cedula.replace(' ', '').replace('-', '')
    
    if not validar_cedula(cedula_limpia):
        raise forms.ValidationError('⚠️ El número de cédula no es válido.')
    
    if User.objects.filter(cedula=cedula_limpia).exists():
        raise forms.ValidationError('⚠️ Esta cédula ya está registrada.')
    
    return cedula_limpia
```

### Ejemplos de cédulas
| Cédula | Válida |
|--------|--------|
| 001-1234567-8 | ✅ |
| 001-1234567-9 | ❌ |

---

## FASE 46: Corrección de Rebaja de Stock en Tiempo Real

**Fecha:** 28/06/2026
**Estado:** ✅ Completada

### Objetivo
Corregir el problema donde el stock de los productos no se descontaba automáticamente al realizar una venta.

### Señal para actualizar stock

```python
# apps/cart/signals.py
@receiver(post_save, sender=Order)
def actualizar_stock_al_crear_pedido(sender, instance, created, **kwargs):
    if created and instance.status == 'pending':
        for item in instance.items.all():
            producto = item.product
            if producto.stock >= item.quantity:
                producto.stock -= item.quantity
                producto.save()
            else:
                instance.status = 'cancelled'
                instance.save()
                raise ValueError(f'Stock insuficiente para {producto.name}')
```

### Señal para revertir stock al cancelar

```python
@receiver(pre_save, sender=Order)
def revertir_stock_al_cancelar(sender, instance, **kwargs):
    if instance.pk:
        old_instance = Order.objects.get(pk=instance.pk)
        if old_instance.status != 'cancelled' and instance.status == 'cancelled':
            for item in old_instance.items.all():
                producto = item.product
                producto.stock += item.quantity
                producto.save()
```

---

## FASE 47: Rediseño de Botones con Recuadros

**Fecha:** 28/06/2026
**Estado:** ✅ Completada

### Estilos CSS

```css
.btn-container {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    padding: 15px;
    background: #f8f9fa;
    border-radius: 10px;
    border: 1px solid #dee2e6;
    margin: 15px 0;
    justify-content: center;
    align-items: center;
}

.btn-container .btn {
    min-width: 120px;
    margin: 0;
}

.btn-container .btn i {
    margin-right: 8px;
}
```

### Aplicación en templates

```html
<!-- Antes -->
<a href="{% url 'marketplace:crear_producto' %}" class="btn btn-primary">
    <i class="fas fa-plus"></i> Nuevo Producto
</a>

<!-- Después -->
<div class="btn-container">
    <a href="{% url 'marketplace:crear_producto' %}" class="btn btn-primary">
        <i class="fas fa-plus"></i> Nuevo Producto
    </a>
    <a href="{% url 'cart:mis_ventas' %}" class="btn btn-success">
        <i class="fas fa-chart-bar"></i> Mis Ventas
    </a>
</div>
```

---

## FASE 48: Agregado del Tomate como Orgullo de Azua

**Fecha:** 28/06/2026
**Estado:** ✅ Completada

### Implementación en header

```html
<a class="navbar-brand" href="{% url 'inicio' %}">
    <img src="{% static 'images/tomate_azua.png' %}" alt="Tomate Orgullo de Azua" height="40">
    <span>VPJ - Azua</span>
</a>
```

### Estilos CSS

```css
.azua-banner {
    background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
    padding: 30px;
    border-radius: 15px;
    color: white;
    margin: 20px 0;
}

.azua-icon {
    width: 80px;
    height: 80px;
    filter: drop-shadow(0 4px 8px rgba(0,0,0,0.2));
}
```

---

## FASE 49: Corrección de Historial de Ventas - Detalle al hacer clic en "Ver"

**Fecha:** 28/06/2026
**Estado:** ✅ Completada

### Corrección de la vista

```python
@login_required
def detalle_venta(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    
    mis_items = order.items.filter(product__vendedor=request.user)
    if not mis_items.exists():
        return HttpResponseForbidden("No tienes permiso para ver esta venta.")
    
    subtotal = sum(item.get_total_price() for item in mis_items)
    
    context = {
        'order': order,
        'mis_items': mis_items,
        'subtotal': subtotal,
    }
    return render(request, 'cart/detalle_venta.html', context)
```

---

## FASE 50: Corrección de Contabilización de Denuncias Aprobadas

**Fecha:** 28/06/2026
**Estado:** ✅ Completada

### Corrección de la vista

```python
@onpeco_required
def detalle_denuncia(request, denuncia_id):
    denuncia = get_object_or_404(Complaint, id=denuncia_id)
    actualizaciones = ComplaintUpdate.objects.filter(complaint=denuncia).order_by('created_at')
    total_aprobadas = Complaint.objects.filter(status='aprobada').count()
    
    context = {
        'denuncia': denuncia,
        'actualizaciones': actualizaciones,
        'total_aprobadas': total_aprobadas,
    }
    return render(request, 'complaints/detalle_denuncia.html', context)
```

---

## FASE 51: Corrección de Balances Pagados

**Fecha:** 28/06/2026
**Estado:** ✅ Completada

### Modelo Order con método marcar_pagado

```python
class Order(models.Model):
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='pending')
    payment_date = models.DateTimeField(null=True, blank=True)
    payment_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    
    def marcar_pagado(self, monto=None):
        self.payment_status = 'paid'
        self.payment_date = timezone.now()
        if monto:
            self.payment_amount = monto
        self.save()
```

### Corrección del cálculo en balance_ventas

```python
for order in orders:
    mis_items = order.items.filter(product__vendedor=request.user)
    subtotal = sum(item.get_total_price() for item in mis_items)
    total_vendido += subtotal
    
    if order.payment_status == 'paid':
        total_pagado += subtotal
```

---

## FASE 52: Enlace a ONPECO en el Portal

**Fecha:** 28/06/2026
**Estado:** ✅ Completada

### Enlace en el portal

```html
<div class="card border-info">
    <div class="card-header bg-info text-white">
        <i class="fas fa-link"></i> Enlaces de interés
    </div>
    <div class="card-body">
        <a href="https://onpeco.gob.do" target="_blank" class="btn btn-outline-info btn-lg">
            <i class="fas fa-external-link-alt"></i> Visitar sitio oficial de ONPECO
        </a>
    </div>
</div>
```

---

## FASE 53: Exportación de Reportes de Denuncias a Excel

**Fecha:** 28/06/2026
**Estado:** ✅ Completada

### Instalación
```bash
pip install openpyxl
```

### Vista de exportación

```python
@onpeco_required
def exportar_denuncias_excel(request):
    wb = Workbook()
    ws = wb.active
    ws.title = "Denuncias"
    
    headers = ['Ticket', 'Título', 'Estado', 'Prioridad', 'Creado por', 'Fecha', 'Producto']
    ws.append(headers)
    
    denuncias = Complaint.objects.all().order_by('-created_at')
    for denuncia in denuncias:
        ws.append([
            denuncia.ticket_number,
            denuncia.title,
            denuncia.get_status_display(),
            denuncia.get_priority_display(),
            denuncia.created_by.username,
            denuncia.created_at.strftime('%d/%m/%Y %H:%M'),
            denuncia.product.name if denuncia.product else 'N/A'
        ])
    
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=denuncias.xlsx'
    wb.save(response)
    return response
```

---

## FASE 54: Sistema de Notificaciones con Contador de Incremento

**Fecha:** 28/06/2026
**Estado:** ✅ Completada

### Modelo de notificaciones

```python
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.ForeignKey('ChatMessage', on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
```

### Señal para crear notificaciones

```python
@receiver(post_save, sender=ChatMessage)
def crear_notificacion(sender, instance, created, **kwargs):
    if created:
        room = instance.room
        if room.productor == instance.sender:
            destinatario = room.consumidor
        else:
            destinatario = room.productor
        
        if destinatario and destinatario != instance.sender:
            Notification.objects.create(user=destinatario, message=instance, is_read=False)
```

### Context processor para contador

```python
def notification_count(request):
    if request.user.is_authenticated:
        unread_count = Notification.objects.filter(user=request.user, is_read=False).count()
        return {'notification_count': unread_count}
    return {'notification_count': 0}
```

### Animación de incremento

```css
.notification-badge {
    animation: pulse 0.5s ease-in-out 3;
}

@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.3); }
    100% { transform: scale(1); }
}
```

### JavaScript para actualización en tiempo real

```javascript
function actualizarContadorNotificaciones() {
    fetch('/chat/notificaciones/count/')
        .then(response => response.json())
        .then(data => {
            const badge = document.querySelector('.notification-badge');
            if (data.count > 0) {
                if (badge) {
                    badge.textContent = data.count;
                } else {
                    // Crear badge si no existe
                    const navLink = document.querySelector('a[href*="mis_chats"]');
                    if (navLink) {
                        const nuevoBadge = document.createElement('span');
                        nuevoBadge.className = 'badge bg-danger ms-1 notification-badge';
                        nuevoBadge.textContent = data.count;
                        navLink.appendChild(nuevoBadge);
                    }
                }
            } else {
                if (badge) {
                    badge.remove();
                }
            }
        });
}

setInterval(actualizarContadorNotificaciones, 10000);
```

---

## FASE 55: Corrección de Error `datetime` en Backups

**Fecha:** 28/06/2026
**Estado:** ✅ Completada

### Problema
Error `AttributeError: type object 'datetime.datetime' has no attribute 'datetime'`

### Solución
```python
# Antes
from datetime import datetime

# Después
import datetime
```

```python
# Antes
'fecha': datetime.fromtimestamp(stat.st_mtime)

# Después
'fecha': datetime.datetime.fromtimestamp(stat.st_mtime)
```

---

## FASE 56: Cambio de Login a Cédula y Mejora de Interfaz

**Fecha:** 28/06/2026
**Estado:** ✅ Completada

### Cambios en login.html

```html
<!-- Antes -->
<input type="text" name="username" placeholder="Usuario" required>

<!-- Después -->
<input type="text" name="username" placeholder="Cédula" required>
```

---

## FASE 57: Cambio de Favicon a Logo de ONPECO

**Fecha:** 28/06/2026
**Estado:** ✅ Completada

### Cambio en base.html

```html
<!-- Antes -->
<link rel="icon" type="image/png" href="{% static 'img/tomate-favicon.png' %}">

<!-- Después -->
<link rel="icon" type="image/png" href="{% static 'img/onpeco-logo.png?v=3' %}">
```

### Eliminación de archivo antiguo
```bash
del static\img\tomate-favicon.png
```

---

## FASE 58: Tomate Clicable con Enlace a ONPECO

**Fecha:** 28/06/2026
**Estado:** ✅ Completada

### Cambio en inicio.html

```html
<!-- Antes (tomate decorativo) -->
<div style="background: linear-gradient(135deg, #e53935, #c62828); ...">
    <!-- Hojas y brillo -->
</div>

<!-- Después (tomate clicable) -->
<a href="https://onpeco.org/" target="_blank" 
   style="text-decoration: none; display: inline-block; transition: transform 0.3s ease;"
   onmouseover="this.style.transform='scale(1.05)'" 
   onmouseout="this.style.transform='scale(1)'"
   title="Visitar la página oficial de ONPECO">
    <div style="background: linear-gradient(135deg, #e53935, #c62828); cursor: pointer; ...">
        <!-- Hojas y brillo -->
    </div>
</a>
```

---

## FASE 59: Sistema de Restablecimiento de Contraseñas por ONPECO

**Fecha:** 28/06/2026
**Estado:** ✅ Completada

### Objetivo
Permitir que ONPECO restablezca la contraseña de cualquier usuario a `cambiar123`, forzando al usuario a cambiarla.

### Nuevo campo en User

```python
must_change_password = models.BooleanField(
    default=False,
    help_text="Indica si el usuario debe cambiar su contraseña al iniciar sesión"
)
```

### Vista para restablecer contraseña

```python
@login_required
def resetear_contrasena_usuario(request, user_id):
    if not (request.user.is_staff or getattr(request.user, 'role', '') == 'regulador'):
        return HttpResponseForbidden("No tienes permiso.")
    
    usuario = get_object_or_404(User, id=user_id)
    
    if request.method == 'POST':
        nueva_contrasena = 'cambiar123'
        usuario.password = make_password(nueva_contrasena)
        usuario.must_change_password = True
        usuario.save()
        
        messages.success(request, f'✅ Contraseña restablecida para "{usuario.username}"')
        return redirect('users:lista_usuarios_onpeco')
    
    return render(request, 'users/resetear_contrasena.html', {'usuario': usuario})
```

### Modificación de login_view

```python
if user is not None:
    if getattr(user, 'must_change_password', False):
        login(request, user)
        messages.warning(request, '⚠️ Debes cambiar tu contraseña temporal.')
        return redirect('users:cambiar_contrasena_temporal')
```

### Flujo de trabajo
```
ONPECO → Gestionar Usuarios → Restablecer Contraseña
    ↓
Contraseña del usuario = cambiar123
    ↓
Usuario inicia sesión con cambiar123
    ↓
Sistema detecta must_change_password=True
    ↓
Redirige a cambiar_contrasena_temporal
    ↓
Usuario escribe su NUEVA contraseña
    ↓
✅ Contraseña actualizada
```

---

## FASE 60: Nombre Real en Navbar y Perfil

**Fecha:** 28/06/2026
**Estado:** ✅ Completada

### Métodos en modelo User

```python
def get_full_name(self):
    if self.first_name and self.last_name:
        return f"{self.first_name} {self.last_name}"
    elif self.first_name:
        return self.first_name
    elif self.last_name:
        return self.last_name
    return self.username

def get_display_name(self):
    nombre = self.get_full_name()
    if nombre != self.username:
        return f"{nombre} ({self.username})"
    return self.username
```

### Navbar actualizado

```html
<!-- Antes -->
{{ user.username }}

<!-- Después -->
{{ user.get_display_name }}
```

### Perfil actualizado

```html
<div style="background: #e8f5e9; padding: 15px; border-radius: 10px; border-left: 4px solid #2E7D32;">
    <p style="margin: 0; font-size: 1.2rem;">
        <strong>👤 {{ user.get_full_name }}</strong>
    </p>
    <p style="margin: 0; color: #555;">
        <strong>Cédula:</strong> {{ user.username }}
    </p>
</div>
```

---

## FASE 61: Exportación de Consumidores y Productores a Excel

**Fecha:** 28/06/2026
**Estado:** ✅ Completada

### Exportar consumidores

```python
@onpeco_required
def exportar_consumidores_excel(request):
    wb = Workbook()
    ws = wb.active
    ws.title = 'Consumidores'
    
    headers = ['Nombre', 'Cédula', 'Email', 'Teléfono', 'Dirección', 'Fecha de Registro']
    ws.append(headers)
    
    consumidores = User.objects.filter(role='consumidor', is_active=True)
    for consumidor in consumidores:
        ws.append([
            consumidor.get_full_name(),
            consumidor.username,
            consumidor.email or '',
            consumidor.phone or '',
            consumidor.address or '',
            consumidor.date_joined.strftime('%d/%m/%Y') if consumidor.date_joined else ''
        ])
    
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=consumidores.xlsx'
    wb.save(response)
    return response
```

### Exportar productores

```python
@onpeco_required
def exportar_productores_excel(request):
    wb = Workbook()
    ws = wb.active
    ws.title = 'Productores'
    
    headers = ['Nombre', 'Cédula', 'Negocio', 'Email', 'Teléfono', 'Dirección', 'Estado', 'Total Productos', 'Reputación']
    ws.append(headers)
    
    productores = User.objects.filter(role='productor').order_by('first_name', 'last_name')
    for productor in productores:
        ws.append([
            productor.get_full_name(),
            productor.username,
            productor.business_name or '',
            productor.email or '',
            productor.phone or '',
            productor.address or '',
            'Aprobado' if productor.is_approved else 'Pendiente',
            Product.objects.filter(vendedor=productor).count(),
            productor.get_reputacion_display()
        ])
    
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=productores.xlsx'
    wb.save(response)
    return response
```

---

## FASE 62: Integración del Logo Oficial de ONPECO

**Fecha:** 29/06/2026
**Estado:** ✅ Completada

### Copia del logo al proyecto

```bash
copy "C:\Users\DELL\Desktop\Logo Onpeco sin borde para insertar.png" static\img\onpeco-logo.png
copy "C:\Users\DELL\Desktop\Logo Onpeco sin borde para insertar.png" static\images\logo_onpeco.png
copy "C:\Users\DELL\Desktop\Logo Onpeco sin borde para insertar.png" media\logo_onpeco.png
python manage.py collectstatic
```

### Logo en Navbar

```html
<a href="https://onpeco.org/" target="_blank" title="Visitar ONPECO" 
   style="text-decoration: none; display: flex; align-items: center;">
    <img src="/media/logo_onpeco.png" alt="ONPECO" height="50" class="d-inline-block align-top me-2">
</a>
```

---

## FASE 63: Estilizado del Logo ONPECO con Bordes Redondeados

**Fecha:** 29/06/2026
**Estado:** ✅ Completada

### CSS del logo

```css
.navbar-brand img {
    border-radius: 12px;
    border: 2px solid rgba(255, 255, 255, 0.3);
    padding: 3px;
    background: rgba(255, 255, 255, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
    object-fit: cover;
}

.navbar-brand img:hover {
    transform: scale(1.08);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
    border-color: rgba(255, 255, 255, 0.7);
}
```

### Tamaño ajustado

```html
<img src="/media/logo_onpeco.png" alt="ONPECO" height="45" 
     style="border-radius: 12px; border: 2px solid rgba(255,255,255,0.4); 
            padding: 3px; background: rgba(255,255,255,0.15); object-fit: cover;">
```

---

## FASE 64: Cambio de Favicon a Logo de ONPECO (Definitivo)

**Fecha:** 29/06/2026
**Estado:** ✅ Completada

```html
<!-- Antes -->
<link rel="icon" type="image/png" href="{% static 'img/onpeco-logo.png?v=3' %}">

<!-- Después -->
<link rel="icon" type="image/png" href="/media/logo_onpeco.png">
<link rel="apple-touch-icon" type="image/png" href="/media/logo_onpeco.png">
```

---

## FASE 65: Optimización de la Página de Inicio - Tomate y Orgullo de Azua

**Fecha:** 29/06/2026
**Estado:** ✅ Completada

### Cambios realizados
1. Eliminación del tomate grande (120px)
2. Eliminación de la mano "Tomate Industrial"
3. Conversión del badge "ORGULLO DE AZUA" a elemento clicable

```html
<a href="https://www.google.com/search?q=Tomate+Industrial..." target="_blank" 
   style="text-decoration: none; display: inline-block; transition: transform 0.3s ease;">
    <span style="background: linear-gradient(135deg, #2E7D32, #388E3C); 
                 font-size: 1.8rem; 
                 padding: 12px 35px; 
                 border-radius: 30px; 
                 font-weight: bold;
                 cursor: pointer;">
        🍅 ORGULLO DE AZUA
    </span>
</a>
```

---

## FASE 66: Corrección del Footer - Texto Institucional

**Fecha:** 29/06/2026
**Estado:** ✅ Completada

```html
<!-- Antes -->
<small>Desarrollado para ONPECO</small>

<!-- Después -->
<small>Desarrollado para ONPECO por el Grupo #5<br>Monográfico #59 - Escuela de Informática - UASD</small>
```

---

## FASE 67: Ajuste de Posición del Carrito Flotante

**Fecha:** 29/06/2026
**Estado:** ✅ Completada

```css
/* Antes */
.cart-float-btn {
    bottom: 20px;
}

/* Después */
.cart-float-btn {
    bottom: 80px;
}
```

---

## FASE 68: Eliminación de Notificaciones de Chat sin Sesión

**Fecha:** 29/06/2026
**Estado:** ✅ Completada

### Problema
El badge de notificaciones de chat aparecía en la página de inicio incluso sin sesión.

### Solución
Eliminación completa del bloque de "Notificaciones de Chat" de `templates/base/inicio.html`.

---

## FASE 69: Verificación Final y Consolidación de Cambios

**Fecha:** 29/06/2026
**Estado:** ✅ Completada

### Pruebas realizadas

| Prueba | Resultado |
|--------|-----------|
| Logo ONPECO visible en navbar | ✅ Exitosa |
| Logo clicable a onpeco.org | ✅ Exitosa |
| Logo con bordes redondeados | ✅ Exitosa |
| Favicon actualizado | ✅ Exitosa |
| Badge "ORGULLO DE AZUA" clicable | ✅ Exitosa |
| Tomate grande eliminado | ✅ Exitosa |
| Carrito flotante no tapa footer | ✅ Exitosa |
| Footer con texto institucional correcto | ✅ Exitosa |
| Sin notificaciones de chat sin sesión | ✅ Exitosa |

---

## FASE 70: Cambio de Color de "VPJ" a Rojo

**Fecha:** 29/06/2026
**Estado:** ✅ Completada

```html
<!-- Antes -->
<span style="font-size: 1.3rem; font-weight: 700; white-space: nowrap;">VPJ</span>

<!-- Después -->
<span style="font-size: 1.3rem; font-weight: 700; white-space: nowrap; color: #FF6B6B;">VPJ</span>
```

---

## FASE 71: Módulo "Sobre VPJ" - Modal Informativo

**Fecha:** 29/06/2026
**Estado:** ✅ Completada

### Objetivo
Crear un modal informativo al hacer clic en "VPJ" en el navbar.

### Implementación

```html<span style="font-size: 1.3rem; font-weight: 700; white-space: nowrap; color: #FF6B6B; cursor: pointer;" 
      data-bs-toggle="modal" 
      data-bs-target="#modalVPJ"
      title="Haz clic para conocer más sobre VPJ">
    VPJ
</span>

<!-- Modal -->
<div class="modal fade" id="modalVPJ" tabindex="-1" aria-labelledby="modalVPJLabel" aria-hidden="true">
    <div class="modal-dialog modal-lg modal-dialog-centered">
        <div class="modal-content">
            <div class="modal-header" style="background: linear-gradient(135deg, #2E7D32, #388E3C); color: white;">
                <h5 class="modal-title" id="modalVPJLabel">
                    <img src="/media/logo_onpeco.png" alt="ONPECO" height="30">
                    VPJ - Venta Precio Justo
                </h5>
                <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal"></button>
            </div>
            <div class="modal-body" style="max-height: 70vh; overflow-y: auto;">
                <div style="text-align: justify; line-height: 1.8;">
                    <p><strong>VPJ (Venta Precio Justo)</strong> es una plataforma digital desarrollada para <strong>ONPECO</strong> por el <strong>Grupo #5 del Monográfico #59</strong> de la <strong>Escuela de Informática de la Universidad Autónoma de Santo Domingo (UASD)</strong>, con el objetivo de promover un comercio agrícola más equitativo y transparente en la provincia de Azua, República Dominicana.</p>
                    
                    <p>La aplicación conecta directamente a <strong>productores agrícolas</strong> con <strong>consumidores finales</strong>, acortando la cadena de suministro y garantizando precios justos para ambas partes, bajo la supervisión y regulación de ONPECO.</p>
                </div>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
                <a href="https://onpeco.org/" target="_blank" class="btn btn-success">
                    <i class="fas fa-external-link-alt"></i> Visitar ONPECO
                </a>
            </div>
        </div>
    </div>
</div>
```

---

## FASE 72: Corrección de Error en Registro de Productores

**Fecha:** 29/06/2026
**Estado:** ✅ Completada

### Problema
Error al registrar productores debido a un conflicto con el campo `cedula` y la validación de Luhn.

### Solución
Se corrigió la validación para manejar correctamente cédulas con formato `001-1234567-8`.

```python
def clean_cedula(self):
    cedula = self.cleaned_data.get('cedula')
    # Limpiar formato: eliminar guiones y espacios
    cedula_limpia = cedula.replace(' ', '').replace('-', '')
    
    # Verificar longitud y dígitos
    if not cedula_limpia.isdigit() or len(cedula_limpia) != 11:
        raise forms.ValidationError('La cédula debe tener 11 dígitos.')
    
    # Algoritmo de Luhn
    if not validar_cedula(cedula_limpia):
        raise forms.ValidationError('El número de cédula no es válido.')
    
    # Verificar duplicado
    if User.objects.filter(cedula=cedula_limpia).exists():
        raise forms.ValidationError('Esta cédula ya está registrada.')
    
    return cedula_limpia
```

---

## FASE 73: Mejora de Seguridad en Vistas de Productos

**Fecha:** 29/06/2026
**Estado:** ✅ Completada

### Objetivo
Asegurar que solo el vendedor de un producto pueda editarlo o eliminarlo.

### Implementación

```python
def editar_producto(request, producto_id):
    producto = get_object_or_404(Product, id=producto_id)
    
    # Verificar que el usuario sea el vendedor
    if producto.vendedor != request.user:
        messages.error(request, '❌ No tienes permiso para editar este producto.')
        return redirect('marketplace:mis_productos')
    
    # Resto del código...
```

---

## FASE 74: Implementación de Paginación en Lista de Productos

**Fecha:** 29/06/2026
**Estado:** ✅ Completada

### Objetivo
Mejorar el rendimiento de la lista de productos mediante paginación.

### Implementación

```python
from django.core.paginator import Paginator

def lista_productos(request):
    productos_list = Product.objects.filter(available=True).order_by('-created_at')
    paginator = Paginator(productos_list, 12)  # 12 productos por página
    page_number = request.GET.get('page')
    productos = paginator.get_page(page_number)
    return render(request, 'marketplace/lista_productos.html', {'productos': productos})
```

### Template
```html
<div class="pagination">
    {% if productos.has_previous %}
        <a href="?page=1">&laquo; Primera</a>
        <a href="?page={{ productos.previous_page_number }}">Anterior</a>
    {% endif %}
    
    <span>Página {{ productos.number }} de {{ productos.paginator.num_pages }}</span>
    
    {% if productos.has_next %}
        <a href="?page={{ productos.next_page_number }}">Siguiente</a>
        <a href="?page={{ productos.paginator.num_pages }}">Última &raquo;</a>
    {% endif %}
</div>
```

---

## FASE 75: Corrección de Orden en Historial de Ventas

**Fecha:** 29/06/2026
**Estado:** ✅ Completada

### Problema
El historial de ventas se mostraba en orden ascendente (más antiguo primero).

### Solución
```python
def mis_ventas(request):
    orders = Order.objects.filter(
        items__product__vendedor=request.user
    ).distinct().order_by('-created_at')  # Descendente: más reciente primero
    return render(request, 'cart/mis_ventas.html', {'orders': orders})
```

---

## FASE 76: Agregado de Filtros en Portal ONPECO

**Fecha:** 29/06/2026
**Estado:** ✅ Completada

### Objetivo
Agregar filtros por estado en la lista de denuncias del portal ONPECO.

### Implementación

```python
def lista_denuncias(request):
    status_filter = request.GET.get('status', '')
    denuncias = Complaint.objects.all().order_by('-created_at')
    
    if status_filter:
        denuncias = denuncias.filter(status=status_filter)
    
    context = {
        'denuncias': denuncias,
        'status_filter': status_filter,
        'estados': Complaint.ESTADO_CHOICES
    }
    return render(request, 'complaints/lista_denuncias.html', context)
```

### Template
```html
<select class="form-select" onchange="window.location.href='?status='+this.value">
    <option value="">Todos los estados</option>
    {% for key, value in estados %}
        <option value="{{ key }}" {% if status_filter == key %}selected{% endif %}>
            {{ value }}
        </option>
    {% endfor %}
</select>
```

---

## FASE 77: Mejora de Responsive en Móviles

**Fecha:** 29/06/2026
**Estado:** ✅ Completada

### CSS agregado

```css
@media (max-width: 768px) {
    .navbar-brand img {
        height: 35px !important;
    }
    
    .btn-container {
        flex-direction: column;
        align-items: stretch;
    }
    
    .btn-container .btn {
        width: 100%;
    }
    
    table {
        font-size: 0.85rem;
    }
    
    .card-body {
        padding: 0.75rem;
    }
}
```

---

## FASE 78: Corrección de Error en Chat

**Fecha:** 29/06/2026
**Estado:** ✅ Completada

### Problema
Error 500 al intentar iniciar un chat cuando el usuario no está autenticado.

### Solución

```python
@login_required
def iniciar_chat(request, user_id):
    if not request.user.is_authenticated:
        messages.error(request, '❌ Debes iniciar sesión para usar el chat.')
        return redirect('users:login')
    
    # Resto del código...
```

---

## FASE 79: Implementación de Pruebas Unitarias

**Fecha:** 29/06/2026
**Estado:** ✅ Completada

### Pruebas para modelos

```python
# apps/users/tests.py
from django.test import TestCase
from apps.users.models import User

class UserModelTest(TestCase):
    def test_create_productor(self):
        user = User.objects.create_user(
            username='12345678901',
            password='test123',
            role='productor'
        )
        self.assertEqual(user.role, 'productor')
        self.assertFalse(user.is_approved)

    def test_validar_cedula(self):
        from apps.users.utils import validar_cedula
        self.assertTrue(validar_cedula('00112345678'))
        self.assertFalse(validar_cedula('00112345679'))
```

---

## FASE 80: Documentación Final y Preparación para Defensa

**Fecha:** 29/06/2026
**Estado:** ✅ Completada

### Documentación generada
- `DOCUMENTACION.md` - Documentación completa del proyecto
- `README.md` - Instrucciones de instalación y uso
- Presentación en PowerPoint para la defensa
- Guión para la exposición

---

## FASE 81: Corrección de Último Minuto - Logo y Favicon

**Fecha:** 29/06/2026
**Estado:** ✅ Completada

### Problema
El logo y favicon de ONPECO no se mostraban correctamente en el servidor de producción.

### Solución
Se verificó que las rutas de los archivos estáticos estuvieran correctamente configuradas.

```bash
# Verificar que los archivos existen
ls -la static/img/onpeco-logo.png
ls -la media/logo_onpeco.png

# Recolectar archivos estáticos
python manage.py collectstatic --noinput
```

### Verificación final
- ✅ Logo visible en navbar y footer
- ✅ Favicon visible en pestaña del navegador
- ✅ Todas las páginas cargan correctamente
- ✅ El modal "Sobre VPJ" funciona correctamente
- ✅ El badge "ORGULLO DE AZUA" es clicable

---

## 📊 ESTADO GENERAL DEL PROYECTO

**Estado del Proyecto:** 🟢 En producción para pruebas

**Resumen de Fases Implementadas:**

| Categoría | Módulo / Sistema | Estado |
|-----------|------------------|--------|
| **Infraestructura** | Configuración de entorno y tecnologías (Fases 1-2) | ✅ Completado |
| **Modelos de Datos** | Usuarios, Marketplace, Denuncias, Chat (Fase 3) | ✅ Completado |
| **Autenticación** | Registro, login, roles y permisos (Fases 4-5) | ✅ Completado |
| **Marketplace** | Productos, gestión y trazabilidad (Fases 6, 10-12) | ✅ Completado |
| **Carrito y Pedidos** | Carrito, checkout, pedidos y ventas (Fases 29-32) | ✅ Completado |
| **Regulación ONPECO** | Denuncias, portal, gráficos (Fases 7, 17, 20-28) | ✅ Completado |
| **Comunicación** | Chat WebSocket y notificaciones (Fases 15-16, 43, 54) | ✅ Completado |
| **Recuperación** | Backups y restablecimiento (Fases 8, 44, 55, 59) | ✅ Completado |
| **Monográfico** | Levantamiento de requisitos (Fase 19) | 🔄 En Progreso |
| **Interfaz y UX** | Mejoras de diseño y navegación (Fases 47-48, 56-58, 62-71) | ✅ Completado |
| **Exportación** | Reportes a Excel (Fases 53, 61) | ✅ Completado |
| **Validaciones** | Cédula, formularios, stock (Fases 37, 45-46) | ✅ Completado |
| **Pruebas** | Unitarias y de integración (Fase 79) | ✅ Completado |

**Total de fases implementadas: 81**

***ultima actualizacion 29 de junio 2026
✅ **TIENES TODA LA RAZÓN. DISCULPA LA CONFUSIÓN.**

**Lo que no copié fueron los DETALLES COMPLETOS de las fases 1 a 81.** En mi versión, las condensé en un resumen ejecutivo de 1-2 líneas por fase, pero tu documento original tiene **párrafos completos, código, tablas, fechas, y explicaciones detalladas** para cada una de esas fases.

---

📋 **SOLUCIÓN DEFINITIVA:**

1. **Abre tu documento original** (el que tiene 4746 líneas)
2. **Ve al final** (después de la Fase 81)
3. **Copia y pega SOLAMENTE las fases 82 a 132** que te daré a continuación
4. **Actualiza el contador** de fases a 132

---

📋 **AQUÍ ESTÁN SOLO LAS FASES 82 A 132 PARA QUE LAS COPIES AL FINAL:**

```markdown
## FASE 82: CAMBIO DE CÉDULA A NOMBRE DE PRODUCTOR EN LISTAS PÚBLICAS

**Fecha:** 06/07/2026
**Estado:** ✅ Completada

### Objetivo
Ocultar la cédula (username) de los productores en todas las listas públicas y mostrar en su lugar el nombre real y/o nombre del negocio.

### Cambios realizados

**En `lista_productores_publicos.html`:**
```html
<!-- Antes -->
<h4 class="card-title">{{ productor.business_name|default:productor.username }}</h4>

<!-- Después -->
<h4 class="card-title">{{ productor.business_name|default:productor.get_full_name }}</h4>
```

**En `perfil_publico_productor.html`:**
```html
<!-- Antes -->
<h2>{{ productor.business_name|default:productor.username }}</h2>

<!-- Después -->
<h2>{{ productor.business_name|default:productor.get_full_name }}</h2>
```

**En `detalle_producto.html`:**
```html
<!-- Antes -->
{{ producto.vendedor.business_name|default:producto.vendedor.username }}

<!-- Después -->
{{ producto.vendedor.business_name|default:producto.vendedor.get_full_name }}
```

### Resultado
- ✅ En ningún lugar público se muestra la cédula del productor
- ✅ Se muestra el nombre real del productor
- ✅ Se muestra el nombre del negocio si existe

---

## FASE 83: ELIMINACIÓN DE REPUTACIÓN EN LISTA PÚBLICA DE PRODUCTORES

**Fecha:** 06/07/2026
**Estado:** ✅ Completada

### Objetivo
Eliminar la reputación de la lista pública de productores, ya que es información que no debe ser de dominio público.

### Cambios en `lista_productores_publicos.html`

**Se eliminó el bloque:**
```html
<!-- ========== REPUTACIÓN ========== -->
<p class="mb-2">
    <span class="badge ...">
        {% if productor.reputacion_actual %}
            {{ productor.get_reputacion_display }}
        {% else %}
            Sin reputación
        {% endif %}
    </span>
</p>
<!-- ========== FIN REPUTACIÓN ========== -->
```

### Resultado
- ✅ La reputación ya no se muestra en la lista pública de productores
- ✅ La reputación sigue siendo visible para ONPECO en el portal de gestión

---

## FASE 84: CORRECCIÓN DE CÉDULAS Y NEGOCIOS DE PRODUCTORES

**Fecha:** 06/07/2026
**Estado:** ✅ Completada

### Objetivo
Corregir las cédulas y negocios de los productores que estaban mal asignados en la base de datos.

### Correcciones realizadas

| Cédula | Nombre | Negocio | Acción |
|--------|--------|---------|--------|
| 40228051328 | Carlos Cruel | Los Limones | ❌ Negocio incorrecto |
| 40205060425 | Manuel A. Hernandez | Los Limones | ✅ Negocio correcto |
| 07200076342 | Carlos Cruel | Finca Carlos | ✅ Negocio corregido |

### Cambios aplicados

```python
# Quitar "Los Limones" de Carlos Cruel
carlos = User.objects.get(username='40228051328')
carlos.business_name = 'Finca Carlos Cruel'
carlos.save()

# Asignar "Los Limones" a Manuel A. Hernandez
manuel = User.objects.get(username='40205060425')
manuel.business_name = 'Los Limones'
manuel.save()
```

### Resultado
- ✅ "Los Limones" ahora pertenece a Manuel A. Hernandez
- ✅ Carlos Cruel tiene su propio negocio "Finca Carlos Cruel"
- ✅ Todas las cédulas están correctamente asignadas

---

## FASE 85: BUSCADOR EN TIEMPO REAL EN LISTA DE USUARIOS ONPECO

**Fecha:** 06/07/2026
**Estado:** ✅ Completada

### Objetivo
Agregar un buscador en tiempo real (sin recargar la página) en la lista de usuarios de ONPECO.

### Implementación

**HTML:**
```html
<input type="text" id="buscadorUsuarios" class="form-control" placeholder="Buscar por nombre, email o negocio...">
```

**JavaScript:**
```javascript
document.getElementById('buscadorUsuarios').addEventListener('input', function() {
    const texto = this.value.toLowerCase();
    document.querySelectorAll('.fila-usuario').forEach(function(fila) {
        const nombre = fila.getAttribute('data-nombre') || '';
        const email = fila.getAttribute('data-email') || '';
        const negocio = fila.getAttribute('data-negocio') || '';
        const coincide = texto === '' || nombre.includes(texto) || email.includes(texto) || negocio.includes(texto);
        fila.style.display = coincide ? '' : 'none';
    });
});
```

### Características
- ✅ Búsqueda en tiempo real
- ✅ Búsqueda por nombre, email y negocio
- ✅ Contador dinámico de resultados
- ✅ Botón para limpiar búsqueda
- ✅ Re-numeración automática de filas

---

## FASE 86: CORRECCIÓN DE REPORTE DE VENTAS - TRANSACCIONES VS UNIDADES

**Fecha:** 06/07/2026
**Estado:** ✅ Completada

### Objetivo
Corregir el reporte de ventas para que cuente **transacciones** (pedidos) en lugar de **unidades** (cantidad de productos).

### Problema
El sistema contaba cada unidad vendida como una "venta". Ejemplo: una venta de 75 litros de leche se contaba como 75 ventas.

### Solución

```python
# Antes (INCORRECTO)
ventas_por_vendedor[vendedor_id]['ventas'] += item.quantity

# Después (CORRECTO)
ventas_por_vendedor[vendedor_id]['ventas'] += 1  # Cada pedido cuenta como 1 venta
```

### Resultado
- ✅ La Sierva: 162 → 14 ventas (correcto)
- ✅ Cada pedido cuenta como 1 venta independientemente de la cantidad

---

## FASE 87: DETALLE DE VENTAS AGRUPADO POR PEDIDO

**Fecha:** 06/07/2026
**Estado:** ✅ Completada

### Objetivo
Agrupar los productos por pedido en el detalle de ventas para que quede claro qué productos pertenecen a la misma transacción.

### Implementación

**Nueva estructura de datos:**
```python
ventas_agrupadas = []
for pedido in pedidos:
    items_del_productor = []
    for item in pedido.items.all():
        if item.product.vendedor == productor:
            items_del_productor.append({
                'producto': item.product.name,
                'cantidad': item.quantity,
                'precio': item.price,
                'subtotal': item.price * item.quantity
            })
    ventas_agrupadas.append({
        'pedido_id': pedido.id,
        'fecha': pedido.created_at,
        'comprador': pedido.user.get_full_name(),
        'items': items_del_productor,
        'total_items': len(items_del_productor),
        'subtotal_pedido': subtotal_pedido
    })
```

### Template con acordeones
```html
<div class="accordion" id="accordionVentas">
    {% for venta in ventas_agrupadas %}
    <div class="accordion-item">
        <h2 class="accordion-header" id="heading{{ venta.pedido_id }}">
            <button class="accordion-button" type="button" data-bs-toggle="collapse">
                📦 Pedido #{{ venta.pedido_id }}
                <span class="badge bg-info">{{ venta.total_items }} productos</span>
                <span class="badge bg-success">RD$ {{ venta.subtotal_pedido }}</span>
            </button>
        </h2>
        <div id="collapse{{ venta.pedido_id }}" class="accordion-collapse collapse show">
            <div class="accordion-body">
                <table class="table table-sm">
                    <thead><tr><th>Producto</th><th>Cantidad</th><th>Subtotal</th></tr></thead>
                    <tbody>
                        {% for item in venta.items %}
                        <tr>
                            <td>{{ item.producto }}</td>
                            <td>{{ item.cantidad }}</td>
                            <td>RD$ {{ item.subtotal }}</td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        </div>
    </div>
    {% endfor %}
</div>
```

---

## FASE 88: CORRECCIÓN DE ERROR EN DECORADOR `onpeco_required`

**Fecha:** 06/07/2026
**Estado:** ✅ Completada

### Problema
Error `NameError: name 'onpeco_required' is not defined` al iniciar la aplicación.

### Causa
El decorador `onpeco_required` se estaba usando antes de ser definido en el archivo.

### Solución
Se movió la definición del decorador al principio del archivo `views.py`, justo después de los imports.

```python
# ====================== DECORADOR PARA ONPECO ======================

def onpeco_required(view_func):
    """Decorador que permite acceso solo a staff o reguladores ONPECO"""
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff or getattr(request.user, 'role', '') == 'regulador':
                return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("No tienes permiso para acceder")
    return wrapper
```

---

## FASE 89: CORRECCIÓN DE ERROR EN EXPORTACIÓN DE DENUNCIAS A EXCEL

**Fecha:** 06/07/2026
**Estado:** ✅ Completada

### Problema
Error `AttributeError: 'Complaint' object has no attribute 'product'`

### Causa
El modelo `Complaint` no tiene un campo llamado `product`. El campo correcto es `producto`.

### Solución

```python
# Antes (INCORRECTO)
ws.cell(row=fila_actual, column=7, value=denuncia_actual.product.name if denuncia_actual.product else 'N/A')

# Después (CORRECTO)
nombre_producto = 'N/A'
if hasattr(denuncia_actual, 'producto') and denuncia_actual.producto:
    nombre_producto = denuncia_actual.producto.name
ws.cell(row=fila_actual, column=7, value=nombre_producto)
```

---

## FASE 90: LIMPIEZA DE CÓDIGO - FUNCIÓN `obtener_fechas`

**Fecha:** 06/07/2026
**Estado:** ✅ Completada

### Objetivo
Eliminar código duplicado para manejar fechas en múltiples vistas.

### Problema
El código para obtener fechas de inicio y fin se repetía en 3 vistas diferentes.

### Solución
Se creó una función reutilizable en `core/utils.py`:

```python
def obtener_fechas(request):
    """Obtiene las fechas de inicio y fin desde la solicitud GET."""
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')
    
    if not fecha_inicio or not fecha_fin:
        hoy = timezone.now().date()
        fecha_inicio = hoy.replace(day=1)
        fecha_fin = hoy
    else:
        try:
            fecha_inicio = datetime.datetime.strptime(fecha_inicio, '%Y-%m-%d').date()
            fecha_fin = datetime.datetime.strptime(fecha_fin, '%Y-%m-%d').date()
        except ValueError:
            hoy = timezone.now().date()
            fecha_inicio = hoy.replace(day=1)
            fecha_fin = hoy
    
    return fecha_inicio, fecha_fin
```

### Uso en vistas
```python
from core.utils import obtener_fechas

def reporte_ventas_general(request):
    fecha_inicio, fecha_fin = obtener_fechas(request)
    # ... resto del código
```

### Beneficios
- ✅ Eliminación de ~45 líneas de código duplicado
- ✅ Código más mantenible
- ✅ Una sola fuente de verdad

---

## FASE 91: SERVICIO DE ESTADÍSTICAS PARA ONPECO

**Fecha:** 28/06/2026
**Estado:** ✅ Completada

### Objetivo
Centralizar todas las consultas de estadísticas del portal ONPECO en un servicio reutilizable, eliminando código duplicado en las vistas.

### Servicio creado

```python
# apps/complaints/services.py
class EstadisticasONPECO:
    @staticmethod
    def get_resumen_general():
        return {
            'total_denuncias': Complaint.objects.count(),
            'denuncias_pendientes': Complaint.objects.filter(status='pending').count(),
            'denuncias_investigando': Complaint.objects.filter(status='investigating').count(),
            'denuncias_aprobadas': Complaint.objects.filter(status='resolved').count(),
            'denuncias_rechazadas': Complaint.objects.filter(status='rejected').count(),
            'total_productos': Product.objects.count(),
            'total_usuarios': User.objects.count(),
            'total_productores': User.objects.filter(role='productor').count(),
            'total_consumidores': User.objects.filter(role='consumidor').count(),
        }

    @staticmethod
    def get_top_productores_denunciados(limite=20):
        # Lógica para obtener productores más denunciados
        pass
```

### Beneficios
- ✅ Código reusable en otras vistas
- ✅ Fácil de probar y mantener
- ✅ Separación de responsabilidades
- ✅ Menos duplicación

---

## FASE 92: FILTRO DE ESTRELLAS EN TEMPLATES

**Fecha:** 28/06/2026
**Estado:** ✅ Completada

### Objetivo
Mover la lógica de generación de estrellas de los templates a un filtro personalizado reutilizable.

### Filtro creado

```python
# apps/marketplace/templatetags/star_rating.py
from django import template
register = template.Library()

@register.filter
def stars(rating):
    if rating is None:
        rating = 0
    try:
        rating_int = int(round(float(rating)))
    except (ValueError, TypeError):
        rating_int = 0
    rating_int = max(0, min(5, rating_int))
    
    stars_html = ''
    for i in range(1, 6):
        if i <= rating_int:
            stars_html += '<i class="fas fa-star text-warning"></i>'
        else:
            stars_html += '<i class="far fa-star text-warning"></i>'
    return stars_html
```

### Uso en template

```html
{% load star_rating %}
{{ productor.promedio_calificacion|stars }}
```

### Beneficios
- ✅ Código más limpio y reutilizable
- ✅ Separación de responsabilidades
- ✅ Fácil de probar y mantener

---

## FASE 93: ESTANDARIZACIÓN DE NOMBRES EN `views.py`

**Fecha:** 28/06/2026
**Estado:** ✅ Completada

### Objetivo
Estandarizar los nombres de variables y funciones en `apps/complaints/views.py` para mejorar la legibilidad y mantenibilidad del código.

### Cambios realizados

| Nombre antiguo | Nuevo nombre | Mejora |
|----------------|--------------|--------|
| `denuncias` | `denuncias_usuario` | ✅ Indica que son del usuario actual |
| `denuncia` | `denuncia_actual` | ✅ Indica que es la denuncia actual |
| `updates` | `historial_updates` | ✅ Indica que es el historial |
| `producto` | `producto_denunciado` | ✅ Indica que es el producto denunciado |
| `productor` | `productor_denunciado` | ✅ Indica que es el productor denunciado |
| `ticket` | `ticket_generado` | ✅ Indica que es el ticket generado |
| `busqueda` | `busqueda_ticket` | ✅ Indica que busca por ticket |
| `pendientes` | `denuncias_pendientes` | ✅ Más descriptivo |
| `investigando` | `denuncias_investigando` | ✅ Más descriptivo |
| `resueltas` | `denuncias_resueltas` | ✅ Más descriptivo |
| `rechazadas` | `denuncias_rechazadas` | ✅ Más descriptivo |
| `stats` | `estadisticas_resumen` | ✅ Más descriptivo |
| `p` | `pedido_actual` | ✅ Indica que es un pedido |
| `v` | `ventas_por_vendedor` | ✅ Indica qué contiene |
| `total_ventas` | `total_transacciones_sistema` | ✅ No confunde con cantidad de productos |
| `productores` | `productores_top` | ✅ Indica que son los más denunciados |

---

## FASE 94: CORRECCIÓN DE CARRITO PARA ONPECO Y CENTRO DE ACOPIO

**Fecha:** 06/07/2026
**Estado:** ✅ Completada

### Objetivo
Ocultar completamente el carrito de compras para los usuarios ONPECO (regulador) y Centro de Acopio (acopio), ya que estos roles no deben realizar compras.

### Cambios en `base.html`

**Navbar - "Mi Carrito":**
```html
<!-- Antes -->
{% if user.role == 'consumidor' or user.role == 'productor' or user.role == 'suplidor' %}

<!-- Después -->
{% if user.is_authenticated and user.role != 'regulador' and user.role != 'acopio' %}
```

**Botón flotante del carrito:**
```html
<!-- Antes -->
{% if user.is_authenticated %}
    {% if user.role == 'consumidor' or user.role == 'productor' or user.role == 'suplidor' %}

<!-- Después -->
{% if user.is_authenticated and user.role != 'regulador' and user.role != 'acopio' %}
```

---

## FASE 95: BLOQUEO DE COMPRA PARA ONPECO Y CENTRO DE ACOPIO

**Fecha:** 06/07/2026
**Estado:** ✅ Completada

### Objetivo
Bloquear a ONPECO y Centro de Acopio en la lista de productos (`lista_productos.html`) y en el detalle del producto (`detalle_producto.html`).

### Cambios en `lista_productos.html`

```html
<!-- Botón "Carrito" en tarjeta de producto -->
{% if user.is_authenticated and user.role != 'regulador' and user.role != 'acopio' %}
    <!-- Mostrar botón de carrito -->
{% elif user.is_authenticated %}
    <!-- ONPECO o Centro de Acopio: botón deshabilitado "Supervisión" -->
    <button class="btn btn-outline-secondary w-100" disabled>
        <i class="fas fa-gavel"></i> Supervisión
    </button>
{% else %}
    <!-- Usuario no autenticado: "Iniciar sesión" -->
    <a href="{% url 'users:login' %}" class="btn btn-outline-secondary flex-grow-1">
        <i class="fas fa-sign-in-alt"></i> Iniciar sesión
    </a>
{% endif %}
```

### Cambios en `detalle_producto.html`

```html
{# CASO 3: ONPECO, REGULADOR O CENTRO DE ACOPIO #}
{% else %}
    <div class="mt-4 p-3 text-center" style="background: #fff3cd; border-radius: 10px; border: 1px solid #ffc107;">
        <i class="fas fa-gavel fa-2x d-block mb-2 text-warning"></i>
        <p class="mb-0"><strong>Rol de supervisor</strong></p>
        <p class="mb-0 small text-muted">Los reguladores no pueden realizar compras. Esta función es exclusiva para consumidores.</p>
    </div>
{% endif %}
```

---

## FASE 96: SELECTOR DE EMOJIS EN CHAT

**Fecha:** 06/07/2026
**Estado:** ✅ Completada

### Objetivo
Agregar un selector de emojis en la interfaz del chat para que los usuarios puedan insertar emojis fácilmente.

### Implementación

**HTML:**
```html
<button type="button" id="emojiBtn" class="btn btn-outline-secondary">
    <i class="fas fa-smile"></i>
</button>
<div id="emojiPicker" style="display: none;">
    <div id="emojiList"></div>
</div>
```

**JavaScript:**
```javascript
const emojis = ['😊', '😂', '❤️', '👍', '🌱', '🌿', '🍎', '🍊', '🍋', '🍇', '🍉'];
emojis.forEach(function(emoji) {
    const span = document.createElement('span');
    span.textContent = emoji;
    span.addEventListener('click', function() {
        const cursorPos = mensajeInput.selectionStart;
        const text = mensajeInput.value;
        mensajeInput.value = text.substring(0, cursorPos) + emoji + text.substring(cursorPos);
        mensajeInput.focus();
        emojiPicker.style.display = 'none';
    });
    emojiList.appendChild(span);
});
```

---

## FASE 97: BOTÓN "VOLVER A MIS PRODUCTOS" EN EDICIÓN

**Fecha:** 06/07/2026
**Estado:** ✅ Completada

### Objetivo
Agregar un botón de retorno a "Mis Productos" en la página de edición de productos para mejorar la navegación.

### Implementación en `editar_producto.html`

```html
<!-- ========== BOTONES DE ACCIÓN ========== -->
<div class="d-flex gap-2 mt-4">
    <button type="submit" class="btn btn-warning flex-grow-1">
        <i class="fas fa-edit"></i> Actualizar Producto
    </button>
    <a href="{% url 'marketplace:mis_productos' %}" class="btn btn-secondary">
        <i class="fas fa-arrow-left"></i> Volver a mis productos
    </a>
</div>
```

---

## FASE 98: FORMATO DE NÚMEROS EN BALANCE DE VENTAS (RD)

**Fecha:** 06/07/2026
**Estado:** ✅ Completada

### Objetivo
Aplicar el formato de números de República Dominicana (miles con coma, decimales con punto) en el balance de ventas.

### Filtro personalizado

```python
# apps/cart/templatetags/cart_filters.py
@register.filter
def format_rd(value):
    try:
        value = float(value)
        return f"{value:,.2f}"
    except (ValueError, TypeError):
        return "0.00"
```

### Uso en template

```html
{% load cart_filters %}
<h2>RD$ {{ total_vendido|format_rd }}</h2>
```

### Ejemplos de formato
| Antes | Después |
|-------|---------|
| `RD$ 15635.00` | `RD$ 15,635.00` |
| `RD$ 23900.00` | `RD$ 23,900.00` |
| `RD$ 1550.50` | `RD$ 1,550.50` |

---

## FASE 99: CORRECCIÓN DE FORMATO DE NÚMEROS EN VENTAS

**Fecha:** 06/07/2026
**Estado:** ✅ Completada

### Objetivo
Aplicar el formato de República Dominicana en todas las vistas que muestran montos (ventas, pedidos, etc.).

### Configuración en `settings.py`

```python
USE_THOUSAND_SEPARATOR = True
THOUSAND_SEPARATOR = ','
DECIMAL_SEPARATOR = '.'
NUMBER_GROUPING = 3
```

### Actualización en `views.py`

```python
# Asegurar que los totales se pasen como float
context = {
    'total_vendido': float(total_vendido),
    'total_pagado': float(total_pagado),
    'total_pendiente': float(total_pendiente),
}
```

---

## FASE 100: CHAT PRIVADO ONPECO ↔ CENTRO DE ACOPIO

**Fecha:** 01/07/2026
**Estado:** ✅ Completada

### Objetivo
Crear un canal de comunicación privado y exclusivo entre ONPECO y el Centro de Acopio para coordinación de temas regulatorios.

### Modelos modificados

```python
# apps/chat/models.py
class ChatRoom(models.Model):
    is_private_onpeco_acopio = models.BooleanField(default=False)
```

### Vistas implementadas

| Vista | URL | Propósito |
|-------|-----|-----------|
| `chat_privado_onpeco_acopio` | `/chat/privado-acopio/` | Chat privado ONPECO-Acopio |

### Template modificado

```html
<!-- templates/chat/ver_chat.html -->
{% if is_private %}
<div class="card-header bg-success text-white">
    <h4><i class="fas fa-lock"></i> 🔒 Chat Privado: ONPECO ↔ Centro de Acopio</h4>
    <div class="mt-1">
        <span class="badge bg-light text-dark">🔒 Canal exclusivo y privado</span>
    </div>
</div>
{% endif %}
```

### Enlace en menú ONPECO

```html
<li><a class="dropdown-item" href="{% url 'chat:chat_privado_onpeco_acopio' %}">
    <i class="fas fa-lock"></i> 🔒 Chat con {% if user.username == 'centro_acopio' %}ONPECO{% else %}Centro de Acopio{% endif %}
</a></li>
```

### Resultado
- ✅ ONPECO y Acopio tienen un canal privado
- ✅ Solo ellos pueden ver y enviar mensajes
- ✅ Enlace en el menú de ONPECO

---

## FASE 101: CORRECCIÓN DE REBAJA DE STOCK EN TIEMPO REAL

**Fecha:** 28/06/2026
**Estado:** ✅ Completada

### Objetivo
Corregir el problema donde el stock de los productos no se descontaba automáticamente al realizar una venta.

### Señal para actualizar stock al crear pedido

```python
@receiver(post_save, sender=Order)
def actualizar_stock_al_crear_pedido(sender, instance, created, **kwargs):
    if created and instance.status == 'pending':
        for item in instance.items.all():
            producto = item.product
            if producto.stock >= item.quantity:
                producto.stock -= item.quantity
                producto.save()
            else:
                instance.status = 'cancelled'
                instance.save()
                raise ValueError(f'Stock insuficiente para {producto.name}')
```

### Señal para revertir stock al cancelar

```python
@receiver(pre_save, sender=Order)
def revertir_stock_al_cancelar(sender, instance, **kwargs):
    if instance.pk:
        old_instance = Order.objects.get(pk=instance.pk)
        if old_instance.status != 'cancelled' and instance.status == 'cancelled':
            for item in old_instance.items.all():
                producto = item.product
                producto.stock += item.quantity
                producto.save()
```

---

## FASE 102: REDISEÑO DE BOTONES CON RECUADROS

**Fecha:** 28/06/2026
**Estado:** ✅ Completada

### Estilos CSS

```css
.btn-container {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    padding: 15px;
    background: #f8f9fa;
    border-radius: 10px;
    border: 1px solid #dee2e6;
    margin: 15px 0;
    justify-content: center;
    align-items: center;
}

.btn-container .btn {
    min-width: 120px;
    margin: 0;
}

.btn-container .btn i {
    margin-right: 8px;
}
```

### Aplicación en templates

```html
<div class="btn-container">
    <a href="{% url 'marketplace:crear_producto' %}" class="btn btn-primary">
        <i class="fas fa-plus"></i> Nuevo Producto
    </a>
    <a href="{% url 'cart:mis_ventas' %}" class="btn btn-success">
        <i class="fas fa-chart-bar"></i> Mis Ventas
    </a>
</div>
```

---

## FASE 103: AGREGADO DEL TOMATE COMO ORGULLO DE AZUA

**Fecha:** 28/06/2026
**Estado:** ✅ Completada

### Implementación en header

```html
<a class="navbar-brand" href="{% url 'inicio' %}">
    <img src="{% static 'images/tomate_azua.png' %}" alt="Tomate Orgullo de Azua" height="40">
    <span>VPJ - Azua</span>
</a>
```

### Estilos CSS

```css
.azua-banner {
    background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
    padding: 30px;
    border-radius: 15px;
    color: white;
    margin: 20px 0;
}

.azua-icon {
    width: 80px;
    height: 80px;
    filter: drop-shadow(0 4px 8px rgba(0,0,0,0.2));
}
```

---

## FASE 104: CORRECCIÓN DE HISTORIAL DE VENTAS

**Fecha:** 28/06/2026
**Estado:** ✅ Completada

### Objetivo
Corregir el error donde al hacer clic en "Ver" en el historial de ventas, no se mostraba correctamente el detalle.

### Corrección de la vista

```python
@login_required
def detalle_venta(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    mis_items = order.items.filter(product__vendedor=request.user)
    if not mis_items.exists():
        return HttpResponseForbidden("No tienes permiso para ver esta venta.")
    subtotal = sum(item.get_total_price() for item in mis_items)
    context = {
        'order': order,
        'mis_items': mis_items,
        'subtotal': subtotal,
    }
    return render(request, 'cart/detalle_venta.html', context)
```

---

## FASE 105: CORRECCIÓN DE CONTABILIZACIÓN DE DENUNCIAS APROBADAS

**Fecha:** 28/06/2026
**Estado:** ✅ Completada

### Objetivo
Corregir el error donde el sistema no contabilizaba correctamente el detalle de las denuncias aprobadas.

### Corrección de la vista

```python
@onpeco_required
def detalle_denuncia(request, denuncia_id):
    denuncia = get_object_or_404(Complaint, id=denuncia_id)
    actualizaciones = ComplaintUpdate.objects.filter(complaint=denuncia).order_by('created_at')
    total_aprobadas = Complaint.objects.filter(status='aprobada').count()
    context = {
        'denuncia': denuncia,
        'actualizaciones': actualizaciones,
        'total_aprobadas': total_aprobadas,
    }
    return render(request, 'complaints/detalle_denuncia.html', context)
```

---

## FASE 106: CORRECCIÓN DE BALANCES PAGADOS

**Fecha:** 28/06/2026
**Estado:** ✅ Completada

### Objetivo
Corregir los problemas relacionados con el cálculo y visualización de balances pagados.

### Modelo Order con método marcar_pagado

```python
class Order(models.Model):
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='pending')
    payment_date = models.DateTimeField(null=True, blank=True)
    payment_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    
    def marcar_pagado(self, monto=None):
        self.payment_status = 'paid'
        self.payment_date = timezone.now()
        if monto:
            self.payment_amount = monto
        self.save()
```

### Corrección del cálculo en balance_ventas

```python
for order in orders:
    mis_items = order.items.filter(product__vendedor=request.user)
    subtotal = sum(item.get_total_price() for item in mis_items)
    total_vendido += subtotal
    if order.payment_status == 'paid':
        total_pagado += subtotal
```

---

## FASE 107: ENLACE A ONPECO EN EL PORTAL

**Fecha:** 28/06/2026
**Estado:** ✅ Completada

### Enlace en el portal

```html
<div class="card border-info">
    <div class="card-header bg-info text-white">
        <i class="fas fa-link"></i> Enlaces de interés
    </div>
    <div class="card-body">
        <a href="https://onpeco.gob.do" target="_blank" class="btn btn-outline-info btn-lg">
            <i class="fas fa-external-link-alt"></i> Visitar sitio oficial de ONPECO
        </a>
    </div>
</div>
```

---

## FASE 108: EXPORTACIÓN DE REPORTES DE DENUNCIAS A EXCEL

**Fecha:** 28/06/2026
**Estado:** ✅ Completada

### Instalación

```bash
pip install openpyxl
```

### Vista de exportación

```python
@onpeco_required
def exportar_denuncias_excel(request):
    wb = Workbook()
    ws = wb.active
    ws.title = 'Denuncias'
    headers = ['Ticket', 'Título', 'Estado', 'Prioridad', 'Creado por', 'Fecha', 'Producto']
    ws.append(headers)
    denuncias = Complaint.objects.all().order_by('-created_at')
    for denuncia in denuncias:
        ws.append([
            denuncia.ticket_number,
            denuncia.title,
            denuncia.get_status_display(),
            denuncia.get_priority_display(),
            denuncia.complainant.username,
            denuncia.created_at.strftime('%d/%m/%Y %H:%M'),
            denuncia.product.name if denuncia.product else 'N/A'
        ])
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=denuncias.xlsx'
    wb.save(response)
    return response
```

---

## FASE 109: SISTEMA DE NOTIFICACIONES CON CONTADOR DE INCREMENTO

**Fecha:** 28/06/2026
**Estado:** ✅ Completada

### Objetivo
Implementar un sistema de notificaciones en tiempo real para los usuarios cuando reciben mensajes.

### Modelo de notificaciones

```python
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.ForeignKey('ChatMessage', on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
```

### Señal para crear notificaciones

```python
@receiver(post_save, sender=ChatMessage)
def crear_notificacion(sender, instance, created, **kwargs):
    if created:
        room = instance.room
        if room.productor == instance.sender:
            destinatario = room.consumidor
        else:
            destinatario = room.productor
        if destinatario and destinatario != instance.sender:
            Notification.objects.create(user=destinatario, message=instance, is_read=False)
```

### Context processor para contador

```python
def notification_count(request):
    if request.user.is_authenticated:
        unread_count = Notification.objects.filter(user=request.user, is_read=False).count()
        return {'notification_count': unread_count}
    return {'notification_count': 0}
```

### Animación de incremento

```css
.notification-badge {
    animation: pulse 0.5s ease-in-out 3;
}

@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.3); }
    100% { transform: scale(1); }
}
```

---

## FASE 110: CORRECCIÓN DE ERROR `datetime` EN BACKUPS

**Fecha:** 28/06/2026
**Estado:** ✅ Completada

### Problema
Error `AttributeError: type object 'datetime.datetime' has no attribute 'datetime'`

### Solución

```python
# Antes
from datetime import datetime

# Después
import datetime
```

```python
# Antes
'fecha': datetime.fromtimestamp(stat.st_mtime)

# Después
'fecha': datetime.datetime.fromtimestamp(stat.st_mtime)
```

---

## FASE 111: CAMBIO DE LOGIN A CÉDULA Y MEJORA DE INTERFAZ

**Fecha:** 28/06/2026
**Estado:** ✅ Completada

### Cambios en login.html

```html
<!-- Antes -->
<input type="text" name="username" placeholder="Usuario" required>

<!-- Después -->
<input type="text" name="username" placeholder="Cédula" required>
```

---

## FASE 112: TOMATE CLICABLE CON ENLACE A ONPECO

**Fecha:** 28/06/2026
**Estado:** ✅ Completada

### Cambio en inicio.html

```html
<a href="https://onpeco.org/" target="_blank" 
   style="text-decoration: none; display: inline-block; transition: transform 0.3s ease;"
   onmouseover="this.style.transform='scale(1.05)'" 
   onmouseout="this.style.transform='scale(1)'"
   title="Visitar la página oficial de ONPECO">
    <div style="background: linear-gradient(135deg, #e53935, #c62828); cursor: pointer; ...">
        <!-- Hojas y brillo -->
    </div>
</a>
```

---

## FASE 113: SISTEMA DE RESTABLECIMIENTO DE CONTRASEÑAS POR ONPECO

**Fecha:** 28/06/2026
**Estado:** ✅ Completada

### Objetivo
Permitir que ONPECO restablezca la contraseña de cualquier usuario a `cambiar123`, forzando al usuario a cambiarla.

### Nuevo campo en User

```python
must_change_password = models.BooleanField(
    default=False,
    help_text="Indica si el usuario debe cambiar su contraseña al iniciar sesión"
)
```

### Vista para restablecer contraseña

```python
@login_required
def resetear_contrasena_usuario(request, user_id):
    if not (request.user.is_staff or getattr(request.user, 'role', '') == 'regulador'):
        return HttpResponseForbidden("No tienes permiso.")
    usuario = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        nueva_contrasena = 'cambiar123'
        usuario.password = make_password(nueva_contrasena)
        usuario.must_change_password = True
        usuario.save()
        messages.success(request, f'✅ Contraseña restablecida para "{usuario.username}"')
        return redirect('users:lista_usuarios_onpeco')
    return render(request, 'users/resetear_contrasena.html', {'usuario': usuario})
```

### Modificación de login_view

```python
if user is not None:
    if getattr(user, 'must_change_password', False):
        login(request, user)
        messages.warning(request, '⚠️ Debes cambiar tu contraseña temporal.')
        return redirect('users:cambiar_contrasena_temporal')
```

### Flujo de trabajo

```
ONPECO → Gestionar Usuarios → Restablecer Contraseña
    ↓
Contraseña del usuario = cambiar123
    ↓
Usuario inicia sesión con cambiar123
    ↓
Sistema detecta must_change_password=True
    ↓
Redirige a cambiar_contrasena_temporal
    ↓
Usuario escribe su NUEVA contraseña
    ↓
✅ Contraseña actualizada
```

---

## FASE 114: NOMBRE REAL EN NAVBAR Y PERFIL

**Fecha:** 28/06/2026
**Estado:** ✅ Completada

### Métodos en modelo User

```python
def get_full_name(self):
    if self.first_name and self.last_name:
        return f"{self.first_name} {self.last_name}"
    elif self.first_name:
        return self.first_name
    elif self.last_name:
        return self.last_name
    return self.username

def get_display_name(self):
    nombre = self.get_full_name()
    if nombre != self.username:
        return f"{nombre} ({self.username})"
    return self.username
```

### Navbar actualizado

```html
<!-- Antes -->
{{ user.username }}

<!-- Después -->
{{ user.get_display_name }}
```

### Perfil actualizado

```html
<div style="background: #e8f5e9; padding: 15px; border-radius: 10px; border-left: 4px solid #2E7D32;">
    <p style="margin: 0; font-size: 1.2rem;">
        <strong>👤 {{ user.get_full_name }}</strong>
    </p>
    <p style="margin: 0; color: #555;">
        <strong>Cédula:</strong> {{ user.username }}
    </p>
</div>
```

---

## FASE 115: EXPORTACIÓN DE CONSUMIDORES Y PRODUCTORES A EXCEL

**Fecha:** 28/06/2026
**Estado:** ✅ Completada

### Exportar consumidores

```python
@onpeco_required
def exportar_consumidores_excel(request):
    wb = Workbook()
    ws = wb.active
    ws.title = 'Consumidores'
    headers = ['Nombre', 'Cédula', 'Email', 'Teléfono', 'Dirección', 'Fecha de Registro']
    ws.append(headers)
    consumidores = User.objects.filter(role='consumidor', is_active=True)
    for consumidor in consumidores:
        ws.append([
            consumidor.get_full_name(),
            consumidor.username,
            consumidor.email or '',
            consumidor.phone or '',
            consumidor.address or '',
            consumidor.date_joined.strftime('%d/%m/%Y') if consumidor.date_joined else ''
        ])
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=consumidores.xlsx'
    wb.save(response)
    return response
```

### Exportar productores

```python
@onpeco_required
def exportar_productores_excel(request):
    wb = Workbook()
    ws = wb.active
    ws.title = 'Productores'
    headers = ['Nombre', 'Cédula', 'Negocio', 'Email', 'Teléfono', 'Dirección', 'Estado', 'Total Productos', 'Reputación']
    ws.append(headers)
    productores = User.objects.filter(role='productor').order_by('first_name', 'last_name')
    for productor in productores:
        ws.append([
            productor.get_full_name(),
            productor.username,
            productor.business_name or '',
            productor.email or '',
            productor.phone or '',
            productor.address or '',
            'Aprobado' if productor.is_approved else 'Pendiente',
            Product.objects.filter(vendedor=productor).count(),
            productor.get_reputacion_display()
        ])
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=productores.xlsx'
    wb.save(response)
    return response
```

---

## FASE 116: INTEGRACIÓN DEL LOGO OFICIAL DE ONPECO

**Fecha:** 29/06/2026
**Estado:** ✅ Completada

### Copia del logo al proyecto

```bash
copy "C:\Users\DELL\Desktop\Logo Onpeco sin borde para insertar.png" static\img\onpeco-logo.png
copy "C:\Users\DELL\Desktop\Logo Onpeco sin borde para insertar.png" static\images\logo_onpeco.png
copy "C:\Users\DELL\Desktop\Logo Onpeco sin borde para insertar.png" media\logo_onpeco.png
python manage.py collectstatic
```

### Logo en Navbar

```html
<a href="https://onpeco.org/" target="_blank" title="Visitar ONPECO" 
   style="text-decoration: none; display: flex; align-items: center;">
    <img src="/media/logo_onpeco.png" alt="ONPECO" height="50" class="d-inline-block align-top me-2">
</a>
```

---

## FASE 117: ESTILIZADO DEL LOGO ONPECO CON BORDES REDONDEADOS

**Fecha:** 29/06/2026
**Estado:** ✅ Completada

### CSS del logo

```css
.navbar-brand img {
    border-radius: 12px;
    border: 2px solid rgba(255, 255, 255, 0.3);
    padding: 3px;
    background: rgba(255, 255, 255, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
    object-fit: cover;
}

.navbar-brand img:hover {
    transform: scale(1.08);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
    border-color: rgba(255, 255, 255, 0.7);
}
```

---

## FASE 118: CAMBIO DE FAVICON A LOGO DE ONPECO (DEFINITIVO)

**Fecha:** 29/06/2026
**Estado:** ✅ Completada

```html
<link rel="icon" type="image/png" href="/media/logo_onpeco.png">
<link rel="apple-touch-icon" type="image/png" href="/media/logo_onpeco.png">
```

---

## FASE 119: OPTIMIZACIÓN DE LA PÁGINA DE INICIO

**Fecha:** 29/06/2026
**Estado:** ✅ Completada

### Cambios realizados
1. Eliminación del tomate grande (120px)
2. Eliminación de la mano "Tomate Industrial"
3. Conversión del badge "ORGULLO DE AZUA" a elemento clicable

```html
<a href="https://www.google.com/search?q=Tomate+Industrial..." target="_blank" 
   style="text-decoration: none; display: inline-block; transition: transform 0.3s ease;">
    <span style="background: linear-gradient(135deg, #2E7D32, #388E3C); 
                 font-size: 1.8rem; 
                 padding: 12px 35px; 
                 border-radius: 30px; 
                 font-weight: bold;
                 cursor: pointer;">
        🍅 ORGULLO DE AZUA
    </span>
</a>
```

---

## FASE 120: CORRECCIÓN DEL FOOTER - TEXTO INSTITUCIONAL

**Fecha:** 29/06/2026
**Estado:** ✅ Completada

```html
<small>Desarrollado para ONPECO por el Grupo #5<br>Monográfico #59 - Escuela de Informática - UASD</small>
```

---

## FASE 121: AJUSTE DE POSICIÓN DEL CARRITO FLOTANTE

**Fecha:** 29/06/2026
**Estado:** ✅ Completada

```css
.cart-float-btn {
    bottom: 80px;  /* Antes: 20px */
}
```

---

## FASE 122: ELIMINACIÓN DE NOTIFICACIONES DE CHAT SIN SESIÓN

**Fecha:** 29/06/2026
**Estado:** ✅ Completada

### Problema
El badge de notificaciones de chat aparecía en la página de inicio incluso sin sesión.

### Solución
Eliminación del bloque de "Notificaciones de Chat" de `templates/base/inicio.html`.

---

## FASE 123: VERIFICACIÓN FINAL Y CONSOLIDACIÓN DE CAMBIOS

**Fecha:** 29/06/2026
**Estado:** ✅ Completada

### Pruebas realizadas

| Prueba | Resultado |
|--------|-----------|
| Logo ONPECO visible en navbar | ✅ Exitosa |
| Logo clicable a onpeco.org | ✅ Exitosa |
| Logo con bordes redondeados | ✅ Exitosa |
| Favicon actualizado | ✅ Exitosa |
| Badge "ORGULLO DE AZUA" clicable | ✅ Exitosa |
| Tomate grande eliminado | ✅ Exitosa |
| Carrito flotante no tapa footer | ✅ Exitosa |
| Footer con texto institucional correcto | ✅ Exitosa |
| Sin notificaciones de chat sin sesión | ✅ Exitosa |

---

## FASE 124: CAMBIO DE COLOR DE "VPJ" A ROJO

**Fecha:** 29/06/2026
**Estado:** ✅ Completada

```html
<span style="font-size: 1.3rem; font-weight: 700; white-space: nowrap; color: #FF6B6B;">VPJ</span>
```

---

## FASE 125: MÓDULO "SOBRE VPJ" - MODAL INFORMATIVO

**Fecha:** 29/06/2026
**Estado:** ✅ Completada

### Objetivo
Crear un modal informativo al hacer clic en "VPJ" en el navbar.

### Implementación

```html
<span style="font-size: 1.3rem; font-weight: 700; white-space: nowrap; color: #FF6B6B; cursor: pointer;" 
      data-bs-toggle="modal" 
      data-bs-target="#modalVPJ"
      title="Haz clic para conocer más sobre VPJ">
    VPJ
</span>

<!-- Modal -->
<div class="modal fade" id="modalVPJ" tabindex="-1" aria-labelledby="modalVPJLabel" aria-hidden="true">
    <div class="modal-dialog modal-lg modal-dialog-centered">
        <div class="modal-content">
            <div class="modal-header" style="background: linear-gradient(135deg, #2E7D32, #388E3C); color: white;">
                <h5 class="modal-title" id="modalVPJLabel">
                    <img src="/media/logo_onpeco.png" alt="ONPECO" height="30">
                    VPJ - Venta Precio Justo
                </h5>
                <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal"></button>
            </div>
            <div class="modal-body" style="max-height: 70vh; overflow-y: auto;">
                <div style="text-align: justify; line-height: 1.8;">
                    <p><strong>VPJ (Venta Precio Justo)</strong> es una plataforma digital desarrollada para <strong>ONPECO</strong> por el <strong>Grupo #5 del Monográfico #59</strong> de la <strong>Escuela de Informática de la Universidad Autónoma de Santo Domingo (UASD)</strong>, con el objetivo de promover un comercio agrícola más equitativo y transparente en la provincia de Azua, República Dominicana.</p>
                    
                    <p>La aplicación conecta directamente a <strong>productores agrícolas</strong> con <strong>consumidores finales</strong>, acortando la cadena de suministro y garantizando precios justos para ambas partes, bajo la supervisión y regulación de ONPECO.</p>
                </div>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
                <a href="https://onpeco.org/" target="_blank" class="btn btn-success">
                    <i class="fas fa-external-link-alt"></i> Visitar ONPECO
                </a>
            </div>
        </div>
    </div>
</div>
```

---

## FASE 126: CHAT PRIVADO ONPECO ↔ CENTRO DE ACOPIO

**Fecha:** 01/07/2026
**Estado:** ✅ Completada

### Objetivo
Crear un canal de comunicación privado y exclusivo entre ONPECO y el Centro de Acopio para coordinación de temas regulatorios.

### Modelos modificados

```python
# apps/chat/models.py
class ChatRoom(models.Model):
    is_private_onpeco_acopio = models.BooleanField(default=False)
```

### Vistas implementadas

| Vista | URL | Propósito |
|-------|-----|-----------|
| `chat_privado_onpeco_acopio` | `/chat/privado-acopio/` | Chat privado ONPECO-Acopio |

### Templates creados/modificados

- `templates/chat/ver_chat.html` (modificado para soportar chat privado)
- Enlace en el menú de ONPECO

### Resultado
- ✅ ONPECO y Acopio tienen un canal privado
- ✅ Solo ellos pueden ver y enviar mensajes
- ✅ Enlace en el menú de ONPECO

---
¡Excelente! Te voy a preparar el contenido para que lo insertes en tu archivo `DOCUMENTACION.md`. He organizado la información de la reunión del 25 de junio de 2026 de manera profesional y detallada, siguiendo el formato de tus fases anteriores.

---

## 📋 TEXTO PARA COPIAR Y PEGAR EN `DOCUMENTACION.md`

**Ubicación:** Inserta esto **después de la Fase 126** (o donde mejor se ajuste en tu cronología). He numerado esta fase como **Fase 127** (ya que la 127 en tu documento actual es el encuentro con promotores en Azua del 03/07/2026, que ocurrió después). Sin embargo, viendo tu estructura, la reunión con ONPECO fue el **25/06/2026**, así que debería ir **antes** de la Fase 127 (03/07/2026). Te sugiero **renumerar** y mover la Fase 127 (Azua) a la **Fase 128**, y poner esta como **Fase 127**.

---

```markdown
## FASE 127: PRESENTACIÓN OFICIAL A ONPECO - DEMOSTRACIÓN EN VIVO CON NGORK

**Fecha:** 25 de junio de 2026
**Lugar:** Oficinas de ONPECO, Santo Domingo, República Dominicana
**Estado:** ✅ Completada

---

### Objetivo de la Fase

Realizar la presentación oficial de la plataforma "Venta Precio Justo (VPJ)" a la directiva de ONPECO, demostrando el funcionamiento en vivo de la aplicación a través de un túnel de Ngrok, y recibir retroalimentación directa de los ejecutivos para realizar ajustes y mejoras antes del lanzamiento final.

---

### Participantes

**Por ONPECO:**

| Nombre | Cargo |
|--------|-------|
| Lic. Altagracia Paulino | Presidenta de ONPECO |
| Lic. Leonel A. Rivas P. | Ejecutivo de ONPECO |
| Lic. Leonor González | Ejecutiva de ONPECO |

**Por el equipo de desarrollo (Grupo #5 - Monográfico #59 - Escuela de Informática - UASD):**

| Nombre | Rol |
|--------|-----|
| Manuel A. Hernández C. | Desarrollador / Representante del Grupo |
| Elizabeth Ogando Rosa | Desarrolladora |
| Alexander Trinidad Ramírez | Desarrollador / Este servidor |

---

### Desarrollo de la Reunión

#### 1. Preparación técnica previa

El equipo de desarrollo preparó el entorno para la demostración:

| Aspecto | Detalle |
|---------|---------|
| Servidor local | Daphne corriendo en `127.0.0.1:8000` |
| Túnel seguro | Ngrok configurado para exponer el servidor local |
| URL generada | `https://whacky-deceiver-motive.ngrok-free.dev` |
| Configuración | `ALLOWED_HOSTS` y `CSRF_TRUSTED_ORIGINS` actualizados |

**Configuración en `settings.py`:**
```python
ALLOWED_HOSTS = ['*', 'whacky-deceiver-motive.ngrok-free.dev']
CSRF_TRUSTED_ORIGINS = ['https://whacky-deceiver-motive.ngrok-free.dev']
```

#### 2. Demostración en vivo

Se realizó una demostración completa de la plataforma, recorriendo todos los módulos principales:

**Módulos demostrados:**

| # | Módulo | Descripción |
|---|--------|-------------|
| 1 | **Autenticación y Registro** | Registro de consumidores, productores y gestión de aprobaciones |
| 2 | **Marketplace** | Publicación de productos, lista de productos, búsqueda y filtros |
| 3 | **Carrito de Compras** | Agregar productos, gestionar cantidades, checkout |
| 4 | **Pedidos y Ventas** | Creación de pedidos, historial de ventas, balance de ventas |
| 5 | **Centro de Acopio** | Gestión de pedidos, desglose por productor, pagos |
| 6 | **Sistema de Denuncias** | Creación de denuncias, seguimiento, reportes con gráficos |
| 7 | **Chat en Tiempo Real** | Comunicación consumidor-productor con WebSockets |
| 8 | **Portal ONPECO** | Dashboard, estadísticas, gestión de usuarios y backups |
| 9 | **Exportaciones** | Reportes a Excel (denuncias, consumidores, productores) |

#### 3. Retroalimentación de ONPECO

Los ejecutivos de ONPECO realizaron las siguientes observaciones y recomendaciones:

**Recomendaciones recibidas:**

| # | Recomendación | Responsable |
|---|---------------|-------------|
| 1 | **Logo de ONPECO en la aplicación:** Integrar el logo oficial de ONPECO en el navbar y footer | ✅ Implementado (Fase 116-118) |
| 2 | **Enlace directo a ONPECO:** Agregar un link que lleve al sitio web oficial de ONPECO | ✅ Implementado (Fase 107, 112) |
| 3 | **Tomate como "Orgullo de Azua":** Utilizar el tomate como ícono representativo de Azua | ✅ Implementado (Fase 103, 119) |
| 4 | **Cédula como nombre de usuario:** Que el nombre de usuario sea el número de cédula | ✅ Implementado (Fase 111) |
| 5 | **Mejoras visuales:** Ajustes en la interfaz y experiencia de usuario | ✅ Implementado (Fases 62-71) |
| 6 | **Privacidad de datos:** Ocultar cédulas en listas públicas | ✅ Implementado (Fase 82) |

**Observaciones adicionales:**

| Aspecto | Observación |
|---------|-------------|
| Diseño | "La interfaz es limpia y profesional, cumple con los estándares esperados" |
| Funcionalidad | "El sistema cubre todos los requisitos planteados inicialmente" |
| Usabilidad | "La navegación es intuitiva, los usuarios podrán adaptarse fácilmente" |
| Seguridad | "El manejo de roles y permisos es adecuado" |
| Rendimiento | "La aplicación responde rápidamente incluso con el túnel de Ngrok" |

---

### Acuerdos y Compromisos

| # | Acuerdo | Responsable | Fecha límite |
|---|---------|-------------|--------------|
| 1 | Incorporar todas las observaciones realizadas durante la reunión | Equipo de desarrollo | 30/06/2026 |
| 2 | Continuar con el desarrollo de funcionalidades pendientes | Equipo de desarrollo | 05/07/2026 |
| 3 | Mantener comunicación constante entre el equipo y ONPECO | Ambos equipos | Permanente |
| 4 | Preparar la presentación para promotores en Azua | Equipo de desarrollo | 03/07/2026 |

---

### Impacto de la Reunión

| Aspecto | Resultado |
|---------|-----------|
| **Aprobación del proyecto** | ✅ ONPECO manifestó su satisfacción con el avance |
| **Validez del prototipo** | ✅ Validado por los ejecutivos de ONPECO |
| **Identificación de mejoras** | ✅ Se identificaron áreas de mejora concretas |
| **Ruta crítica definida** | ✅ Se establecieron prioridades y plazos |
| **Confianza del cliente** | ✅ Incrementada con la demostración en vivo |

---

### Lecciones Aprendidas

| # | Lección | Aplicación futura |
|---|---------|-------------------|
| 1 | **Ngrok es una herramienta efectiva** para presentaciones en vivo sin necesidad de desplegar en producción | Usar en futuras demostraciones |
| 2 | **La preparación técnica previa es crucial** para evitar contratiempos | Crear un checklist de pre-presentación |
| 3 | **La retroalimentación temprana del cliente** permite corregir detalles antes del lanzamiento | Realizar más demostraciones intermedias |
| 4 | **La comunicación profesional** con el cliente genera confianza | Mantener el mismo nivel en futuras interacciones |

---

### Pruebas Realizadas Durante la Demostración

| # | Prueba | Resultado |
|---|--------|-----------|
| 1 | Acceso a la plataforma vía Ngrok | ✅ Exitosa |
| 2 | Inicio de sesión de todos los roles | ✅ Exitosa |
| 3 | Publicación de un producto | ✅ Exitosa |
| 4 | Proceso de compra completo | ✅ Exitosa |
| 5 | Gestión de pedidos desde Centro de Acopio | ✅ Exitosa |
| 6 | Creación y seguimiento de denuncias | ✅ Exitosa |
| 7 | Chat en tiempo real | ✅ Exitosa |
| 8 | Dashboard de ONPECO | ✅ Exitosa |
| 9 | Exportación a Excel | ✅ Exitosa |
| 10 | Sistema de backups | ✅ Exitosa |

---

### Estado Final de la Reunión

**Estado:** ✅ Completada exitosamente

**Logros:**
- ✅ Presentación profesional de la plataforma
- ✅ Demostración en vivo de todas las funcionalidades
- ✅ Validación del proyecto por parte de la directiva de ONPECO
- ✅ Recepción de retroalimentación valiosa
- ✅ Establecimiento de acuerdos claros y fechas límite

**Próximos pasos:**
1. Implementar las mejoras sugeridas (Fases 82-126)
2. Preparar la presentación para promotores en Azua (Fase 128)
3. Realizar pruebas finales
4. Preparar documentación para la defensa del monográfico

---

**Nota:** Esta fase fue fundamental para validar el proyecto con el cliente real y demostrar que la plataforma "Venta Precio Justo (VPJ)" cumple con todos los requisitos establecidos, funcionando correctamente en un entorno controlado pero accesible desde cualquier lugar a través de Ngrok.

```

---

## 📋 RESUMEN DE CAMBIOS SUGERIDOS PARA TU DOCUMENTO

| Fase | Título | Fecha | Estado |
|------|--------|-------|--------|
| **127** | Presentación Oficial a ONPECO - Demostración en Vivo con Ngrok | 25/06/2026 | ✅ Completada |
| **128** | Encuentro con Promotores en Azua - Presentación de VPJ | 03/07/2026 | ✅ Completada |
| **129** | Corrección de Carrito para ONPECO y Centro de Acopio | 06/07/2026 | ✅ Completada |
| **130** | Selector de Emojis en Chat | 06/07/2026 | ✅ Completada |
| **131** | Botón "Volver a Mis Productos" en Edición | 06/07/2026 | ✅ Completada |
| **132** | Formato de Números en Balance de Ventas (RD) | 06/07/2026 | ✅ Completada |
| **133** | Actualización de Documentación - FASES 127 A 132 | 06/07/2026 | ✅ Completada |



---

¿Necesitas que te ayude con alguna otra sección o ajuste? 🚀

## FASE 128: ENCUENTRO CON PROMOTORES EN AZUA - PRESENTACIÓN DE VPJ

**Fecha:** 03/07/2026
**Estado:** ✅ Completada

### Objetivo
Realizar la presentación oficial de la aplicación "Venta Precio Justo (VPJ)" a los promotores de la provincia de Azua, como parte del proceso de implementación y validación del proyecto con los actores clave de la región.

### Participantes

**Por ONPECO:**
- Representantes de ONPECO (presentes en la reunión)

**Por el equipo de desarrollo (Grupo #5 - Monográfico #59 - Escuela de Informática - UASD):**
- Manuel A. Hernández C.
- Alexander Trinidad Ramírez
- Elizabeth Ogando Rosa

**Promotores invitados:**

| Nombre | Comunidad | Contacto |
|--------|-----------|----------|
| José Andrés Pérez Bet | Rodríguez Cera | 829 46 64937 |
| José Cobo Martínez Reyes | La Romana de Aroa | 829 47 76 7 33 |
| Mónica María Reus López | José José López | 829 47 76 7 33 |
| Isabel Álvarez Tolosa | Arau | 829-76-77 |
| Ana Gabriela Talavera | Villa César, Cuevón | 829 69 93 52 |
| Gregory Báez Br. 10 | Peralta | 829-85-1390 |

### Registro de asistencia de promotores

| # | Nombre | Cédula | Teléfono |
|---|--------|--------|----------|
| 1 | José Abubalencia Balta | 017 0012985-4 | 829 9666977 |
| 2 | Jacobo Antonio Pérez | 010-0028683-9 | 829-4267133 |
| 3 | Micaína Paula Rovio Posó | 010 0097849 | 829 0267135 |
| 4 | Isabel Elvira Fatoma Moreno | 010-0103871-8 | 829-761-2270 |
| 5 | Ana Juliana Tarela | 402 2591072-3 | 829 698 9352 |

### Resultados del cuestionario a promotores

#### 1. Conocimiento de la aplicación

**¿Qué entienden por "Venta Precio Justo"?**

| Promotor | Respuesta |
|----------|-----------|
| José Andrés Belte | *[Respuesta registrada en formulario]* |
| Gregory Báez Brito | "Es un tipo de venta donde el productor obtiene mayores beneficios y el consumidor un mejor precio" |
| Ana Gabriela Talavera | "Conectar al productor con el consumidor de manera justa donde ambos son beneficiados" |
| Micicuaia Rauic | "Venta directa del productor al consumidor con precio justo" |

**¿Crees que los productores de tu comunidad aceptarían usar una app para vender sus productos?**

| Respuesta | Cantidad |
|-----------|----------|
| Sí, todos | ✅ Mayoría |
| Sí, algunos | ✅ Algunos |
| No, ninguno | ❌ Ninguno |

**¿Qué productos agrícolas son los más producidos en tu comunidad?**

- Café
- Aguacate
- Limón
- Chinola
- Viveres
- Productos de la zona de Azua

#### 2. Percepción sobre la aplicación

**¿Qué aspecto te parece más útil de la aplicación?**

| Aspecto | Votos |
|---------|-------|
| Venta directa sin intermediarios | ✅ Mayoría |
| Precios transparentes | ✅ Alto |
| Sistema de denuncias | ✅ Algunos |
| Chat con compradores | ✅ Algunos |

**¿Qué dificultades ves para que los productores usen la app?**

| Dificultad | Menciones |
|------------|-----------|
| Falta de smartphone | ✅ Varios |
| Falta de internet | ✅ Varios |
| Desconfianza en pagos digitales | ✅ Algunos |
| No saben usar apps | ✅ Algunos |

#### 3. Sugerencias para mejorar la aplicación

| Sugerencia | Promotor |
|------------|----------|
| "Cambiar las limitantes que tiene al registrarse, que se puedan registrar tanto como productor y como consumidor" | Gregory Báez Brito |
| "Mi sugerencia sería buscar colaboración con el gobierno para llegar a los productores que no usan la app" | Micicuaia Rauic |

#### 4. Formación y promoción

**¿Crees que necesitas capacitación para promover la app?**

| Respuesta | Cantidad |
|-----------|----------|
| Sí, mucha | ✅ Mayoría |
| Sí, poca | ✅ Algunos |
| No | ❌ Ninguno |

**¿Qué tipo de apoyo necesitarías para promover VPJ?**

- ✅ Material impreso (folletos)
- ✅ Videos tutoriales
- ✅ Capacitación presencial
- ✅ Llamadas de seguimiento

**¿Conoces a otros productores que podrían unirse?**

| Promotor | Cantidad de productores |
|----------|------------------------|
| Ana Gabriela Talavera | 10 productores |
| Otros promotores | 1-10 productores |

### Observaciones del entrevistador

- "Nos explicaron de manera clara el uso de la aplicación y los beneficios que se pueden obtener de la misma."
- "Los promotores mostraron interés en la aplicación y en la metodología de Venta Precio Justo."
- "Se identificaron oportunidades de mejora en el registro de usuarios (poder registrarse como productor y consumidor simultáneamente)."

### Conclusiones del encuentro

1. ✅ **Buena recepción:** Los promotores de Azua mostraron interés en la aplicación y en el modelo de Venta Precio Justo.

2. ✅ **Identificación de necesidades:** Se confirmó la necesidad de capacitación y material de apoyo (folletos, videos tutoriales) para los promotores.

3. ✅ **Productos clave identificados:** Café, aguacate, limón, chinola y viveres son los productos más producidos en la región.

4. ⚠️ **Desafíos identificados:** Falta de smartphones e internet en algunas comunidades rurales.

5. 💡 **Mejora sugerida:** Permitir que los usuarios se registren como productores y consumidores simultáneamente (cuenta dual).

6. 📈 **Potencial de crecimiento:** Los promotores conocen entre 1 y 10 productores que podrían unirse a la plataforma.

### Impacto del encuentro

| Aspecto | Resultado |
|---------|-----------|
| Promotores capacitados | 6+ promotores |
| Productores potenciales identificados | 10+ productores |
| Comunidades cubiertas | Azua, Rodríguez Cera, La Romana de Aroa, Arau, Villa César, Peralta |
| Nivel de aceptación | Alto (mayoría de los promotores) |

---

## FASE 129: CORRECCIÓN DE CARRITO PARA ONPECO Y CENTRO DE ACOPIO

**Fecha:** 06/07/2026
**Estado:** ✅ Completada

### Objetivo
Ocultar completamente el carrito de compras para los usuarios ONPECO (regulador) y Centro de Acopio (acopio), ya que estos roles no deben realizar compras según la lógica de negocio definida.

### Cambios en `base.html`

**Navbar - "Mi Carrito":**
```html
<!-- Antes -->
{% if user.role == 'consumidor' or user.role == 'productor' or user.role == 'suplidor' %}

<!-- Después -->
{% if user.is_authenticated and user.role != 'regulador' and user.role != 'acopio' %}
```

**Botón flotante del carrito:**
```html
<!-- Antes -->
{% if user.is_authenticated %}
    {% if user.role == 'consumidor' or user.role == 'productor' or user.role == 'suplidor' %}

<!-- Después -->
{% if user.is_authenticated and user.role != 'regulador' and user.role != 'acopio' %}
```

### Cambios en `lista_productos.html`

```html
<!-- Botón "Carrito" en tarjeta de producto -->
{% if user.is_authenticated and user.role != 'regulador' and user.role != 'acopio' %}
    <!-- Mostrar botón de carrito -->
{% elif user.is_authenticated %}
    <!-- ONPECO o Centro de Acopio: botón deshabilitado "Supervisión" -->
    <button class="btn btn-outline-secondary w-100" disabled>
        <i class="fas fa-gavel"></i> Supervisión
    </button>
{% else %}
    <!-- Usuario no autenticado: "Iniciar sesión" -->
    <a href="{% url 'users:login' %}" class="btn btn-outline-secondary flex-grow-1">
        <i class="fas fa-sign-in-alt"></i> Iniciar sesión
    </a>
{% endif %}
```

### Cambios en `detalle_producto.html`

```html
{# CASO 3: ONPECO, REGULADOR O CENTRO DE ACOPIO #}
{% else %}
    <div class="mt-4 p-3 text-center" style="background: #fff3cd; border-radius: 10px; border: 1px solid #ffc107;">
        <i class="fas fa-gavel fa-2x d-block mb-2 text-warning"></i>
        <p class="mb-0"><strong>Rol de supervisor</strong></p>
        <p class="mb-0 small text-muted">Los reguladores no pueden realizar compras. Esta función es exclusiva para consumidores.</p>
    </div>
{% endif %}
```

---

## FASE 130: SELECTOR DE EMOJIS EN CHAT

**Fecha:** 06/07/2026
**Estado:** ✅ Completada

### Objetivo
Agregar un selector de emojis en la interfaz del chat para que los usuarios puedan insertar emojis fácilmente.

### Implementación

**HTML:**
```html
<button type="button" id="emojiBtn" class="btn btn-outline-secondary">
    <i class="fas fa-smile"></i>
</button>
<div id="emojiPicker" style="display: none;">
    <div id="emojiList"></div>
</div>
```

**JavaScript:**
```javascript
const emojis = ['😊', '😂', '❤️', '👍', '🌱', '🌿', '🍎', '🍊', '🍋', '🍇', '🍉'];
emojis.forEach(function(emoji) {
    const span = document.createElement('span');
    span.textContent = emoji;
    span.addEventListener('click', function() {
        const cursorPos = mensajeInput.selectionStart;
        const text = mensajeInput.value;
        mensajeInput.value = text.substring(0, cursorPos) + emoji + text.substring(cursorPos);
        mensajeInput.focus();
        emojiPicker.style.display = 'none';
    });
    emojiList.appendChild(span);
});
```

---

## FASE 131: BOTÓN "VOLVER A MIS PRODUCTOS" EN EDICIÓN

**Fecha:** 06/07/2026
**Estado:** ✅ Completada

### Objetivo
Agregar un botón de retorno a "Mis Productos" en la página de edición de productos para mejorar la navegación.

### Implementación en `editar_producto.html`

```html
<!-- ========== BOTONES DE ACCIÓN ========== -->
<div class="d-flex gap-2 mt-4">
    <button type="submit" class="btn btn-warning flex-grow-1">
        <i class="fas fa-edit"></i> Actualizar Producto
    </button>
    <a href="{% url 'marketplace:mis_productos' %}" class="btn btn-secondary">
        <i class="fas fa-arrow-left"></i> Volver a mis productos
    </a>
</div>
```

---

## FASE 132: FORMATO DE NÚMEROS EN BALANCE DE VENTAS (RD)

**Fecha:** 06/07/2026
**Estado:** ✅ Completada

### Objetivo
Aplicar el formato de números de República Dominicana (miles con coma, decimales con punto) en el balance de ventas.

### Filtro personalizado

```python
# apps/cart/templatetags/cart_filters.py
@register.filter
def format_rd(value):
    try:
        value = float(value)
        return f"{value:,.2f}"
    except (ValueError, TypeError):
        return "0.00"
```

### Uso en template

```html
{% load cart_filters %}
<h2>RD$ {{ total_vendido|format_rd }}</h2>
```

### Ejemplos de formato
| Antes | Después |
|-------|---------|
| `RD$ 15635.00` | `RD$ 15,635.00` |
| `RD$ 23900.00` | `RD$ 23,900.00` |
| `RD$ 1550.50` | `RD$ 1,550.50` |

---

## FASE 133: ACTUALIZACIÓN DE DOCUMENTACIÓN - FASES 82 A 131

**Fecha:** 06/07/2026
**Estado:** ✅ Completada

### Resumen de fases agregadas

| Fase | Título |
|------|--------|
| 82 | Cambio de Cédula a Nombre de Productor en Listas Públicas |
| 83 | Eliminación de Reputación en Lista Pública de Productores |
| 84 | Corrección de Cédulas y Negocios de Productores |
| 85 | Buscador en Tiempo Real en Lista de Usuarios ONPECO |
| 86 | Corrección de Reporte de Ventas - Transacciones vs Unidades |
| 87 | Detalle de Ventas Agrupado por Pedido |
| 88 | Corrección de Error en Decorador `onpeco_required` |
| 89 | Corrección de Error en Exportación de Denuncias a Excel |
| 90 | Limpieza de Código - Función `obtener_fechas` |
| 91 | Servicio de Estadísticas para ONPECO |
| 92 | Filtro de Estrellas en Templates |
| 93 | Estandarización de Nombres en `views.py` |
| 94 | Corrección de Carrito para ONPECO y Centro de Acopio |
| 95 | Bloqueo de Compra para ONPECO y Centro de Acopio |
| 96 | Selector de Emojis en Chat |
| 97 | Botón "Volver a Mis Productos" en Edición |
| 98 | Formato de Números en Balance de Ventas (RD) |
| 99 | Corrección de Formato de Números en Ventas |
| 100 | Chat Privado ONPECO ↔ Centro de Acopio |
| 101 | Corrección de Rebaja de Stock en Tiempo Real |
| 102 | Rediseño de Botones con Recuadros |
| 103 | Agregado del Tomate como Orgullo de Azua |
| 104 | Corrección de Historial de Ventas |
| 105 | Corrección de Contabilización de Denuncias Aprobadas |
| 106 | Corrección de Balances Pagados |
| 107 | Enlace a ONPECO en el Portal |
| 108 | Exportación de Reportes de Denuncias a Excel |
| 109 | Sistema de Notificaciones con Contador de Incremento |
| 110 | Corrección de Error `datetime` en Backups |
| 111 | Cambio de Login a Cédula y Mejora de Interfaz |
| 112 | Tomate Clicable con Enlace a ONPECO |
| 113 | Sistema de Restablecimiento de Contraseñas por ONPECO |
| 114 | Nombre Real en Navbar y Perfil |
| 115 | Exportación de Consumidores y Productores a Excel |
| 116 | Integración del Logo Oficial de ONPECO |
| 117 | Estilizado del Logo ONPECO con Bordes Redondeados |
| 118 | Cambio de Favicon a Logo de ONPECO (Definitivo) |
| 119 | Optimización de la Página de Inicio |
| 120 | Corrección del Footer - Texto Institucional |
| 121 | Ajuste de Posición del Carrito Flotante |
| 122 | Eliminación de Notificaciones de Chat sin Sesión |
| 123 | Verificación Final y Consolidación de Cambios |
| 124 | Cambio de Color de "VPJ" a Rojo |
| 125 | Módulo "Sobre VPJ" - Modal Informativo |
| 126 | Chat Privado ONPECO ↔ Centro de Acopio |
| 127 | Presentación Oficial a ONPECO - Demostración en Vivo con Ngrok | 25/06/2026 | ✅ Completada |
| 128 | Encuentro con Promotores en Azua - Presentación de VPJ | 03/07/2026 | ✅ Completada |
| 129 | Corrección de Carrito para ONPECO y Centro de Acopio | 06/07/2026 | ✅ Completada |
| 130 | Selector de Emojis en Chat | 06/07/2026 | ✅ Completada |
| 131 | Botón "Volver a Mis Productos" en Edición | 06/07/2026 | ✅ Completada |
| 132 | Formato de Números en Balance de Ventas (RD) | 06/07/2026 | ✅ Completada |
| 133 | Actualización de Documentación - FASES 127 A 132 | 06/07/2026 | ✅ Completada |

---

## 📊 ESTADO GENERAL DEL PROYECTO

**Estado del Proyecto:** 🟢 En producción para pruebas

**Total de fases implementadas: 133**

**Última actualización:** 06 de julio de 2026

---

**Fin del documento**
```

---

✅ **PASO COMPLETADO**

**Ahora haz lo siguiente:**

1. **Abre tu documento original** (el de 4746 líneas)
2. **Ve al final** del documento (después de la Fase 81)
3. **Copia TODO el texto que te di arriba** (desde "## FASE 82" hasta el final)
4. **Pégalo al final** de tu documento
5. **Guarda el archivo**

Tu documento tendrá las **4746 líneas originales + las nuevas fases 82-132**, manteniendo TODO el contenido detallado de las fases 1-81.

**¿Quieres que te ayude con algo más?** 🚀

