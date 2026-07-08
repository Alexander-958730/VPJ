"# VPJ - Venta Precio Justo" 
# VPJ - Venta Precio Justo

**Plataforma de comercio justo para ONPECO**

---

## 📋 Descripción

VPJ (Venta Precio Justo) es una plataforma digital desarrollada para **ONPECO** por el **Grupo #5 del Monográfico #59** de la **Escuela de Informática de la Universidad Autónoma de Santo Domingo (UASD)**.

La aplicación conecta directamente a **productores agrícolas de la provincia de Azua** con **consumidores finales**, eliminando intermediarios especulativos y garantizando precios justos para ambas partes.

---

## 🚀 Tecnologías Utilizadas

| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| Python | 3.12.9 | Lenguaje de programación |
| Django | 4.2.7 | Framework web |
| PostgreSQL | 14+ | Base de datos |
| Daphne | 4.2.2 | Servidor ASGI (WebSockets) |
| Bootstrap 5 | 5.3.0 | Diseño y estilos |
| Chart.js | 4.4.0 | Gráficos y reportes |
| OpenPyXL | 3.1.5 | Exportación a Excel |

---

## 👥 Roles del Sistema

| Rol | Usuario de prueba | Contraseña | Función principal |
|-----|-------------------|------------|-------------------|
| **Consumidor** | bartolo | bartolo123 | Compra productos, califica, denuncia |
| **Productor** | nancy | nancy123 | Publica productos, vende, balance |
| **ONPECO (Regulador)** | onpeco_regulador | regulador123 | Supervisa, gestiona denuncias, backups |
| **Centro de Acopio** | centro_acopio | acopio123 | Gestiona pedidos y pagos |
> **Nota sobre el rol Suplidor:**  
> El código del rol **Suplidor** está implementado en el sistema, pero fue **desactivado** por decisión de ONPECO. La organización prefirió probar primero el modelo de venta directa (Productor → Consumidor) antes de incorporar intermediarios.  
>  
> Si en el futuro la logística lo requiere, el rol Suplidor puede ser **reactivado** fácilmente, ya que todo el código y la lógica de trazabilidad de precios están funcionando.

---

## 📂 Documentación

| Documento | Descripción |
|-----------|-------------|
| [DOCUMENTACION.md](DOCUMENTACION.md) | Documentación técnica completa (133 fases) |
| [Manual del Usuario.md](Manual%20del%20Usuario.md) | Manual de usuario para los 4 roles |
| [MANUAL_INSTALACION.md](MANUAL_INSTALACION.md) | Manual de instalación paso a paso |
| [ALCANCES.md](ALCANCES.md) | Documento de alcances del proyecto por módulo |
| [AVANCES.md](AVANCES.md) | Resumen de avances del proyecto (144 funcionalidades) |
| [Documentacion plantilla universidad.docx](Documentacion%20plantilla%20universidad.docx) | Plantilla de documentación universitaria (formato APA 7) |

---

## 🛠️ Instalación Rápida

### 1. Clonar el repositorio
```bash
git clone https://github.com/Alexander-958730/VPJ.git
cd VPJ
