# FUNCIONALIDADES FUTURAS Y FUERA DEL ALCANCE - VPJ

**Venta Precio Justo - Plataforma de comercio justo para ONPECO**

---

## 📋 INTRODUCCIÓN

Durante el desarrollo del proyecto **VPJ (Venta Precio Justo)**, recibimos múltiples sugerencias de diferentes actores involucrados en el ecosistema: ONPECO, promotores de la provincia de Azua, usuarios finales, y docentes de la Escuela de Informática de la UASD.

Este documento recopila:

1. **Funcionalidades futuras:** Sugerencias recibidas que podrían implementarse en versiones posteriores.
2. **Lo que NO contempla el proyecto:** Aquello que está fuera del alcance actual, ya sea por limitaciones técnicas, de tiempo, o porque no forma parte del objetivo del monográfico.

Este documento demuestra que el equipo de desarrollo tiene una **visión clara del proyecto**, sabe **gestionar expectativas** y entiende **los límites del sistema**.

---

## 📊 CLASIFICACIÓN DE FUNCIONALIDADES

| Prioridad | Descripción |
|-----------|-------------|
| 🔴 **Alta** | Funcionalidades que mejorarían significativamente la experiencia del usuario |
| 🟡 **Media** | Funcionalidades que agregarían valor, pero no son críticas |
| 🟢 **Baja** | Funcionalidades que podrían implementarse en el largo plazo |

---

## 🚫 LO QUE NO CONTEMPLA EL PROYECTO (FUERA DEL ALCANCE)

Esta sección documenta lo que **NO está incluido** en la versión actual del sistema VPJ, ya sea porque no fue solicitado, porque requiere infraestructura adicional, o porque está fuera del alcance del monográfico.

### 1. Infraestructura y Despliegue

| # | Aspecto | Motivo |
|---|---------|--------|
| 1 | **Despliegue en la nube con hosting profesional** | No está contemplado en el alcance del monográfico. El sistema se entrega para ser instalado por ONPECO. |
| 2 | **Servidor dedicado o VPS** | Requiere contratación externa y administración técnica. ONPECO deberá gestionarlo si decide escalar. |
| 3 | **Certificado SSL propio** | El monográfico no cubre la compra ni configuración de certificados SSL comerciales. |
| 4 | **Balanceo de carga** | No es necesario para un proyecto piloto. Se requeriría si el sistema crece significativamente. |
| 5 | **Base de datos en la nube** | La base de datos se entrega en PostgreSQL local. La migración a la nube es responsabilidad de ONPECO. |

### 2. Pagos y Transacciones Financieras

| # | Aspecto | Motivo |
|---|---------|--------|
| 6 | **Pasarela de pagos en línea** | No se implementó por requerir integración con servicios externos (Stripe, PayPal). |
| 7 | **Pagos con tarjeta de crédito/débito** | Requiere pasarela de pagos y cumplimiento de normativas financieras. |
| 8 | **Pagos con monedas digitales** | No es necesario para el proyecto piloto. |
| 9 | **Facturación electrónica automática** | Requiere integración con sistemas de facturación del Estado. |

### 3. Funcionalidades Avanzadas

| # | Aspecto | Motivo |
|---|---------|--------|
| 10 | **Aplicación móvil nativa (iOS/Android)** | No está contemplado en el alcance del monográfico. |
| 11 | **Notificaciones push** | Requiere servicios de terceros (Firebase, OneSignal). |
| 12 | **Geolocalización en tiempo real** | Requiere integración con APIs de mapas (Google Maps, OpenStreetMap). |
| 13 | **Inteligencia artificial o recomendaciones** | No es necesario para el proyecto piloto. |
| 14 | **Chatbots automáticos** | No está contemplado en el alcance. |
| 15 | **Integración con sistemas externos** | No se integró con otros sistemas de ONPECO por no ser requerido. |

### 4. Roles y Permisos

| # | Aspecto | Motivo |
|---|---------|--------|
| 16 | **Roles personalizados por ONPECO** | No se implementó por simplicidad del monográfico. |
| 17 | **Activación del rol Suplidor** | Fue desactivado por decisión de ONPECO. Se reactivará cuando se defina una política clara. |
| 18 | **Cuenta dual (Productor + Consumidor)** | No se implementó por complejidad en la gestión de sesiones. |

### 5. Interfaz y Experiencia de Usuario

| # | Aspecto | Motivo |
|---|---------|--------|
| 19 | **Modo oscuro** | No es prioritario para el proyecto piloto. |
| 20 | **Animaciones avanzadas** | No es necesario para la versión inicial. |
| 21 | **Multilenguaje (inglés)** | No es necesario para el piloto en Azua. |
| 22 | **Imagen de fondo en página de inicio** | Se sugiere para futura versión. |

### 6. Mantenimiento y Soporte

| # | Aspecto | Motivo |
|---|---------|--------|
| 23 | **Soporte técnico 24/7** | No está contemplado en el alcance. |
| 24 | **Sistema de tickets de soporte** | No se implementó por simplicidad. |
| 25 | **Base de conocimiento (FAQ)** | No se implementó en la versión actual. |

### 7. Infraestructura de Comunicación

| # | Aspecto | Motivo |
|---|---------|--------|
| 26 | **Correos electrónicos transaccionales** | Requiere configuración de servidor SMTP. |
| 27 | **Boletines informativos** | No es necesario para el piloto. |
| 28 | **Integración con redes sociales** | No está contemplado. |

---

## 🆕 FUNCIONALIDADES FUTURAS POR MÓDULO

### 1. Módulo de Autenticación y Usuarios

| # | Funcionalidad | Prioridad | Descripción |
|---|---------------|-----------|-------------|
| 1 | Cuenta dual (Productor + Consumidor) | 🟡 Media | Permitir que un usuario se registre como productor y consumidor simultáneamente, con una sola cuenta. |
| 2 | Verificación de identidad con documentos | 🟡 Media | Permitir a los productores subir documentos de identidad para verificar su identidad. |
| 3 | Roles personalizables por ONPECO | 🟢 Baja | Permitir a ONPECO crear roles personalizados con permisos específicos. |
| 4 | **Activación del rol Suplidor** | 🔴 Alta | **Reactivar el rol Suplidor cuando ONPECO defina una política clara de intermediación.** El código ya está implementado y desactivado, listo para ser activado. |

---

### 2. Módulo de Marketplace (Productos)

| # | Funcionalidad | Prioridad | Descripción |
|---|---------------|-----------|-------------|
| 5 | Geolocalización de productos | 🔴 Alta | Mostrar productos en un mapa, permitiendo a los consumidores ver productos cercanos. |
| 6 | Sistema de ofertas y promociones | 🟡 Media | Permitir a productores crear ofertas especiales (descuentos, combos, etc.). |
| 7 | Notificaciones de stock bajo para consumidores | 🟡 Media | Notificar a consumidores cuando un producto favorito tenga stock bajo. |
| 8 | Comparador de precios | 🟢 Baja | Permitir a consumidores comparar precios de productos similares. |
| 9 | **Pantalla de bienvenida con imagen de fondo** | 🔴 Alta | **Incorporar una imagen de fondo opaca que haga alusión a los productos agrícolas (canasta llena de frutas, verduras, productos de Azua).** |
| 10 | Videos de productos | 🟢 Baja | Permitir a productores subir videos cortos de sus productos. |
| 11 | Etiquetas de "Producto del día" | 🟡 Media | Destacar productos con etiquetas visuales (oferta, nuevo, más vendido). |
| 12 | Categorías con íconos personalizados | 🟢 Baja | Asignar íconos personalizados a cada categoría de producto. |

---

### 3. Módulo de Carrito de Compras

| # | Funcionalidad | Prioridad | Descripción |
|---|---------------|-----------|-------------|
| 13 | Guardar carrito para después | 🟡 Media | Permitir a consumidores guardar su carrito para completar la compra después. |
| 14 | Lista de deseos (Wishlist) | 🟢 Baja | Permitir a consumidores guardar productos favoritos sin comprarlos. |
| 15 | Cálculo de envío automático | 🟡 Media | Calcular automáticamente el costo de envío basado en la ubicación. |

---

### 4. Módulo de Pedidos y Checkout

| # | Funcionalidad | Prioridad | Descripción |
|---|---------------|-----------|-------------|
| 16 | Múltiples direcciones de entrega | 🟡 Media | Permitir a consumidores tener varias direcciones guardadas. |
| 17 | Pago con tarjeta de crédito integrado | 🔴 Alta | Integrar pasarela de pagos (PayPal, Stripe, etc.) para pagos en línea. |
| 18 | Facturación electrónica | 🟡 Media | Generar facturas electrónicas para los pedidos. |
| 19 | Seguimiento de entregas en tiempo real | 🟢 Baja | Permitir a consumidores ver el estado de su pedido en un mapa. |
| 20 | **Comisión porcentual para operatividad** | 🔴 Alta | **Permitir que ONPECO y el Centro de Acopio establezcan una cuota porcentual sobre cada venta para mantener la operatividad de la plataforma y el personal.** |

---

### 5. Módulo de Centro de Acopio

| # | Funcionalidad | Prioridad | Descripción |
|---|---------------|-----------|-------------|
| 21 | Reportes de pagos automáticos | 🟡 Media | Generar reportes automáticos de pagos realizados a productores. |
| 22 | Dashboard de Acopio con gráficos | 🟢 Baja | Dashboards visuales con estadísticas de pedidos y pagos. |
| 23 | **Gestión de comisiones** | 🔴 Alta | **Permitir al Centro de Acopio gestionar y visualizar las comisiones generadas por las ventas.** |
| 24 | Historial de comisiones por productor | 🟡 Media | Mostrar a cada productor el historial de comisiones aplicadas a sus ventas. |

---

### 6. Módulo de Denuncias

| # | Funcionalidad | Prioridad | Descripción |
|---|---------------|-----------|-------------|
| 25 | Denuncias anónimas | 🟡 Media | Permitir a consumidores denunciar de forma anónima. |
| 26 | Sistema de mediación | 🟢 Baja | Crear un sistema de mediación entre consumidores y productores. |
| 27 | Categorías de denuncias predefinidas | 🟡 Media | Ampliar las categorías de denuncias para cubrir más casos. |

---

### 7. Módulo de Chat en Tiempo Real

| # | Funcionalidad | Prioridad | Descripción |
|---|---------------|-----------|-------------|
| 28 | Grupos de chat | 🟡 Media | Permitir chats grupales entre productores de una misma zona. |
| 29 | Notificaciones push | 🔴 Alta | Enviar notificaciones push a los usuarios cuando reciben mensajes. |
| 30 | Archivos adjuntos en chat | 🟢 Baja | Permitir enviar imágenes y documentos en el chat. |
| 31 | Mensajes de voz | 🟢 Baja | Permitir enviar mensajes de voz en el chat. |
| 32 | Respuestas rápidas (plantillas) | 🟡 Media | Permitir a productores tener respuestas predefinidas para preguntas frecuentes. |

---

### 8. Módulo de ONPECO (Portal de Supervisión)

| # | Funcionalidad | Prioridad | Descripción |
|---|---------------|-----------|-------------|
| 33 | Panel de control en tiempo real | 🔴 Alta | Dashboard con datos en vivo de ventas, denuncias y usuarios activos. |
| 34 | Auditoría de acciones de usuarios | 🟡 Media | Registrar todas las acciones de los usuarios para auditoría. |
| 35 | Gestión de roles y permisos | 🟢 Baja | Permitir a ONPECO gestionar roles y permisos de usuarios. |
| 36 | **Configuración de comisiones** | 🔴 Alta | **Panel para que ONPECO configure el porcentaje de comisión por venta.** |
| 37 | Reporte de ingresos por comisiones | 🟡 Media | Reporte detallado de los ingresos generados por comisiones. |

---

### 9. Módulo de Reportes y Exportaciones

| # | Funcionalidad | Prioridad | Descripción |
|---|---------------|-----------|-------------|
| 38 | Reportes personalizables | 🟡 Media | Permitir a ONPECO crear reportes personalizados. |
| 39 | Exportación a PDF mejorada | 🟡 Media | Generar PDFs con mejor formato y diseño. |
| 40 | Reportes de comisiones | 🟡 Media | Reporte detallado de comisiones generadas y pagadas. |
| 41 | Dashboards interactivos | 🟢 Baja | Dashboards con gráficos interactivos para análisis de datos. |

---

### 10. Módulo de Interfaz y Usabilidad

| # | Funcionalidad | Prioridad | Descripción |
|---|---------------|-----------|-------------|
| 42 | Modo oscuro | 🟢 Baja | Implementar un modo oscuro para la interfaz. |
| 43 | Aplicación móvil (PWA) | 🔴 Alta | Convertir la aplicación en una Progressive Web App para dispositivos móviles. |
| 44 | Accesibilidad (WCAG) | 🟡 Media | Mejorar la accesibilidad para personas con discapacidades. |
| 45 | **Pantalla de bienvenida con imagen de fondo** | 🔴 Alta | **Mejorar la página de inicio con una imagen de fondo alusiva a productos agrícolas.** |
| 46 | Animaciones y transiciones | 🟢 Baja | Agregar animaciones suaves para mejorar la experiencia del usuario. |
| 47 | Selector de idioma (inglés) | 🟢 Baja | Permitir cambiar el idioma de la interfaz. |

---

### 11. Módulo de Mantenimiento y Soporte

| # | Funcionalidad | Prioridad | Descripción |
|---|---------------|-----------|-------------|
| 48 | Sistema de tickets de soporte | 🟡 Media | Permitir a usuarios reportar problemas técnicos a través de un sistema de tickets. |
| 49 | Base de conocimiento (FAQ) | 🟢 Baja | Crear una sección de preguntas frecuentes para usuarios. |
| 50 | Monitoreo de rendimiento | 🟡 Media | Implementar herramientas de monitoreo para detectar caídas del sistema. |
| 51 | **Fondo de operatividad** | 🔴 Alta | **Sistema que permita gestionar los fondos generados por comisiones para el mantenimiento de la plataforma.** |

---

### 12. Módulo de Comunicación y Marketing

| # | Funcionalidad | Prioridad | Descripción |
|---|---------------|-----------|-------------|
| 52 | Boletines informativos | 🟢 Baja | Enviar boletines a los usuarios con novedades de la plataforma. |
| 53 | Notificaciones por correo de pedidos | 🔴 Alta | Enviar correos automáticos de confirmación y seguimiento de pedidos. |
| 54 | Integración con redes sociales | 🟢 Baja | Permitir compartir productos en redes sociales. |

---

## 📊 RESUMEN DE FUNCIONALIDADES FUTURAS

| Prioridad | Cantidad |
|-----------|----------|
| 🔴 Alta | 14 |
| 🟡 Media | 21 |
| 🟢 Baja | 19 |
| **TOTAL** | **54** |

---

## 📋 FUNCIONALIDADES DESTACADAS POR SU IMPACTO

| # | Funcionalidad | Impacto esperado |
|---|---------------|------------------|
| 1 | **Activación del Suplidor** | Permitir intermediarios regulados por ONPECO, ampliando la cadena de valor. |
| 2 | **Comisión porcentual para operatividad** | Garantizar la sostenibilidad económica de la plataforma y del personal. |
| 3 | **Pantalla de bienvenida con imagen de fondo** | Mejorar la identidad visual y la experiencia del usuario. |
| 4 | **Aplicación móvil (PWA)** | Aumentar el acceso desde dispositivos móviles. |
| 5 | **Pago con tarjeta de crédito** | Facilitar las transacciones y aumentar las ventas. |
| 6 | **Notificaciones push** | Mejorar la comunicación y el engagement de los usuarios. |
| 7 | **Geolocalización de productos** | Optimizar la logística y reducir tiempos de entrega. |
| 8 | **Gestión de comisiones** | Dar a ONPECO y al Acopio control sobre los ingresos generados. |

---

## 🎯 RECOMENDACIONES ESTRATÉGICAS PARA FUTURAS VERSIONES

| Fase | Recomendación | Funcionalidades asociadas |
|------|---------------|---------------------------|
| **Fase 1** (Corto plazo) | Mejoras de experiencia de usuario | #9, #45 (Pantalla de bienvenida), #43 (PWA) |
| **Fase 2** (Mediano plazo) | Módulo de sostenibilidad económica | #20, #23, #36, #51 (Comisiones y operatividad) |
| **Fase 3** (Mediano plazo) | Ampliación de roles | #4 (Activación del Suplidor) |
| **Fase 4** (Largo plazo) | Integraciones avanzadas | #5 (Geolocalización), #17 (Pagos) |

---

## ✅ CONCLUSIÓN

El sistema **VPJ** ha sido desarrollado con una arquitectura modular que permite la incorporación de nuevas funcionalidades de manera gradual. Las funcionalidades aquí documentadas representan la visión de futuro del proyecto y están listas para ser evaluadas e implementadas en versiones posteriores, de acuerdo con las necesidades y recursos de ONPECO.

**Especial atención merecen:**

1. **La reactivación del rol Suplidor**, que requiere una política clara de ONPECO.
2. **El sistema de comisiones**, que garantizaría la sostenibilidad de la plataforma.
3. **La mejora visual de la página de inicio**, que fortalecería la identidad de la marca VPJ.

---

## 📋 NOTA FINAL

Las funcionalidades aquí documentadas como **"Fuera del alcance"** no forman parte del proyecto actual, pero quedan registradas para futuras versiones. Este documento demuestra que el equipo de desarrollo ha considerado múltiples escenarios y está preparado para la evolución del sistema.

---

**Última actualización:** 08 de julio de 2026

---

*Documento elaborado por el Grupo #5 - Monográfico #59 - Escuela de Informática - UASD*