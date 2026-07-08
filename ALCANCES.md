📄 DOCUMENTO: ALCANCES DEL PROYECTO VPJ POR MÓDULO
markdown
# ALCANCES DEL PROYECTO VPJ (VENTA PRECIO JUSTO)

**Plataforma de comercio justo para ONPECO**

Desarrollado por el Grupo #5 - Monográfico #59
Escuela de Informática - Universidad Autónoma de Santo Domingo (UASD)

**Última actualización:** 08 de julio de 2026

---

## 📋 CONTENIDO

1. [Alcance General del Proyecto](#1-alcance-general-del-proyecto)
2. [Módulo de Autenticación y Usuarios](#2-módulo-de-autenticación-y-usuarios)
3. [Módulo de Marketplace (Productos)](#3-módulo-de-marketplace-productos)
4. [Módulo de Carrito de Compras](#4-módulo-de-carrito-de-compras)
5. [Módulo de Pedidos y Ventas](#5-módulo-de-pedidos-y-ventas)
6. [Módulo de Centro de Acopio](#6-módulo-de-centro-de-acopio)
7. [Módulo de Denuncias](#7-módulo-de-denuncias)
8. [Módulo de Chat en Tiempo Real](#8-módulo-de-chat-en-tiempo-real)
9. [Módulo de ONPECO (Regulador)](#9-módulo-de-onpeco-regulador)
10. [Módulo de Reportes y Exportaciones](#10-módulo-de-reportes-y-exportaciones)
11. [Módulo de Backups y Restauración](#11-módulo-de-backups-y-restauración)
12. [Resumen de Funcionalidades por Rol](#12-resumen-de-funcionalidades-por-rol)

---

## 1. ALCANCE GENERAL DEL PROYECTO

### 1.1 Objetivo General

Desarrollar una plataforma de comercio justo que conecte directamente a productores agrícolas de la provincia de Azua con consumidores finales, eliminando intermediarios especulativos y garantizando precios justos para ambas partes, bajo la supervisión y regulación de ONPECO.

### 1.2 Objetivos Específicos

| # | Objetivo | Módulo asociado |
|---|----------|-----------------|
| 1 | Permitir el registro y autenticación de 4 roles de usuario | Autenticación |
| 2 | Facilitar la publicación y gestión de productos agrícolas | Marketplace |
| 3 | Implementar un sistema de compras con carrito de compras | Carrito |
| 4 | Gestionar pedidos y ventas con trazabilidad | Pedidos y Ventas |
| 5 | Centralizar pagos a través del Centro de Acopio | Centro de Acopio |
| 6 | Permitir denuncias de consumidores con seguimiento | Denuncias |
| 7 | Implementar comunicación en tiempo real con WebSockets | Chat |
| 8 | Proveer herramientas de supervisión para ONPECO | ONPECO |
| 9 | Generar reportes y exportaciones a Excel | Reportes |
| 10 | Implementar sistema de backups y restauración | Backups |

### 1.3 Usuarios del Sistema

| Rol | Cantidad estimada | Función principal |
|-----|-------------------|-------------------|
| Consumidor | ~200,000 potenciales | Compra productos, califica, denuncia |
| Productor | ~50,000 potenciales | Publica productos, vende, balance |
| ONPECO (Regulador) | ~10-20 | Supervisa, gestiona denuncias, backups |
| Centro de Acopio | ~5-10 | Gestiona pedidos y pagos |

---

## 2. MÓDULO DE AUTENTICACIÓN Y USUARIOS

### 2.1 Alcance

| Aspecto | Detalle |
|---------|---------|
| **Responsable** | Módulo de autenticación y gestión de usuarios |
| **Objetivo** | Permitir el registro, inicio de sesión y gestión de perfiles para los 4 roles del sistema |

### 2.2 Funcionalidades Implementadas

| # | Funcionalidad | Estado |
|---|---------------|--------|
| 1 | Registro de consumidores (aprobación automática) | ✅ |
| 2 | Registro de productores (requiere aprobación de ONPECO) | ✅ |
| 3 | Registro de suplidores (desactivado para implementación futura) | ⚠️ Desactivado |
| 4 | Inicio de sesión con cédula | ✅ |
| 5 | Cierre de sesión | ✅ |
| 6 | Perfil de usuario con foto y ubicación | ✅ |
| 7 | Recuperación de contraseña ("Olvidé mi contraseña") | ✅ |
| 8 | Restablecimiento de contraseña por ONPECO | ✅ |
| 9 | Validación de cédula con algoritmo de Luhn | ✅ |
| 10 | Aprobación de productores por ONPECO | ✅ |

### 2.3 Modelos de Datos

```python
class User(models.Model):
    ROLES = (
        ('productor', 'Productor'),
        ('consumidor', 'Consumidor'),
        ('suplidor', 'Suplidor'),
        ('regulador', 'Regulador'),
        ('acopio', 'Centro de Acopio'),
    )
    
    username = models.CharField(max_length=20, unique=True)  # Cédula
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    role = models.CharField(max_length=20, choices=ROLES)
    is_approved = models.BooleanField(default=False)
    business_name = models.CharField(max_length=100, blank=True)
    profile_image = models.ImageField(upload_to='profiles/', null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    must_change_password = models.BooleanField(default=False)
2.4 Alcance del Módulo de Usuarios
Función	Descripción	Requisitos previos
Registrar consumidor	Formulario público, aprobación automática	Ninguno
Registrar productor	Formulario público, requiere aprobación de ONPECO	Ninguno
Aprobar productor	ONPECO revisa y aprueba productores pendientes	Ser ONPECO
Iniciar sesión	Autenticación con cédula y contraseña	Estar registrado
Recuperar contraseña	Envío de enlace de recuperación por email	Tener email registrado
Restablecer contraseña	ONPECO puede restablecer a 'cambiar123'	Ser ONPECO
2.5 Usuarios de Prueba
Rol	Usuario	Contraseña
Consumidor	bartolo	bartolo123
Productor	nancy	nancy123
ONPECO	onpeco_regulador	regulador123
Centro de Acopio	centro_acopio	acopio123
3. MÓDULO DE MARKETPLACE (PRODUCTOS)
3.1 Alcance
Aspecto	Detalle
Responsable	Módulo de marketplace y gestión de productos
Objetivo	Permitir a productores publicar, gestionar y vender sus productos agrícolas
3.2 Funcionalidades Implementadas
#	Funcionalidad	Estado
1	Lista de productos con paginación	✅
2	Detalle de producto	✅
3	Búsqueda en tiempo real de productos	✅
4	Filtros por categoría	✅
5	Creación de productos (productores)	✅
6	Edición de productos (solo propietario)	✅
7	Eliminación de productos (solo propietario)	✅
8	Control de stock con rebaja automática	✅
9	Alerta de stock bajo	✅
10	Contador de vistas por producto	✅
11	Imagen de producto	✅
3.3 Modelos de Datos
python
class Product(models.Model):
    CATEGORIAS = (
        ('frutas', 'Frutas'),
        ('verduras', 'Verduras'),
        ('tuberculos', 'Tubérculos'),
        ('lacteos', 'Lácteos'),
        ('hierbas', 'Hierbas'),
        ('otros', 'Otros'),
    )
    
    UNIDADES = (
        ('kg', 'Kilogramo'),
        ('lb', 'Libra'),
        ('unidad', 'Unidad'),
        ('docena', 'Docena'),
    )
    
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='productos')
    productor_origen = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
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
3.4 Alcance del Módulo de Marketplace
Función	Descripción	Requisitos previos
Listar productos	Muestra todos los productos disponibles	Ninguno
Ver detalle	Muestra información completa del producto	Ninguno
Buscar productos	Búsqueda en tiempo real por nombre	Ninguno
Crear producto	Formulario para publicar producto	Ser productor aprobado
Editar producto	Modificar producto existente	Ser propietario
Eliminar producto	Ocultar producto (soft delete)	Ser propietario
Ver stock	Visualizar stock disponible	Todos
4. MÓDULO DE CARRITO DE COMPRAS
4.1 Alcance
Aspecto	Detalle
Responsable	Módulo de carrito de compras
Objetivo	Permitir a consumidores seleccionar y gestionar productos antes de comprar
4.2 Funcionalidades Implementadas
#	Funcionalidad	Estado
1	Agregar productos al carrito	✅
2	Ver carrito con productos	✅
3	Actualizar cantidades	✅
4	Eliminar productos del carrito	✅
5	Vaciar carrito	✅
6	Cálculo automático de subtotales y total	✅
7	Bloqueo de carrito para ONPECO y Acopio	✅
8	Persistencia de carrito por usuario	✅
4.3 Modelos de Datos
python
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('marketplace.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)
4.4 Alcance del Módulo de Carrito
Función	Descripción	Requisitos previos
Agregar al carrito	Añade producto al carrito del usuario	Ser consumidor
Ver carrito	Muestra todos los productos en el carrito	Ser consumidor
Actualizar cantidad	Modifica la cantidad de un producto	Ser consumidor
Eliminar producto	Quita producto del carrito	Ser consumidor
Vaciar carrito	Elimina todos los productos	Ser consumidor
5. MÓDULO DE PEDIDOS Y VENTAS
5.1 Alcance
Aspecto	Detalle
Responsable	Módulo de pedidos, ventas y balances
Objetivo	Gestionar el ciclo completo de compra: desde el pedido hasta el pago
5.2 Funcionalidades Implementadas
#	Funcionalidad	Estado
1	Checkout con datos de entrega	✅
2	Confirmación de pedido	✅
3	Mis pedidos (consumidor)	✅
4	Detalle de pedido (consumidor)	✅
5	Mis ventas (productor)	✅
6	Detalle de venta (productor)	✅
7	Balance de ventas (productor)	✅
8	Formato de números RD (miles con coma, decimales con punto)	✅
9	Estados del pedido (pendiente, confirmado, preparando, entregado, cancelado)	✅
10	Desglose de pedidos por productor	✅
5.3 Modelos de Datos
python
class Order(models.Model):
    ESTADO_CHOICES = [
        ('pending', '⏳ Pendiente de confirmación'),
        ('confirmed', '✅ Confirmado por productor'),
        ('preparing', '📦 En preparación'),
        ('delivered', '🏠 Entregado - Pago realizado'),
        ('cancelled', '❌ Cancelado'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pending')
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    delivery_type = models.CharField(max_length=20, choices=TIPO_ENTREGA_CHOICES, default='delivery')
    shipping_address = models.TextField()
    phone_number = models.CharField(max_length=15)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='pending')
    payment_date = models.DateTimeField(blank=True, null=True)
    payment_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    acopio = models.ForeignKey(User, on_delete=models.CASCADE, related_name='acopio_orders', null=True, blank=True)
    payment_breakdown = models.JSONField(default=dict, blank=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('marketplace.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
5.4 Alcance del Módulo de Pedidos y Ventas
Función	Descripción	Requisitos previos
Checkout	Formulario de confirmación de pedido	Tener productos en carrito
Confirmación de pedido	Página de confirmación con número de pedido	Haber completado checkout
Mis pedidos	Lista de pedidos del consumidor	Ser consumidor
Detalle de pedido	Ver productos y estado del pedido	Ser propietario del pedido
Mis ventas	Lista de pedidos recibidos	Ser productor
Balance de ventas	Resumen de ventas con formato RD	Ser productor
6. MÓDULO DE CENTRO DE ACOPIO
6.1 Alcance
Aspecto	Detalle
Responsable	Módulo de Centro de Acopio
Objetivo	Centralizar la gestión de pedidos y pagos, resolviendo el problema de pagos a múltiples productores en un solo pedido
6.2 Funcionalidades Implementadas
#	Funcionalidad	Estado
1	Lista de pedidos recibidos	✅
2	Detalle de pedido con desglose por productor	✅
3	Registro de pagos a productores	✅
4	Visualización de desglose en JSON	✅
5	Chat privado con ONPECO	✅
6.3 Estructura del Desglose de Pagos
json
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
6.4 Alcance del Módulo de Centro de Acopio
Función	Descripción	Requisitos previos
Ver pedidos	Lista de pedidos recibidos	Ser Centro de Acopio
Ver detalle	Desglose de pedido por productor	Ser Centro de Acopio
Registrar pago	Marcar como pagado a un productor	Ser Centro de Acopio
Chat con ONPECO	Comunicación privada con ONPECO	Ser Centro de Acopio
7. MÓDULO DE DENUNCIAS
7.1 Alcance
Aspecto	Detalle
Responsable	Módulo de denuncias y seguimiento
Objetivo	Permitir a consumidores reportar problemas y a ONPECO dar seguimiento
7.2 Funcionalidades Implementadas
#	Funcionalidad	Estado
1	Creación de denuncias por consumidores	✅
2	Lista de denuncias (ONPECO)	✅
3	Detalle de denuncia con historial	✅
4	Actualización de estado (ONPECO)	✅
5	Filtros por estado	✅
6	Generación de ticket automático	✅
7	Prioridad de denuncias (baja, media, alta, crítica)	✅
8	Historial de actualizaciones	✅
7.3 Modelos de Datos
python
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
7.4 Alcance del Módulo de Denuncias
Función	Descripción	Requisitos previos
Crear denuncia	Formulario para reportar problema	Ser consumidor
Mis denuncias	Lista de denuncias del consumidor	Ser consumidor
Lista de denuncias	Todas las denuncias del sistema	Ser ONPECO
Detalle de denuncia	Ver información completa y historial	Ser ONPECO
Actualizar denuncia	Cambiar estado y agregar comentario	Ser ONPECO
Reporte de denuncias	Gráfico de denuncias por mes	Ser ONPECO
8. MÓDULO DE CHAT EN TIEMPO REAL
8.1 Alcance
Aspecto	Detalle
Responsable	Módulo de chat con WebSockets
Objetivo	Permitir comunicación en tiempo real entre consumidores y productores, y entre ONPECO y Centro de Acopio
8.2 Funcionalidades Implementadas
#	Funcionalidad	Estado
1	Chat en tiempo real con WebSockets	✅
2	Lista de conversaciones por usuario	✅
3	Ventana de chat con mensajes	✅
4	Selector de emojis	✅
5	Notificaciones de mensajes no leídos	✅
6	Badge de notificaciones en navbar	✅
7	Chat privado ONPECO ↔ Centro de Acopio	✅
8	Mensajes en tiempo real con Daphne	✅
9	Almacenamiento de mensajes en base de datos	✅
8.3 Modelos de Datos
python
class ChatRoom(models.Model):
    productor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_rooms_as_productor')
    consumidor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_rooms_as_consumidor')
    is_private_onpeco_acopio = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ChatMessage(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
8.4 Arquitectura del Chat
text
Cliente (Navegador) ←→ WebSocket ←→ Daphne (ASGI) ←→ Django Channels ←→ Base de datos
8.5 Alcance del Módulo de Chat
Función	Descripción	Requisitos previos
Iniciar chat	Crear sala de chat con productor	Estar autenticado
Lista de chats	Ver conversaciones activas	Estar autenticado
Enviar mensaje	Mensaje en tiempo real	Estar autenticado
Selector de emojis	Insertar emojis en el chat	Estar autenticado
Chat privado ONPECO-Acopio	Canal exclusivo para coordinación	Ser ONPECO o Acopio
9. MÓDULO DE ONPECO (REGULADOR)
9.1 Alcance
Aspecto	Detalle
Responsable	Módulo de supervisión y regulación de ONPECO
Objetivo	Proveer herramientas de control, supervisión y gestión para ONPECO
9.2 Funcionalidades Implementadas
#	Funcionalidad	Estado
1	Portal ONPECO (dashboard)	✅
2	Gestión de denuncias (lista, detalle, actualización)	✅
3	Reporte de denuncias con gráficos	✅
4	Productos más consultados	✅
5	Productores más denunciados	✅
6	Aprobación de productores	✅
7	Gestión de backups	✅
8	Exportación de datos a Excel	✅
9	Chat privado con Centro de Acopio	✅
10	Restablecimiento de contraseñas de usuarios	✅
11	Buscador en tiempo real de usuarios	✅
12	Bloqueo de acceso al admin de Django	✅
9.3 Estructura del Portal ONPECO
text
Portal ONPECO
├── Dashboard (estadísticas)
│   ├── Total de denuncias
│   ├── Denuncias pendientes
│   ├── Denuncias en revisión
│   ├── Denuncias resueltas
│   └── Denuncias rechazadas
├── Gestión de Denuncias
│   ├── Lista de denuncias (con filtros)
│   ├── Detalle de denuncia
│   └── Actualización de estado
├── Reportes
│   └── Gráfico de denuncias por mes
├── Supervisión
│   ├── Productos más vistos
│   └── Productores más denunciados
├── Usuarios
│   ├── Aprobar productores
│   └── Restablecer contraseñas
├── Backups
│   ├── Crear punto de restauración
│   └── Lista de backups
└── Comunicación
    └── Chat privado con Centro de Acopio
9.4 Alcance del Módulo de ONPECO
Función	Descripción	Requisitos previos
Portal ONPECO	Dashboard con estadísticas	Ser ONPECO
Gestionar denuncias	Lista, detalle y actualización	Ser ONPECO
Reporte de denuncias	Gráfico de denuncias por mes	Ser ONPECO
Productos más vistos	Ranking de productos	Ser ONPECO
Productores más denunciados	Ranking de productores	Ser ONPECO
Aprobar productores	Activar cuentas de productores	Ser ONPECO
Gestión de backups	Crear y restaurar backups	Ser ONPECO
Exportar a Excel	Denuncias, consumidores, productores	Ser ONPECO
Chat con Acopio	Canal privado de comunicación	Ser ONPECO
10. MÓDULO DE REPORTES Y EXPORTACIONES
10.1 Alcance
Aspecto	Detalle
Responsable	Módulo de reportes y exportaciones
Objetivo	Permitir la generación de reportes y exportación de datos a Excel
10.2 Funcionalidades Implementadas
#	Funcionalidad	Estado
1	Reporte de denuncias con gráfico (Chart.js)	✅
2	Exportación de denuncias a Excel	✅
3	Exportación de consumidores a Excel	✅
4	Exportación de productores a Excel	✅
5	Filtros por fechas en reportes	✅
6	Formato de números RD en reportes	✅
10.3 Alcance del Módulo de Reportes
Función	Descripción	Requisitos previos
Reporte de denuncias	Gráfico de barras con denuncias por mes	Ser ONPECO
Exportar denuncias	Excel con todas las denuncias	Ser ONPECO
Exportar consumidores	Excel con todos los consumidores	Ser ONPECO
Exportar productores	Excel con todos los productores	Ser ONPECO
11. MÓDULO DE BACKUPS Y RESTAURACIÓN
11.1 Alcance
Aspecto	Detalle
Responsable	Módulo de backups y restauración
Objetivo	Permitir a ONPECO crear puntos de restauración y recuperar el sistema en caso de fallo
11.2 Funcionalidades Implementadas
#	Funcionalidad	Estado
1	Creación de puntos de restauración	✅
2	Lista de backups con fecha y tamaño	✅
3	Restauración de backups	✅
4	Backup automático programado	✅
5	Historial de backups	✅
11.3 Modelos de Datos
python
class BackupHistory(models.Model):
    filename = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    description = models.TextField(blank=True)
    size = models.BigIntegerField(default=0)
11.4 Alcance del Módulo de Backups
Función	Descripción	Requisitos previos
Crear backup	Genera punto de restauración	Ser ONPECO
Listar backups	Muestra backups disponibles	Ser ONPECO
Restaurar backup	Recupera sistema desde backup	Ser ONPECO
12. RESUMEN DE FUNCIONALIDADES POR ROL
12.1 Consumidor
#	Funcionalidad	Módulo
1	Registro de consumidor	Autenticación
2	Inicio de sesión	Autenticación
3	Ver productos	Marketplace
4	Buscar productos	Marketplace
5	Ver detalle de producto	Marketplace
6	Agregar al carrito	Carrito
7	Ver carrito	Carrito
8	Finalizar compra (checkout)	Pedidos
9	Ver mis pedidos	Pedidos
10	Ver detalle de pedido	Pedidos
11	Crear denuncia	Denuncias
12	Chat con productores	Chat
12.2 Productor
#	Funcionalidad	Módulo
1	Registro de productor	Autenticación
2	Inicio de sesión	Autenticación
3	Crear producto	Marketplace
4	Editar producto	Marketplace
5	Eliminar producto	Marketplace
6	Ver mis productos	Marketplace
7	Ver mis ventas	Pedidos
8	Ver detalle de venta	Pedidos
9	Balance de ventas	Pedidos
10	Chat con consumidores	Chat
12.3 ONPECO (Regulador)
#	Funcionalidad	Módulo
1	Inicio de sesión	Autenticación
2	Portal ONPECO (dashboard)	ONPECO
3	Gestionar denuncias	ONPECO
4	Reporte de denuncias	ONPECO
5	Productos más vistos	ONPECO
6	Productores más denunciados	ONPECO
7	Aprobar productores	ONPECO
8	Gestión de backups	ONPECO
9	Exportación a Excel	ONPECO
10	Chat privado con Acopio	Chat
12.4 Centro de Acopio
#	Funcionalidad	Módulo
1	Inicio de sesión	Autenticación
2	Ver pedidos recibidos	Centro de Acopio
3	Ver detalle de pedido (desglose)	Centro de Acopio
4	Registrar pagos	Centro de Acopio
5	Chat privado con ONPECO	Chat
📊 RESUMEN GENERAL
Total de Funcionalidades por Módulo
Módulo	Funcionalidades
Autenticación y Usuarios	10
Marketplace (Productos)	11
Carrito de Compras	8
Pedidos y Ventas	10
Centro de Acopio	5
Denuncias	7
Chat en Tiempo Real	9
ONPECO (Regulador)	12
Reportes y Exportaciones	6
Backups y Restauración	4
TOTAL	82 funcionalidades
Total de Fases Documentadas
Fase	Estado
Fases 1-81	✅ Documentadas
Fases 82-133	✅ Documentadas
TOTAL	133 fases
Fin del Documento de Alcances

Última actualización: 08 de julio de 2026