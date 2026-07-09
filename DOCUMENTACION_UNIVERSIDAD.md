REPÚBLICA DOMINICANA
UNIVERSIDAD AUTÓNOMA DE SANTO DOMINGO
FACULTAD DE CIENCIAS
Escuela de Informática
                                        
TÍTULO DEL PROYECTO
                              Ventas Precio Justo ONPECO-UASD
                                                    Sustentante
Manuel Alexander Hernández Contreras
                           Alexander Trinidad Ramírez
                                       Elizabeth Ogando Rosa

                                                  Coordinador
                                Lic. Erik Minor Cordero
                                             Asesor Metodológico
                   Maestra Yacqueline Tejada Tio
                       Santo Domingo, República Dominicana, Distrito Nacional
 Junio del año 2026

                                               REPÚBLICA DOMINICANA
UNIVERSIDAD AUTÓNOMA DE SANTO DOMINGO
FACULTAD DE CIENCIAS
Escuela de Informática
     
TÍTULO DEL PROYECTO
Ventas Precio Justo ONPECO-UASD
Sustentantes
Manuel Alexander Hernández Contrera_________100476805
Alexander Trinidad Ramirez__________________958730
Elizabeth Ogando Rosa __________________CG5074

Coordinador
Lic. Erik Minor Cordero
Asesor Metodológico
Maestra Yacqueline Tejada Tio
Santo Domingo, República Dominicana, Distrito Nacional
Junio del año 2026




Ventas Precio Justo ONPECO-UASD  
FICHA GENERAL DEL PROYECTO
Información principal y autorización del proyecto
Fecha: 28/05/2026	Nombre del Proyecto:
Venta s Precio Justo ONPECO-UASD
Coordinador del proyecto:	Lic. Erik Minor Cordero
Asesor del proyecto:	Metodológico: Maestra Yacqueline Tejada Tio
Contenido: Martha Lidia Pérez Medina
	Miembros del proyecto:                                Manuel Alexander Hernández Contrera
Alexander Trinidad Ramírez
	Elizabeth Ogando Rosa

	

28/05/2026	Fecha tentativa de finalización:
29/06/2026
	Necesidad del proyecto:
	La creciente necesidad de optimización y modernización para la comercialización de los productos agrícolas en la provincia de Azua. Surge debido a la existencia de intermediarios que influyen en la fijación de los precios, afectando tanto a los productores como a los consumidores. Muchos agricultores venden sus productos a precios reducidos, mientras que los consumidores los adquieren a un costo más elevado, generando desigualdad en el proceso de comercialización. La implementación de esta plataforma permitirá centralizar las ofertas de productos agrícolas, facilitar la comunicación directa entre productores y consumidores, mejorar el acceso a la información sobre los precios, disponibilidad de productos, fortalecer la visibilidad de los productos locales, contribuir a promover un comercio más justo, eficiente, competitivo dentro del sector agrícola de la provincia de Azua.
Tabla 1 Ficha General
INDICE
[Generar índice automático con actualización dinámica mediante Microsoft Word]



















INTRODUCCIÓN
El presente documento constituye el informe monográfico del proyecto “Ventas Precio Justo ONPECO-UASD” (denominado técnicamente como “VPJ”), desarrollado como parte de los requisitos académicos de la Escuela de Informática de la Universidad Autónoma de Santo Domingo (UASD). El proyecto surge a partir de una problemática concreta identificada en la provincia de Azua, República Dominicana, donde pequeños y medianos productores agrícolas enfrentan dificultades estructurales para comercializar sus productos debido a la intervención de intermediarios que fijan precios desfavorables, afectando tanto los ingresos de los agricultores como el costo final que pagan los consumidores en la canasta familiar.
El objetivo principal de este trabajo es desarrollar una plataforma digital que permita la interacción directa entre productores, consumidores y suplidores, eliminando progresivamente los eslabones innecesarios en la cadena de comercialización. La aplicación, construida con Python y el framework Django, incorpora funcionalidades clave como registro diferenciado de usuarios por roles (consumidor, productor, suplidor y regulador ONPECO), publicación y gestión de productos agrícolas, un sistema formal de denuncias por precios abusivos con seguimiento y ticket único, chat en tiempo real mediante WebSockets, respaldos automáticos de la base de datos, y un portal exclusivo para el ente regulador ONPECO con gráficos estadísticos y ranking de productos más consultados.
El desarrollo del proyecto se ha apoyado en dos encuentros de seguimiento con los representantes de ONPECO. El primero, realizado el 28 de mayo de 2026, permitió identificar la problemática central, los actores involucrados y las funcionalidades prioritarias para la plataforma. El segundo encuentro, llevado a cabo el 16 de junio de 2026, tuvo como objetivo presentar el avance de la plataforma y validar los ajustes necesarios. Como resultado de esta segunda reunión, se acordó la implementación de nuevas funcionalidades orientadas a fortalecer la gestión de pagos y la supervisión del comercio, entre las que se incluyen: el módulo de Centro de Acopio, que permite gestionar pedidos y registrar pagos parciales a productores; la funcionalidad de Balance de Ventas para que los productores visualicen el total vendido, pagado y pendiente; y un sistema de validación avanzada en los formularios de registro que resalta errores específicos y muestra mensajes de éxito visuales. Estas mejoras responden directamente a las necesidades expresadas por ONPECO para garantizar una mayor transparencia en la cadena de comercialización.
La estructura del presente monográfico ha sido organizada siguiendo los lineamientos establecidos por la coordinación académica. En el Capítulo I se presenta la descripción general del proyecto, incluyendo el planteamiento del problema, los objetivos generales y específicos, la justificación o necesidad del proyecto, los antecedentes que contextualizan la iniciativa, el alcance definido para la solución tecnológica, y la descripción de los entregables generados a lo largo del desarrollo. En el Capítulo II se detalla la composición del equipo de trabajo, incluyendo las funciones y responsabilidades de cada miembro, así como la estructura organizacional representada mediante un organigrama. El Capítulo III aborda los aspectos técnicos fundamentales, donde se especifican los requerimientos de hardware y software necesarios para la ejecución del sistema, y se describe la arquitectura técnica implementada, incluyendo los diagramas de conexión de red, conexión eléctrica y conectividad ADSL. El Capítulo IV presenta el presupuesto detallado del proyecto, expresado en pesos dominicanos con precios realistas del mercado local, abarcando recursos humanos, hardware, software, infraestructura y contingencias. El Capítulo V contiene la planificación operativa del proyecto, con la lista de actividades organizadas por etapas, las matrices de secuencia y tiempo que permiten visualizar el orden lógico y la duración estimada de cada tarea, así como la matriz de costos asociada. Finalmente, el Capítulo VI presenta las conclusiones y recomendaciones derivadas del proceso de desarrollo, seguidas de la bibliografía consultada y los anexos que complementan la documentación.
Se invita al lector a recorrer las páginas de este documento con la certeza de que cada sección ha sido desarrollada con rigor técnico y metodológico, reflejando el trabajo colaborativo del equipo sustentante, el acompañamiento de los asesores metodológico y de contenido, y el respaldo institucional de ONPECO, la UASD Recinto Azua, CONASSAN y el Ministerio de Agricultura de la República Dominicana. Todo ello con un propósito claro: contribuir a un comercio más justo, transparente y eficiente para los productores y consumidores de la provincia de Azua.

I.	Resumen Ejecutivo.
El presente proyecto tiene como objetivo desarrollar una aplicación digital para la comercialización de productos agrícolas en la provincia de Azua, con la finalidad de fortalecer la relación directa entre productores y consumidores. La iniciativa surge ante la problemática identificada en el proceso de comercialización de productos agrícolas, donde la presencia de intermediarios provoca que los productores reciban menores beneficios económicos por sus cosechas, mientras que los consumidores adquieren los productos a precios mucho más elevados. Como parte del desarrollo, se realizaron dos encuentros de seguimiento con los representantes de ONPECO. El primero, el 28 de mayo de 2026, permitió identificar la problemática central, los actores involucrados y las funcionalidades prioritarias. El segundo, el 16 de junio de 2026, tuvo como objetivo presentar el avance de la plataforma y validar los ajustes necesarios, lo que resultó en la incorporación de nuevas funcionalidades como el Centro de Acopio, el Balance de Ventas y la validación avanzada de formularios.
La plataforma permite a los productores publicar sus productos, gestionar precios, mostrar la disponibilidad de inventario y promover sus ofertas, mientras que los consumidores pueden comparar precios, visualizar información de los productos y realizar compras de manera más accesible. Además, incluye herramientas de retroalimentación, clasificación de productos por categorías, chat en tiempo real, sistema de denuncias con tickets único, y un portal exclusivo para ONPECO con gráficos estadísticos y rankings. Como parte de las mejoras acordadas en el segundo encuentro, se implementó el módulo de Centro de Acopio para la gestión de pedidos y registro de pagos a productores, el Balance de Ventas que permite a los productores visualizar el total vendido, pagado y pendiente, y un sistema de validación avanzada en los formularios de registro que resalta errores específicos y muestra mensajes de éxito visuales.
Se espera que la implementación de esta solución tecnológica fortalezca la visibilidad de los productos locales, promueva un comercio más justo y transparente, mejore las oportunidades de comercialización para los pequeños y medianos productores, y contribuya a la reducción del costo de la canasta familiar en la provincia de Azua.


II.1. Descripción del proyecto
El proyecto "Ventas Precio Justo ONPECO-UASD" consiste en una plataforma digital que conecta directamente a productores y consumidores agrícolas de Azua, eliminando la intermediación en la comercialización de productos. Su desarrollo se basa en el levantamiento de información realizado con ONPECO, que evidenció la necesidad de una herramienta que centralice la oferta de productos, precios y disponibilidad en la región.
La plataforma integra funcionalidades clave para ambos actores: los productores pueden publicar y gestionar sus productos con precios y stock actualizado; los consumidores pueden buscar, filtrar por categorías y comparar opciones antes de decidir su compra. Adicionalmente, el sistema incluye notificaciones, un buzón de retroalimentación para quejas y sugerencias, y una interfaz sencilla que garantiza la protección de datos personales.
Con estas características, la plataforma facilita la comunicación entre productores y consumidores, promueve un comercio más justo y eficiente, y contribuye a la transparencia en la fijación de precios en la provincia de Azua.
II.2. Objetivo General
Desarrollar, mediante el lenguaje de programación Python, una plataforma digital para la comercialización de productos agrícolas en la provincia de Azua, que permita la interacción directa entre productores y consumidores, facilite el acceso a información sobre precios, oferta y disponibilidad de productos, fortalezca la visibilidad de los productos locales y contribuya a un comercio más justo, transparente y eficiente.
II.3. Objetivos Específicos
	Identificar las necesidades y problemáticas que enfrentan los productores y consumidores agrícolas de la provincia de Azua en el proceso de comercialización de productos.
	Diseñar una plataforma digital que facilite la interacción directa entre productores y consumidores, reduciendo la intermediación para promover un comercio más justo.
	Definir las funcionalidades de la plataforma para permitir la publicación, búsqueda y comparación de productos agrícolas, así como el acceso a información sobre precios, ofertas y disponibilidad.
	Implementar módulos adicionales para la gestión de pedidos, pagos a productores y balance de ventas, en respuesta a los requerimientos surgidos durante el seguimiento con ONPECO.
	Promover la visibilidad y comercialización de los productos locales mediante herramientas tecnológicas que fortalezcan su presencia en el mercado y mejoren las oportunidades de negocio para los productores.
II.4. Necesidad del Proyecto
En la provincia de Azua, los pequeños y medianos productores agrícolas comercializan sus productos a través de intermediarios, utilizando métodos informales como contactos telefónicos y acuerdos verbales. Actualmente no existe una plataforma digital que centralice la oferta, los precios y la disponibilidad de los productos locales. Esta situación obliga a los productores a depender de terceros para vender, reduciendo sus márgenes de ganancia, mientras que los consumidores desconocen qué productos están disponibles, a qué precio y de quién pueden comprarlos directamente.

Esta carencia limita la capacidad de los productores para ampliar su mercado más allá de su entorno inmediato y restringe la transparencia del comercio local, ya que el consumidor no puede comparar precios ni conocer la procedencia de los productos. Además, la información sobre cosechas, precios y ofertas se pierde o desactualiza al depender de canales no estructurados.
Por estas razones, surge la necesidad de desarrollar una plataforma digital que funcione como un mercado virtual para los productos agrícolas de Azua, automatizando desde la publicación de productos con precios actualizados hasta la búsqueda y comparación por parte de los consumidores, eliminando la intermediación y promoviendo un comercio más justo, eficiente y transparente.
La implementación de esta plataforma se justifica por las siguientes razones principales: permite a los productores reducir las dificultades de ventas mediante una mayor visibilidad de sus productos; facilita a los consumidores el acceso a información actualizada sobre precios, ofertas y disponibilidad; disminuye las pérdidas económicas por productos no vendidos; fortalece la comunicación directa entre productores y consumidores; y promueve un comercio más justo y transparente que beneficia a ambos actores.
II.5. Antecedentes del Proyecto
En la provincia de Azua, República Dominicana, la comercialización de productos agrícolas ha dependido históricamente de intermediarios que adquieren las cosechas antes incluso de ser recolectadas, fijando precios que benefician exclusivamente a los eslabones intermedios de la cadena de distribución. Esta práctica ha generado una desigualdad estructural en el mercado local: los pequeños y medianos productores reciben ingresos reducidos por sus productos, mientras que los consumidores finales adquieren los mismos alimentos a precios significativamente elevados, incrementando el costo de la canasta familiar y limitando el acceso a productos frescos.
Según el levantamiento de información realizado mediante entrevistas a los solicitantes del proyecto (ONPECO, UASD Recinto Azua, CONASSAN y Ministerio de Agricultura), no existen antecedentes de intentos formales por resolver esta problemática mediante herramientas tecnológicas. Actualmente, los productores comercializan sus cosechas a través de métodos informales como contactos telefónicos y acuerdos verbales, sin contar con una plataforma digital que centralice la oferta, los precios y la disponibilidad de productos locales. Los consumidores, por su parte, desconocen qué productos están disponibles, a qué precio y de quién pueden comprarlos directamente, lo que perpetúa la dependencia de intermediarios.
A nivel nacional e internacional, existen plataformas de comercio electrónico agrícola como Agromarket, Algramo o Mercado Libre Agro, pero ninguna de ellas integra en un solo sistema a productores, consumidores y suplidores con un mecanismo formal de denuncia de precios elevados, respaldado por un ente regulador como ONPECO. La mayoría de estas soluciones se limitan a ser mercados virtuales sin capacidad de supervisión, seguimiento de denuncias, trazabilidad de precios o generación de reportes estadísticos para entidades gubernamentales.
Investigaciones previas en el ámbito de la economía colaborativa y el comercio justo, como los estudios de Martínez (2021) sobre mercados digitales para pequeños agricultores en América Latina, demuestran que la transparencia en la fijación de precios y la eliminación de intermediarios pueden incrementar los ingresos de los productores hasta en un 30% y reducir los precios para los consumidores en un 25%. Estos antecedentes respaldan la viabilidad y el impacto potencial del presente proyecto.
Ante esta problemática y la ausencia de soluciones tecnológicas integrales en la provincia de Azua, surge la necesidad de desarrollar "Ventas Precio Justo ONPECO-UASD" (denominada también "VPJ"), una plataforma digital que permita el registro diferenciado de productores, consumidores y suplidores; la publicación y consulta de productos agrícolas; un sistema formal de denuncias de precios abusivos con seguimiento por parte de ONPECO; y herramientas de supervisión como reportes gráficos y backups automáticos. Como resultado de los encuentros de seguimiento con ONPECO, se han incorporado funcionalidades adicionales como el Centro de Acopio para la gestión de pedidos y pagos a productores, el Balance de Ventas para que los productores visualicen el total vendido, pagado y pendiente, y un sistema de validación avanzada en los formularios de registro. El proyecto se desarrolla con Python y Django, bajo la coordinación de la Universidad Autónoma de Santo Domingo (UASD) y el respaldo institucional de ONPECO, CONASSAN y el Ministerio de Agricultura de la República Dominicana.
II.6. ALCANCE DEL PROYECTO
A continuación, se describen los límites y alcance del proyecto "Ventas Precio Justo ONPECO-UASD" (VPJ), definiendo lo que incluye y lo que no incluye la solución desarrollada.
Alcance Funcional (Lo que SÍ incluye el proyecto)
Módulo	Funcionalidades	Estado	Porcentaje
Usuarios	Registro de consumidores, productores y suplidores. Inicio y cierre de sesión. Edición de perfil de usuario. Activación o desactivación de perfil público mediante checkbox. Aprobación de productores y suplidores por parte de ONPECO. Lista de productores y suplidores pendientes de aprobación. Perfil público visible del productor para consumidores. Lista de productores públicos con buscador. Validación de correo electrónico y nombre de usuario duplicado en el registro. Mensaje de éxito grande con botón para iniciar sesión después del registro. Errores en campos específicos resaltados en rojo. Redirección a la página de inicio de sesión después del registro exitoso.	
Completado

100%
Marketplace	Publicación de productos por productores y suplidores aprobados. Edición y eliminación de productos. Catálogo de productos para consumidores. Detalle de producto con contador de visitas. Alertas automáticas de stock bajo. Clasificación de productos por categorías. Búsqueda de productos por nombre. Ranking de Productos Más Consultados visible para ONPECO. Declaración de productor origen por parte de suplidores.	
Completado

100%

Carrito de Compras	Agregar productos al carrito. Actualizar cantidades de productos. Eliminar productos del carrito. Vaciar el carrito completamente. Resumen del carrito con total de ítems y total a pagar.	
Completado

100%
Pedidos	Proceso de checkout con selección de tipo de entrega (domicilio o recoger en punto de venta). Creación de pedido con Centro de Acopio como vendedor. Historial de pedidos del consumidor. Detalle de pedido específico para el consumidor. Mis ventas para productores. Detalle de venta para productores. Actualización de estado del pedido por productor (confirmar, preparar, entregar, cancelar). Actualización de estado del pedido por Centro de Acopio.	
Completado


100%
Centro de Acopio	Visualización de todos los pedidos recibidos. Detalle de pedido con desglose de pagos por productor. Actualización de estado del pedido. Registro de pagos a productores con montos parciales. Visualización de estado de pago general del pedido (pendiente, parcial, pagado)	
Completado

100%
Balance de Ventas	Visualización de Total Vendido, Total Pagado y Pendiente de Pago para productores. Historial de ventas con detalle de productos vendidos por pedido. Estado de pago por pedido (pendiente, parcial, pagado).	
Completado

100%
Denuncias	Creación de denuncias por consumidores. Tipos de denuncia: precio abusivo, mala calidad, problema con entrega y otros. Prioridad: alta, media o baja. Ticket único con formato CD-XXXXXX. Historial de seguimiento con cambios de estado. Estados: pendiente, en investigación, resuelto y rechazado. Gestión de denuncias por ONPECO con cambio de estado y comentarios. Listado de mis denuncias para consumidores. Gráfico de denuncias por mes con Chart.js para ONPECO	Completado
100%
Reputación y Calificaciones	Calificación de productores por consumidores con estrellas de 1 a 5. Promedio de calificación visible en perfil del productor. Gestión de reputación por ONPECO (Excelente, Bueno, Regular, Malo, Pésimo). Ranking de productores y suplidores con calificaciones visible para ONPECO. Ranking de productores más denunciados visible para ONPECO.	
Completado

100%
Exportaciones	Exportación de denuncias a PDF. Exportación de denuncias a Excel. Exportación de listado de productores a PDF.	Completado 	
100%
Chat en Tiempo Real	Comunicación instantánea entre consumidores y productores mediante WebSockets. Salas de chat privadas por pareja de usuarios. Mensajería en tiempo real con Daphne. Historial de conversaciones en Mis Conversaciones.	Completado 	
100%
Portal ONPECO	Dashboard con tarjetas de indicadores clave de rendimiento. Aprobación de productores y suplidores pendientes. Gestión completa de denuncias con cambio de estado y comentarios. Gráfico de denuncias por mes. Ranking de productos más consultados. Ranking de productores más denunciados. Ranking de productores y suplidores con calificaciones. Gestión de reputación. Gestión de backups del sistema.	
Completado

100%
Backups	Backup automático diario a las 2:00 AM. Creación de puntos de restauración manuales desde interfaz web. Restauración de la base de datos desde backup existente. Limpieza automática manteniendo los últimos 10 backups.	Completado

100%
Interfaz y Usabilidad	Diseño responsive con Bootstrap 5 para computadoras y dispositivos móviles. Navegación dinámica según rol del usuario. Mensajes de éxito y error con notificaciones visuales. Formato de números con punto para decimales y coma para miles (estilo República Dominicana). Validación de formularios con errores en campos específicos resaltados en rojo. Mensajes de éxito grandes y visuales en el registro con botón para iniciar sesión.	
Completado


100%
Tabla 2 Alcance Funcional
2.6.2. Alcance Técnico (Infraestructura desarrollada)
Componente	Descripción
Backend	Python 3.12 con framework Django 5.x
Base de Datos	SQLite3 (base de datos por defecto de Django)
Servidor ASGI	Daphne para soporte de WebSockets (chat en tiempo real)
Frontend	Bootstrap 5, Chart.js, Font Awesome, HTML5, CSS3
Reportes	Generación de gráficos de denuncias con Chart.js. Exportación pendiente para versiones futuras.
Backups	JSON nativo con datos serializados (dumpdata de Django)
Tabla 3 Alcance Técnico
2.6.3. Usuarios Alcanzados
A continuación, se detallan las capacidades de cada rol de usuario dentro de la plataforma:
Rol	Capacidades dentro del alcance
Consumidor	Registrarse, ver catálogo de productos, ver detalle de productos, crear denuncias, ver seguimiento de sus denuncias, contactar a productores por chat.
Productor	Registrarse (requiere aprobación de ONPECO), publicar/editar/eliminar productos, gestionar stock, recibir mensajes de consumidores por chat, ver productos propios.
Suplidor	Registrarse (requiere aprobación de ONPECO), publicar productos (declarando productor origen y precio de compra), gestionar inventario.
Regulador (ONPECO)	Acceso a portal exclusivo, aprobar productores y suplidores, gestionar todas las denuncias, visualizar reportes gráficos, ver ranking de productos más consultados, gestionar backups del sistema.
Administrador	Acceso al panel de administración de Django (localhost/admin). Gestión completa de usuarios, productos y denuncias.
Tabla 4 Usuarios Alcanzados

2.6.4. Lo que NO incluye el proyecto (Fuera del alcance)
Ítem	Justificación
Pasarela de pagos en línea (tarjeta de crédito, PayPal, Yappy, transferencia bancaria)	El sistema registra pedidos y genera órdenes de compra, pero no procesa pagos electrónicos. El pago se acuerda entre consumidor, Centro de Acopio y productores fuera de la plataforma (contraentrega o pago por separado).
Módulo de logística o envíos	No se implementa seguimiento de entregas, rutas de distribución ni integración con servicios de mensajería.
Aplicación móvil nativa (iOS o Android)	La plataforma es web responsive, accesible desde navegadores móviles, pero no se desarrollaron aplicaciones nativas.
Geolocalización o mapas	No se implementa visualización de productores en mapas ni cálculo de distancias.
Multi-idioma	El sistema opera exclusivamente en español.
Despliegue en servidor en la nube	El proyecto se entrega funcional en entorno local (localhost); el despliegue en producción no está dentro del alcance.
Exportación de productos a Excel PDF	No implementado dentro del alcance del proyecto. Solo está disponible la exportación de denuncias y listado de productores.
Notificaciones por correo electrónico o push	Las notificaciones son únicamente visuales dentro de la plataforma (mensajes Django).
Tabla 5 NO incluye el proyecto


2.6.5. Condiciones de operación
El sistema ha sido desarrollado y probado en entorno Windows 10 y 11. El acceso a la plataforma se realiza a través de la dirección local http://127.0.0.1:8000, pudiendo también configurarse para acceso en red local mediante el ajuste de la dirección IP. Para su correcta ejecución, se requiere contar con Python 3.11 o superior, pip, un entorno virtual y todas las dependencias listadas en el archivo requirements.txt. El inicio del sistema se realiza ejecutando el comando daphne core. asgi:application desde la terminal, con el entorno virtual previamente activado.
2.6.6. Cobertura geográfica
El proyecto se enfoca exclusivamente en la provincia de Azua, República Dominicana, como caso piloto. Los productores, consumidores y suplidores registrados pertenecen o comercializan productos en esta región. La escalabilidad a otras provincias queda fuera del alcance del presente proyecto
2.7. Descripción de los entregables del proyecto
A continuación, se enumeran y describen los entregables generados durante el desarrollo del proyecto "Ventas Precio Justo ONPECO-UASD" (VPJ), desde la fase de levantamiento de información hasta la entrega final del sistema funcional.
E01. Informe de levantamiento de información: Documento que recoge los resultados de la entrevista realizada a los solicitantes del proyecto, incluyendo ONPECO, UASD, CONASSAN y el Ministerio de Agricultura. Contiene la identificación del problema de intermediarios, las consecuencias para productores y consumidores, los actores involucrados, las funcionalidades deseadas y las expectativas del proyecto. (Entregado)
E02. Informe de análisis del sistema: Documento que describe el análisis de la problemática actual, la identificación de requerimientos funcionales y no funcionales, la definición de roles de usuario (productor, consumidor, suplidor, regulador ONPECO), y la especificación de los módulos necesarios: autenticación, marketplace, denuncias, chat y respaldos. (Entregado).
E03. Prototipo no funcional: Diseño de la estructura de la base de datos (modelos: User, Product, Complaint, ComplaintUpdate) y diseño de las principales interfaces de usuario, incluyendo mockups de registro, login, catálogo de productos, formulario de denuncias y portal ONPECO. (Entregado).
E04. Prototipo funcional (versión alpha): Implementación inicial del sistema con funcionalidades operativas como registro y autenticación de usuarios, creación de productos, visualización de catálogo, sistema de denuncias con tickets únicos y panel administrativo básico. Incluye la configuración del entorno Django con SQLite. (Entregado).
E05. Sistema completo versión final: Entregable final que incluye todas las funcionalidades completadas, probadas y documentadas. Este entregable abarca los módulos de usuarios, marketplace, carrito de compras y pedidos, centro de acopio con gestión de pagos, balance de ventas, denuncias con tickets único y seguimiento, reputación y calificaciones, exportaciones a PDF y Excel, chat en tiempo real con WebSockets, portal ONPECO con gráficos y rankings, backups automáticos, e interfaz de usuario responsive. (Entregado).
E06. Manual de usuario: Documento guía para cada tipo de usuario (consumidor, productor, suplidor, regulador ONPECO, centro de acopio) explicando paso a paso cómo registrarse, publicar productos, crear denuncias, aprobar usuarios, gestionar pagos y utilizar el chat. (Entregado).
E07. Acta de conformidad: Documento firmado por ONPECO al finalizar el proyecto, confirmando que el sistema cumple con los alcances acordados y que ha sido recibido a satisfacción. (Pendiente de firma).
Los submódulos incluidos en el entregable E05 (Sistema completo versión final) son los siguientes:
E05.1 Módulo de usuarios: Registro diferenciado para productores, consumidores y suplidores. Inicio y cierre de sesión. Perfil de usuario editable. Aprobación manual de productores y suplidores por ONPECO.
E05.2 Módulo de marketplace: Publicación, edición y eliminación de productos. Visualización de catálogo con tarjetas. Detalle de producto con contador de visitas. Alertas de stock bajo. Clasificación por categorías.
E05.3 Módulo de denuncias: Creación de denuncias por consumidores con tipo (precio, calidad, entrega, otro) y prioridad (alta, media, baja). Asignación de ticket único con formato CD-XXXXXX. Historial de seguimiento con cambios de estado (pendiente, en investigación, resuelto, rechazado). Gestión completa por ONPECO.
E05.4 Portal ONPECO (Regulador): Dashboard exclusivo con menú lateral. Aprobación de productores y suplidores. Gestión de todas las denuncias del sistema. Reporte gráfico de denuncias por mes utilizando Chart.js. Ranking de productos más consultados.
E05.5 Sistema de respaldos (backups): Generación manual de puntos de restauración desde interfaz web. Backup automático programado diariamente a las 2:00 AM mediante Programador de Tareas de Windows. Almacenamiento en formato JSON en carpeta backups. Listado de respaldos disponibles con fecha y tamaño.
E05.6 Módulo de chat en tiempo real: Comunicación instantánea entre consumidores y productores mediante WebSockets. Salas de chat privadas por pareja de usuarios. Botón "Contactar al productor" en perfil público. Servidor Daphne configurado como ASGI.
E05.7 Reportes y estadísticas: Gráfico de denuncias mensuales con Chart.js. Tabla de productos más vistos ordenados por contador de visitas. Acceso exclusivo para reguladores ONPECO.
E05.8 Interfaz de usuario: Plantillas HTML con Bootstrap 5 y diseño responsive. Navegación dinámica según rol del usuario. Mensajes de éxito y error mediante sistema de notificaciones de Django.
E05.9 Documentación técnica: Archivo DOCUMENTACION.md con registro detallado de fases de desarrollo, comandos ejecutados, problemas encontrados y soluciones aplicadas.
Forma de entrega del sistema final (E05):
Se entrega la carpeta completa "cosecha_directa" con todas las aplicaciones Django, templates, archivos estáticos y configuración. Se incluye el archivo "db.sqlite3" con la estructura de tablas y datos de prueba, así como el archivo "requirements.txt" con todas las dependencias necesarias como Django, daphne, channels y pillow. Se proporcionan instrucciones para activar el entorno virtual y ejecutar el comando "daphne core. asgi:application". La carpeta "backups" contiene ejemplos de puntos de restauración generados durante el desarrollo. Se adjuntan los archivos de documentación "DOCUMENTACION.md" y "README.md" con instrucciones de instalación, configuración y uso. Finalmente, se incluyen los anexos: guía de entrevista (A01), diccionario de datos físico de la base de datos (A02) y manual de usuario (A03).
Observaciones sobre los entregables:
Todos los entregables han sido desarrollados en el marco de la Universidad Autónoma de Santo Domingo (UASD), Facultad de Ciencias, Escuela de Informática. El sistema fue desarrollado en su totalidad en Python con Django y probado en entorno Windows 10 y 11. La funcionalidad de exportación de reportes a Excel y PDF se encuentra disponible para denuncias y listado de productores. El despliegue en servidor de producción no está incluido; el sistema se entrega para ejecución en entorno local.

II.	Equipo De Trabajo.
Miembros del proyecto.
Manuel A Hernández Contreras         100476805
Elizabeth Ogando Rosa                       CG-5074
Alexander Trinidad Ramírez                958730


Organigrama del proyecto.






















3.3. Descripción de las funciones y responsabilidades
A continuación, se detallan las funciones y responsabilidades de cada miembro del equipo según su rol en el proyecto.
Alexander Trinidad Ramírez (Analista de sistema): Realizó el levantamiento de requerimientos funcionales y no funcionales mediante entrevistas a productores, suplidores, consumidores y personal de ONPECO, así como la observación directa de sus procesos. Elaboró los informes de levantamiento y análisis del sistema, incluyendo diagramas de casos de uso, flujos de trabajo y especificación de requisitos. Validó que el prototipo funcional y el entregable final cumplieran con la documentación generada.
Alexander Trinidad Ramírez (Soporte de Usuarios y Redes): Brindó asistencia técnica a los usuarios finales durante la fase de pruebas y despliegue, resolviendo dudas sobre el uso del sistema. Configuró el entorno de hosting o servidor para el despliegue de la aplicación y garantizó la disponibilidad y seguridad básica de la red y el servicio. Elaboró el manual de usuario.
Manuel Alexander Hernández Contreras (Programador): Participó activamente en el desarrollo de la aplicación en el backend con Python y Django. Colaboró en la redacción del monográfico y asistió a las reuniones de seguimiento. Fue el encargado principal del módulo de denuncias y del sistema de respaldos (backups).
Manuel Alexander Hernández Contreras (Líder del proyecto): Supervisó el avance del proyecto, aprobó los entregables, coordinó con la asesora metodológica y evaluó el cumplimiento de los objetivos del monográfico.
Elizabeth Ogando Rosa (Analista de prueba): Diseñó y ejecutó casos de prueba funcionales y no funcionales sobre el sistema. Identificó errores, los documentó en un informe de incidencias y coordinó con el programador las correcciones necesarias. Realizó pruebas de integración, aceptación y rendimiento, verificando que el sistema cumpliera con el alcance definido antes de cada entrega.

Elizabeth Ogando Rosa (Analista de infraestructura): Diseñó y gestionó la infraestructura tecnológica necesaria para el despliegue del sistema. Seleccionó y configuró el servicio de hosting o cloud computing, gestionó la base de datos en producción y aseguró la escalabilidad y disponibilidad del sistema. Elaboró el manual técnico de despliegue y mantenimiento.
Profesora Yacqueline Tejada Tio (Asesora metodológica): Orientó al equipo en la aplicación del método de investigación. Revisó y corrigió la estructura del monográfico, asegurando que el documento cumpliera con los estándares académicos de la UASD y validando la coherencia entre los objetivos y los resultados presentados.
Lic. Erik Minor Cordero (Coordinador del proyecto): Supervisó el avance general del proyecto, revisó y aprobó los entregables, coordinó reuniones de seguimiento con el equipo de desarrollo, garantizó el cumplimiento de los plazos establecidos y actuó como enlace principal entre el equipo y las autoridades de la facultad.
Martha Lidia Pérez Medina (Asesora de contenido): Validó la pertinencia técnica del proyecto, revisó la documentación relacionada con el desarrollo de la aplicación, aseguró que la solución tecnológica respondiera a las necesidades identificadas y orientó sobre buenas prácticas de desarrollo de software.
3.4. Actores externos colaboradores
Además del equipo de trabajo interno, el proyecto contó con la colaboración y participación de las siguientes instituciones y personas durante el levantamiento de información y validación de requisitos:
ONPECO (Oficina Nacional de Protección al Consumidor) fue la entidad solicitante del proyecto, proporcionando la problemática, necesidades y funcionalidades deseadas, y participando en la entrevista de levantamiento de información. Por parte de ONPECO, participaron Rita González (Coordinadora ejecutiva), responsable principal del proyecto; Leonor González (Coordinadora operativa), quien colaboró en la definición de requerimientos funcionales; Leonel A. Rivas P. (Coordinador técnico), quien aportó lineamientos técnicos y normativos para el sistema de denuncias; y Nayelis Cabreras (Administración), quien colaboró en la logística de las reuniones y entrevistas.
La UASD Recinto Azua facilitó el contacto con productores agrícolas de la provincia de Azua. CONASSAN (Secretaría Técnica del Consejo Nacional para la Soberanía y Seguridad Alimentaria y Nutricional) aportó información sobre políticas de seguridad alimentaria. El Ministerio de Agricultura, representado por Daniel Velas, validó la pertinencia del proyecto para el sector agrícola dominicano.
Descripción De Los Aspectos Técnicos.
4.1. Requerimientos de hardware
A continuación, se especifican los requerimientos mínimos y recomendados de hardware para la correcta ejecución del sistema en el entorno del cliente (ONPECO, productores y consumidores).
Objeto	Descripción (Mínimo)	Descripción (Recomendado)
Procesador (CPU)	Intel Core i3 o AMD equivalente (2.0 GHz)	Intel Core i5 o superior (2.5 GHz o más)
Memoria RAM	4 GB	8 GB o superior
Almacenamiento (Disco duro)	10 GB de espacio libre (disco duro mecánico HDD)	20 GB de espacio libre (unidad de estado sólido SSD)
Resolución de pantalla	1366 x 768 píxeles	1920 x 1080 píxeles o superior
Conexión a internet	2 Mbps (para navegación básica)	5 Mbps o superior (para chat en tiempo real y carga de imágenes)
Dispositivo de entrada	Teclado y mouse (ratón)	Teclado, mouse y cámara web (opcional para videollamadas futuras)
Smartphone / Tablet	No requerido (acceso opcional mediante navegador móvil)	Compatible con navegadores modernos (Chrome, Firefox, Safari)
Tabla 6 Requerimientos de hardware

Nota: Al ser una aplicación web responsive, los consumidores podrán acceder desde dispositivos móviles (teléfonos inteligentes y tabletas) siempre que cuenten con un navegador actualizado y conexión a internet estable.
4.2.1. Dependencias de Python (requirements.txt)
Librería / Paquete	Versión	Propósito
Django	6.0.6	Framework web principal
daphne	4.0.0	Servidor ASGI para WebSockets y chat
channels	4.0.0	Soporte para WebSockets en Django
channels-redis	4.1.0	Backend para capas de canales (opcional, producción)
Pillow	Última	Manejo de imágenes (carga de fotos de productos)
openpyxl	Última	Exportación a Excel
reportlab	Última	Generación de PDFs
xhtml2pdf	Última	Conversión de HTML a PDF
Tabla 7 Dependencias de Python (requirements.txt)
4.2.4. Herramientas de desarrollo utilizadas
Para el desarrollo del sistema se utilizaron las siguientes herramientas:
Herramienta	Propósito
Visual Studio Code (VS Code)	Editor de código principal
Terminal de Windows / CMD	Ejecución de comandos, entorno virtual, servidor Daphne
Git	Control de versiones (opcional)
Programador de tareas de Windows	Backup automático diario (ejecución programada de auto_backup.bat)
Django admin panel	Gestión de usuarios y datos (http://127.0.0.1:8000/admin)

Tabla 8 Herramientas de desarrollo utilizadas
4.3. Arquitectura técnica del proyecto
A continuación, se describe la arquitectura técnica implementada en el sistema "Ventas Precio Justo ONPECO-UASD".
4.3.1. Arquitectura general del sistema
El sistema sigue una arquitectura cliente-servidor basada en el patrón MVT (Model-View-Template) de Django, con capas adicionales para soporte de WebSockets mediante Daphne y Channels. Esta arquitectura permite manejar tanto peticiones HTTP tradicionales como conexiones persistentes para el chat en tiempo real.
El cliente (navegador web) se comunica con el servidor a través de HTTP para las operaciones convencionales (visualización de páginas, envío de formularios, etc.) y a través de WebSockets para la mensajería instantánea. El servidor Daphne actúa como interfaz ASGI, recibiendo las peticiones y dirigiéndolas al módulo correspondiente. Las peticiones HTTP son procesadas por Django, mientras que las conexiones WebSocket son manejadas por Django Channels.
La base de datos SQLite3 almacena toda la información del sistema: usuarios, productos, pedidos, denuncias y configuraciones. Los respaldos automáticos se generan en formato JSON y se almacenan en la carpeta /backups.
4.3.2. Estructura de carpetas del proyecto
El proyecto se organiza en una estructura de carpetas que separa claramente las responsabilidades. La carpeta "core" contiene la configuración principal de Django.
La carpeta "apps" agrupa todas las aplicaciones del sistema: "users" para la gestión de usuarios y roles, "marketplace" para el catálogo de productos, "complaints" para el sistema de denuncias, "chat" para la mensajería en tiempo real, y "cart" para el carrito de compras y pedidos. Las carpetas "templates", "static" y "media" contienen las plantillas HTML, los archivos estáticos y los archivos subidos por los usuarios respectivamente.
4.3.3. Diagrama de conexión de red
El sistema está diseñado para funcionar en un entorno local, accesible a través de la dirección http://127.0.0.1:8000. Para acceso desde otros equipos en la misma red local, se puede iniciar Daphne con el parámetro -b 0.0.0.0, permitiendo que otros dispositivos se conecten utilizando la dirección IP del servidor.
4.3.4. Tecnologías y estándares utilizados
El sistema utiliza Python 3.12 como lenguaje de programación principal, Django 6.0.6 como framework web, Daphne 4.0.0 como servidor ASGI para WebSockets, y SQLite3 como base de datos. En el frontend se utilizan HTML5, CSS3, Bootstrap 5 para el diseño responsive, Chart.js para gráficos estadísticos y Font Awesome para iconografía. La comunicación en tiempo real se realiza mediante el protocolo WebSocket.
4.3.5. Diagramas de conexión eléctrica
Dado que el sistema será desplegado en la nube, la infraestructura eléctrica es responsabilidad del proveedor de servicios cloud. El proveedor garantiza la alimentación eléctrica continua, sistemas de respaldo y refrigeración para los servidores. Por lo tanto, no se requiere infraestructura eléctrica adicional por parte del cliente (ONPECO) más allá de un equipo con conexión a internet para acceder a la plataforma.
4.3.6. Diseño de conexión ADSL / Internet (acceso desde la nube)
El sistema estará alojado en la nube, por lo que los usuarios solo necesitan una conexión a internet estable para acceder a la plataforma a través de un navegador web.
Se recomienda una conexión con velocidad mínima de 2 Mbps para navegación básica y 5 Mbps o superior para el uso del chat en tiempo real y la carga de imágenes. La conexión debe soportar WebSockets, por lo que se requiere una latencia baja (menor a 100 ms). En zonas rurales, se recomienda el uso de fibra óptica o 4G/5G si el ADSL tradicional no ofrece estabilidad suficiente.
 
  
Nota: Para acceso desde otros equipos en la misma red local, se debe iniciar Daphne con el comando: daphne -b 0.0.0.0 -p 8000 Core. asgi:application


4.3.4. Tecnologías y estándares utilizados
Tecnología / Estándar	Versión	Uso en el proyecto
Python	3.11+	Lenguaje de programación principal
Django	6.0.6	Framework web (MVT)
Daphne	4.0.0	Servidor ASGI (WebSockets)
Channels	4.0.0	Capa de WebSockets para Django
SQLite	3.x	Base de datos relacional
HTML5	Estándar	Estructura de las páginas web
CSS3	Estándar	Estilos visuales
Bootstrap	5	Framework CSS (diseño responsive)
JavaScript	ES6	Interactividad, gráficos, WebSockets
Chart.js	3.x	Gráficos estadísticos (denuncias por mes)
Font Awesome	6.4.0	Iconografía
JSON	Estándar	Formato de respaldos (backups)
WebSockets	Protocolo	Chat en tiempo real
ASGI	Estándar	Interfaz asíncrona para servidores web
	Tabla 9 Tecnologías y estándares utilizados
	
	
	
	
	
	
	


4.3.7. Diagrama de flujo de datos simplificado
  
4.3.8. Diagrama de conexión para respaldos automáticos
Los respaldos automáticos del sistema se ejecutan diariamente a las 2:00 AM mediante el Programador de Tareas de Windows, que ejecuta el archivo auto_backup.bat ubicado en la carpeta del proyecto.
El script batch activa el entorno virtual de Python y ejecuta el comando python manage.py auto_backup. Este comando genera un archivo JSON con la estructura completa de la base de datos y lo almacena en la carpeta /backups con un nombre que incluye la fecha y hora de creación, como backup_auto_20260608_020915.json.
El sistema mantiene automáticamente los últimos 10 backups, eliminando los más antiguos para evitar el consumo excesivo de espacio en disco. El usuario también puede generar puntos de restauración manuales desde la interfaz web, sin necesidad de acceder al servidor.

    
4.3.6. Diseño de conexión ADSL / Internet
El sistema requiere conexión a internet para que los usuarios (consumidores, productores, suplidores y ONPECO) puedan acceder a la plataforma, así como para el funcionamiento del chat en tiempo real mediante WebSockets.
Se recomienda una conexión a internet con velocidad mínima de 2 Mbps para navegación básica y 5 Mbps o superior para el chat en tiempo real y la carga de imágenes de productos. La conexión debe ser estable, con latencia menor a 100 ms para garantizar el correcto funcionamiento de los WebSockets. Se sugiere fibra óptica o 4G/5G en zonas donde el ADSL tradicional no ofrezca suficiente estabilidad.
El servidor se ejecuta en un equipo local con dirección IP configurable. Para acceso desde otros equipos en la misma red local, se debe iniciar Daphne con el parámetro -b 0.0.0.0 y los usuarios se conectan a través de la dirección IP del servidor en el puerto 8000. En zonas rurales con conexiones lentas, se recomienda optimizar las imágenes de productos comprimiéndolas antes de subirlas y configurar la reconexión automática de WebSockets en caso de interrupciones.
.    

4.3.6. Diseño de conexión ADSL / Internet
El sistema requiere conexión a internet para que los usuarios (consumidores, productores, suplidores y ONPECO) puedan acceder a la plataforma, así como para el funcionamiento del chat en tiempo real mediante WebSockets.
Para el correcto funcionamiento de la plataforma, los usuarios finales deben contar con una conexión a internet que cumpla con los siguientes requisitos: velocidad de bajada mínima de 2 Mbps y recomendada de 5 Mbps o superior; velocidad de subida mínima de 1 Mbps y recomendada de 3 Mbps o superior; latencia menor a 100 ms y recomendada menor a 50 ms para garantizar el correcto funcionamiento del chat en tiempo real con WebSockets. Se recomienda fibra óptica o 4G/5G en zonas donde el ADSL tradicional no ofrezca suficiente estabilidad. La conexión debe ser estable y soportar los protocolos HTTP y WebSockets.
En zonas rurales con conexiones lentas, se recomienda optimizar las imágenes de productos comprimiéndolas antes de subirlas y configurar la reconexión automática de WebSockets en caso de interrupciones.
4.3.6. Diseño de conexión ADSL / Internet
El sistema requiere conexión a internet para que los usuarios puedan acceder a la plataforma, así como para el funcionamiento del chat en tiempo real mediante WebSockets. Para el correcto funcionamiento, los usuarios finales deben contar con una conexión a internet con velocidad de bajada mínima de 2 Mbps y recomendada de 5 Mbps o superior, velocidad de subida mínima de 1 Mbps y recomendada de 3 Mbps o superior, y latencia menor a 100 ms, siendo recomendable menos de 50 ms para garantizar el correcto funcionamiento del chat.
Se recomienda fibra óptica o 4G/5G en zonas donde el ADSL tradicional no ofrezca suficiente estabilidad. En zonas rurales de la provincia de Azua, se sugiere considerar internet por fibra óptica o 4G/5G ante mala cobertura ADSL, optimizar las imágenes de productos comprimiéndolas antes de subirlas para compensar la baja velocidad de subida, y configurar WebSockets con reconexión automática para mantener la comunicación estable ante latencia alta o cortes frecuentes.
La conexión debe ser estable y soportar los protocolos HTTP y WebSockets para el correcto funcionamiento de todas las funcionalidades de la plataforma.
V. PRESUPUESTO
A continuación, se presenta el presupuesto detallado para el desarrollo e implementación del proyecto "Ventas Precio Justo ONPECO-UASD" (VPJ). Los costos se expresan en pesos dominicanos (DOP), utilizando un tipo de cambio referencial de 1 USD = 62 DOP (valor aproximado para junio 2026).
V.1 Recursos Humanos
El equipo de desarrollo está compuesto por tres personas, quienes han trabajado en el proyecto durante aproximadamente 4 semanas, con una dedicación estimada de 6 horas diarias por persona, totalizando 504 horas hombre. Para este proyecto, se utiliza una tarifa de 1,000 DOP por hora (aproximadamente 16 USD por hora), considerando el ámbito académico y la naturaleza no comercial del desarrollo. El costo total en recursos humanos asciende a 504,000 DOP.
V.2 Hardware
Para el desarrollo del proyecto, se utilizan tres computadoras personales con un costo estimado de 45,000 DOP cada una, totalizando 135,000 DOP. Se recomienda adicionalmente un servidor en la nube para el despliegue del sistema, con un costo mensual aproximado de 1,000 DOP, un regulador de voltaje con un costo de 2,000 DOP, un UPS de 5,500 DOP, y un disco duro externo de 1TB para respaldos adicionales con un costo de 3,500 DOP. El total en hardware asciende a 147,000 DOP.
V.3 Software y Licencias
El proyecto utiliza exclusivamente software de código abierto, por lo que no se incurre en costos de licencias. Todas las herramientas utilizadas, incluyendo Python, Django, Daphne, SQLite, Bootstrap, Chart.js y Visual Studio Code, son gratuitas.

V.4 Infraestructura y Conectividad
Se estima un costo mensual de 2,500 DOP para la conexión a internet y 1,800 DOP para el consumo eléctrico del equipo del cliente, totalizando 51,600 DOP anuales.
V.5 Resumen General
El costo total estimado del proyecto asciende a aproximadamente 835,560 DOP, incluyendo recursos humanos (504,000 DOP), hardware (147,000 DOP), infraestructura y conectividad (51,600 DOP), software (0 DOP) y un 10% de contingencias (75,960 DOP) para imprevistos.
Recurso	Cantidad	Horas totales	Tarifa por hora (DOP)	Subtotal (DOP)
Desarrollador Python/Django (Sustentante 1)	1 persona	168 horas	1,000 DOP	168,000 DOP
Desarrollador Python/Django (Sustentante 2)	1 persona	168 horas	1,000 DOP	168,000 DOP
Desarrollador Python/Django (Sustentante 3)	1 persona	168 horas	1,000 DOP	168,000 DOP
Total, Recursos Humanos	3 personas	504 horas	-	504,000 DOP
	
	Tabla 10 Presupuesto de Recursos Humanos





V.2. Presupuesto de Hardware
A continuación, se detallan los equipos y componentes de hardware necesarios para el desarrollo y ejecución del sistema.
Objeto	Descripción	Cantidad	Costo unitario (DOP)	Subtotal (DOP)
Computadora de desarrollo	Laptop/Desktop con procesador Intel Core i5, 8GB RAM, SSD 256GB (equipo existente del equipo desarrollador)	3	45,000 DOP	135,000 DOP
Servidor de producción (recomendado)	Computadora dedicada para ONPECO: Intel Core i5, 16GB RAM, SSD 512GB (para alojar la aplicación y base de datos)	1	55,000 DOP	55,000 DOP
UPS (respaldo de energía)	Respaldo de energía 650VA para proteger el servidor ante cortes de luz (recomendado para zona rural de Azua)	1	5,500 DOP	5,500 DOP
Regulador de voltaje (AVR)	Protección contra fluctuaciones eléctricas	1	2,000 DOP	2,000 DOP
Disco duro externo (Backups)	Almacenamiento externo 1TB para respaldos adicionales de la base de datos	1	3,500 DOP	3,500 DOP
Reuter / Módem	Equipo de red para conectividad (puede ser proporcionado por el ISP)	1	3,000 DOP	3,000 DOP
	Total, Hardware $204,000 DOP                        Tabla 11 Presupuesto de software

V.3. Presupuesto de Software y Licencias
El proyecto utiliza mayormente software de código abierto (open source) sin costos de licencia. A continuación, se detallan los componentes y sus costos asociados:
Objeto	Descripción	Licencia	Costo (DOP)
Sistema Operativo	Windows 10/11 (equipos existentes) o Linux (Ubuntu) – gratuito	Propietario / Open Source	0 DOP (ya incluido en equipos)
Python 3.11+	Lenguaje de programación (código abierto)	Open Source (PSF License)	0 DOP
Django 5.x	Framework web (código abierto)	Open Source (BSD License)	0 DOP
Daphne / Channels	Servidor ASGI y WebSockets (código abierto)	Open Source	0 DOP
SQLite3	Base de datos integrada (código abierto)	Open Source (Public Domain)	0 DOP
Visual Studio Code	Editor de código (gratuito)	Propietario (gratuito)	0 DOP
Pillow	Librería de manejo de imágenes	Open Source	0 DOP
Chart.js	Librería de gráficos JavaScript	Open Source (MIT License)	0 DOP
Bootstrap 5	Framework CSS (código abierto)	Open Source (MIT License)	0 DOP
Font Awesome	Librería de iconos (versión gratuita)	Open Source / Freemium	0 DOP
Navegadores web	Chrome, Firefox, Edge (gratuitos)	Propietario (gratuito)	0 DOP
Antivirus (recomendado)	Protección para el servidor (ej.: Windows Defender gratuito o solución comercial)	Freemium	0 - 5,000 DOP
Total, Software 0 - 5,000 DOP      Table 12 Presupuesto de Software y Licencias
V.4.  Presupuesto de infraestructura y Conectividad
Concepto	Descripción	Periodicidad	Costo mensual (DOP)	Costo anual (DOP)
Conexión a internet	Plan residencial/empresarial de Claro, Altice o Viva. Velocidad mínima recomendada: 10 Mbps (fibra óptica recomendada)	Mensual	2,500 DOP	30,000 DOP
Electricidad	Consumo energético del servidor y equipos de red (estimado: 150 kWh/mes a 12 DOP/kWh	Mensual	1,800 DOP	21,600 DOP
Alojamiento (hosting)	Opcional: despliegue en la nube. Servidores VPS básicos (DigitalOcean, AWS, etc.) desde 15 USD/mes (930 DOP)	Mensual	0 - 1,000 DOP (opcional)	0 - 12,000 DOP (opcional)
Dominio (opcional)	Registro de dominio.com.do (si se despliega en producción)	Anual	0 - 2,000 DOP	0 - 2,000 DOP
	Tabla 13 Presupuesto de Infraestructura y Conectividad
Total, Infraestructura anual aprox. 51,600 DOP (sin opcionales)
V.5. Resumen General del Presupuesto
El costo total estimado del proyecto asciende a aproximadamente 835,560 DOP, distribuido de la siguiente manera: recursos humanos (504,000 DOP), hardware (204,000 DOP), infraestructura y conectividad (51,600 DOP), software y licencias (0 - 5,000 DOP) y un 10% de contingencias (75,960 DOP) para imprevistos.
V.6. Desglose mensual de costos operativos para ONPECO
Una vez implementado el sistema, los costos recurrentes mensuales para ONPECO incluyen mantenimiento y soporte técnico (4 horas mensuales a 1,000 DOP por hora, totalizando 4,000 DOP), conexión a internet (2,500 DOP), electricidad (1,800 DOP) y respaldos en la nube (opcional, 500 DOP). El total mensual estimado es de 8,800 DOP.
V.7. Oferta al Cliente (ONPECO)
El producto final entregado a ONPECO incluye el código fuente completo del proyecto Django "VPJ" con todas sus aplicaciones (users, marketplace, complaints, chat). Se entrega el archivo de base de datos "db.sqlite3" con la estructura de tablas y datos de prueba. La documentación técnica se proporciona en el archivo "DOCUMENTACION.md" con el registro de fases, comandos y solución de problemas.
El manual de usuario incluye guías paso a paso para consumidores, productores y reguladores ONPECO. Se incluyen scripts de respaldo (auto_backup.bat y el comando personalizado auto_backup), el archivo "requirements.txt" con todas las dependencias, y las instrucciones de despliegue para instalación, configuración y ejecución con Daphne.
V.8. Beneficios para ONPECO
La implementación del sistema ofrece múltiples beneficios para ONPECO. Permite la reducción de intermediarios al conectar directamente a productores y consumidores, eliminando sobreprecios. Garantiza transparencia de precios mediante el sistema de denuncias y seguimiento para precios abusivos. Facilita una supervisión efectiva a través del portal ONPECO con reportes gráficos y ranking de productos más consultados. Asegura el respaldo automático de datos con backups diarios sin intervención manual. Ofrece comunicación en tiempo real mediante el chat integrado entre consumidores y productores con WebSockets. Y utiliza tecnología escalable en Django, lista para adaptarse a futuras necesidades.
V.9. Forma de pago sugerida
Se sugiere una forma de pago distribuida en tres etapas. La primera etapa corresponde al inicio del proyecto, con un 30% del total (250,668 DOP), asociado a la firma de acuerdo y levantamiento de información. La segunda etapa corresponde a la entrega del prototipo funcional E04, con otro 30% (250,668 DOP). La tercera y última etapa corresponde a la entrega final del sistema E05, con el 40% restante (334,224 DOP). El monto total asciende a 835,560 DOP.
V.10. Notas y supuestos presupuestarios
	Tipo de cambio: Se utilizó 1 USD = 62 DOP como referencia para convertir tarifas internacionales a moneda local.
	Horas de desarrollo: El cálculo de 504 horas hombre es una estimación basada en la dedicación académica del equipo. En un entorno comercial, un proyecto de esta complejidad podría requerir entre 600 y 800 horas hombre, lo que elevaría el costo a aproximadamente 1,000,000 DOP.
	Tarifas de desarrolladores: Según datos de mercado, los desarrolladores junior en Latinoamérica cobran entre 10 y 25 USD por hora, mientras que los desarrolladores senior pueden cobrar entre 35 y 60 USD por hora. Para este proyecto se utilizó la tarifa más conservadora.
	Hardware existente: Se asume que el equipo desarrollador cuenta con computadoras personales. En caso de requerir equipos nuevos, el costo sería adicional.
	Conexión a internet: Los precios de internet en República Dominicana varían según el operador (Claro, Altice, Viva) y el plan contratado. Se estimó un plan de fibra óptica básico de 2,500 DOP mensuales.
	Contingencias: Se incluye un 10% adicional para imprevistos, como fallas de hardware, retrasos en desarrollo o capacitación adicional.
	Mantenimiento post-implementación: No está incluido en el presupuesto inicial, pero se recomienda considerar un costo mensual de aproximadamente 8,800 DOP para soporte continuo.

VI. LISTA DE ACTIVIDADES
A continuación, se enuncia el conjunto de actividades realizadas para el análisis, diseño, desarrollo e implementación del proyecto "Ventas Precio Justo ONPECO-UASD" (VPJ).
A. Levantamiento de información
N°	Actividad	Descripción
1	Diseñar guía de entrevista	Elaborar el cuestionario para recolectar información sobre la problemática de precios en Azua.
2	Realizar entrevista a ONPECO	Entrevistar a los responsables del proyecto (Rita González, Leonor González, Leonel Rivas, Nayelis Cabreras).
3	Identificar actores involucrados	Registrar a productores, consumidores, suplidores, ONPECO, UASD, CONASSAN y Ministerio de Agricultura.
4	Identificar necesidades del cliente	Documentar las funcionalidades deseadas: denuncias, publicación de productos, aprobación de usuarios, etc.
5	Identificar obstáculos y limitaciones	Registrar resistencia al cambio, acceso a internet, educación digital, necesidad de auspiciadores.
6	Elaborar informe de levantamiento de información (E01	Consolidar toda la información recolectada en un documento formal.
	Tabla 14 Actividades de levantamiento de información.
	
	B. Análisis del sistema actual
	
N°	Actividad	Descripción
7	Describir el sistema actual	Documentar cómo comercializan actualmente los productores (métodos informales: teléfono, acuerdos verbales).
8	Determinar departamentos involucrados	Identificar áreas de ONPECO, UASD y otras instituciones que participan.
9	Diagrama de flujo del sistema actual	Representar gráficamente el proceso actual de comercialización con intermediarios.
10	Narrativa de los procesos actuales	Describir paso a paso cómo ocurre la venta de productos agrícolas actualmente.
11	Identificar debilidades del sistema actual	Documentar problemas: intermediarios, precios desiguales, falta de transparencia, pérdidas económicas.
12	Elaborar informe del análisis del sistema actual	Consolidar hallazgos en un documento formal.
Tabla 15 Actividades de análisis del sistema actual
	C. Estudios de factibilidad
	
N°	Actividad	Descripción
13	
Realizar factibilidad técnica	Evaluar si la tecnología propuesta (Python, Django, SQLite, Daphne) es viable.
14	Realizar factibilidad económica	Estimar costos de desarrollo, hardware, software y operación (presupuesto).
15	Realizar factibilidad operacional	Evaluar si los usuarios (productores, consumidores) podrán usar el sistema.
16	
Elaborar informe de factibilidad	Consolidar los tres estudios en un documento formal.
	Tabla 16 Actividades de estudios de factibilidad.
D. Análisis del sistema propuesto
N°	Actividad	Descripción
17	Describir la plataforma propuesta	Describir la plataforma "Ventas Precio Justo ONPECO-UASD" (VPJ).
18	Definir objetivos del proyecto	Definir los objetivos generales y específicos del proyecto.
19	Redactar justificación	Redactar la justificación del proyecto basada en la problemática de intermediarios.
20	Definir metodología	Definir la metodología de desarrollo (iterativa incremental por fases).
21	Diagrama de flujo de datos	Representar gráficamente el flujo de datos del sistema propuesto.
22	Diagrama de casos de uso	Representar gráficamente los actores y sus interacciones con el sistema.
23	Elaborar informe de análisis	Consolidar el análisis del sistema propuesto en un documento formal (E03).
	Tabla 17 Actividades de análisis del sistema propuesto.

E. Diseño del sistema
N°	Actividad	Descripción
24	Diseñar arquitectura del sistema	Definir la estructura cliente-servidor con Daphne ASGI + Django.
25	Diseñar base de datos	Crear modelos User (con roles), Product, Complaint, ComplaintUpdate.
26	Diseñar diagramas de conexión.	Representar la topología de red, conexión eléctrica y ADSL.
27	Diseñar pantallas del sistema	Diseñar menú principal, catálogo, detalle de producto, perfil de usuario.
28	Diseñar portal ONPECO	Diseñar dashboard, gráficos, ranking de productos, gestión de respaldos.
29	Describir campos de formularios	Documentar todos los campos (nombre, tipo, validación, descripción).
30	Describir botones del sistema	Documentar todos los botones (función, destino, mensajes asociados).
Tabla  18 Actividades de diseño del sistema.
F.  Desarrollo del sistema (codificación)
N°	Actividad	Descripción
31	Configurar entorno de desarrollo.	Instalar Python, crear entorno virtual, instalar Django y dependencias.
32	Desarrollar módulo de usuarios	Crear app users, modelo User con roles, registro, login, logout, perfil, aprobación por ONPECO.
33	Desarrollar módulo de Marketplace	Crear app marketplace, modelo Product, vistas CRUD, catálogo, stock bajo.
34	Desarrollar módulo de denuncias	Crear app complaints, modelos Complaint y Complaint Update, tickets únicos, historial de seguimiento, gestión por ONPECO.
35	Desarrollar portal ONPECO	Crear dashboard con gráficos Chart.js, ranking de productos más consultados
36	Desarrollar sistema de respaldos	Implementar comando auto_backup, script batch, programación en Windows.
37	Desarrollar módulo de chat en tiempo real	Implementar WebSockets con Daphne y salas privadas.
38	Desarrollar templates HTML con Bootstrap	Crear plantillas base, formularios, tablas, mensajes de éxito/error.
39	Desarrollar módulo de carrito, pedidos y checkout	Implementar carrito de compras, checkout, modelos Order y OrderItem.
40	Desarrollar centro de acopio, balance de ventas y pagos	Implementar centro de acopio, desglose de pagos, balance de ventas y pagos a productores.
41	Desarrollar exportaciones, calificaciones y reputación	Implementar exportación a PDF/Excel, calificación de productores y gestión de reputación por ONPECO.
42	Desarrollar rankings y visibilidad de perfil	Implementar ranking de productores más denunciados, ranking con calificaciones y checkbox de visibilidad de perfil.
Tabla 19 Actividades de desarrollo del sistema.
G.  Pruebas y calidad
N°	Actividad	Descripción
43	Realizar pruebas unitarias	Probar cada modelo, vista y formulario individualmente.
44	Realizar pruebas de integración	Probar la interacción entre módulos (denuncias desde productos, chat entre roles).
45	Realizar pruebas de roles y permisos	Verificar que consumidores, productores, suplidores y reguladores tengan accesos correctos.
46	Realizar pruebas de WebSockets y chat en tiempo real.	Verificar conexiones en tiempo real entre consumidores y productores.
47	Realizar pruebas de respaldos	Verificar generación manual y automática de backups JSON.
48	Documentar errores y soluciones	Registrar en DOCUMENTACION.md los problemas encontrados y sus soluciones.
	Tabla 20 Actividades de pruebas y calidad.
H. Documentación y cierre
N°	Actividad	Descripción
49	Elaborar documentación y cierre del proyecto	Redactar manual de usuario, manual técnico, entregar sistema funcional a ONPECO, capacitar al personal y realizar reunión de cierre con acta de conformidad.
Tabla 21 Actividades de documentación y cierre.
VII. DESCRIPCIÓN DE ACTIVIDADES
A continuación, se describe de manera detallada el conjunto de actividades realizadas para el análisis, diseño, desarrollo e implementación del proyecto "Ventas Precio Justo ONPECO-UASD" (VPJ).
Levantamiento de información
Actividad 1: Diseñar guía de entrevista
Se elaboró un cuestionario estructurado con el objetivo de recolectar información precisa sobre la problemática de precios de productos agrícolas en la provincia de Azua. El cuestionario se organizó en seis bloques temáticos:
Bloque	Temática	Preguntas
Bloque 1	Entendiendo el problema	4 preguntas
Bloque 2	Conociendo a los usuarios	3 preguntas
Bloque 3	Funcionalidades deseadas	3 preguntas
Bloque 4	Actores involucrados	3 preguntas
Bloque 5	Expectativas y limitaciones	3 preguntas
Bloque 6	Logística para el monográfico	4 preguntas
	Tabla 22 Diseñar guía de entrevista.
	
Total: 20 preguntas abiertas, diseñadas para permitir que los entrevistados expresaran libremente su percepción sobre el problema, sin inducir respuestas hacia soluciones tecnológicas predefinidas. Este enfoque garantizó que las necesidades reales del cliente fueran capturadas antes de proponer cualquier solución técnica.
Actividad 2: Realizar entrevista a los responsables de ONPECO
La entrevista se realizó el 28 de mayo de 2026 en las oficinas de ONPECO (Oficina Nacional de Protección al Consumidor). Participaron los siguientes responsables del proyecto:
Nombre	Cargo
Rita González	Coordinadora ejecutiva
Leonor González	Coordinadora operativa
Leonel A. Rivas P.	Coordinador técnico
Nayelis Cabreras	Administración
	Tabla 23 Realizar entrevista a los responsables de ONPECO.
	
	
	Duración de la entrevista
	
	La entrevista tuvo una duración aproximada de 2 horas. Se aplicó el cuestionario diseñado previamente, tomando notas escritas de todas las respuestas. No se realizó grabación de audio por solicitud de los entrevistados.
	Principales hallazgos:
	Existe un problema estructural con intermediarios que compran productos antes de la cosecha a precios bajos y los venden a precios elevados a los consumidores. Los productores reciben ingresos reducidos, mientras que los consumidores pagan precios inflados. No existen intentos previos de solución tecnológica ni estudios formales que respalden el problema, solo percepción general. Los usuarios (productores) tienen conocimientos básicos de tecnología, como el uso de WhatsApp y Facebook.
	La aplicación debe incluir compras directas, comparación de precios, notificaciones, categorías de productos, disponibilidad de inventario y un sistema de denuncias con seguimiento. Participan instituciones como CONASSAN, UASD Recinto Azua y Ministerio de Agricultura.
Actividad 3: Identificar actores involucrados
A partir de la entrevista, se identificaron los siguientes actores clave para el proyecto:
Actor	Rol en el sistema
Productores agrícolas	Ofrecen sus cosechas directamente en la plataforma, publican precios y disponibilidad.
Consumidores	Buscan productos, comparan precios, compran y pueden realizar denuncias.
Suplidores (intermediarios regulados)	Pueden publicar productos siempre que declaren productor origen y precio de compra.
ONPECO (Regulador)	Ente regulador que aprueba productores y suplidores, gestiona denuncias y supervisa el sistema.
UASD Recinto Azua	Institución académica colaboradora que facilitó contactos con productores locales.
CONASSAN	Entidad gubernamental que aportó lineamientos sobre seguridad alimentaria.
Ministerio de Agricultura	Institución que validó la pertinencia del proyecto para el sector agrícola.
Tabla 24 Identificar actores involucrados.
Actividad 4: Identificar las necesidades del cliente
Con base en las respuestas de la entrevista (preguntas 8, 9 y 10), se identificaron las siguientes necesidades funcionales:

Necesidad	Descripción
Registro por roles	El sistema debe permitir registro diferenciado para productores, consumidores y suplidores.
Aprobación de usuarios	ONPECO debe aprobar manualmente a productores y suplidores antes de que puedan publicar productos.
Publicación de productos	Los productores y suplidores deben poder publicar productos con nombre, descripción, precio, categoría, stock y fotos.
Catálogo y búsqueda	Los consumidores deben poder ver todos los productos disponibles, filtrar por categorías y buscar productos específicos.
Denuncias	Los consumidores deben poder denunciar productos o productores por: precio abusivo, mala calidad, problemas de entrega u otros motivos
Seguimiento de denuncias	ONPECO debe poder cambiar el estado de las denuncias (pendiente, en investigación, resuelto, rechazado) y agregar comentarios de seguimiento.
Notificaciones	El sistema debe mostrar mensajes de éxito/error al usuario sobre sus acciones.
Reportes y estadísticas	ONPECO debe poder visualizar gráficos de denuncias por mes y ranking de productos más consultados.
Respaldo de datos	El sistema debe realizar respaldos automáticos de la base de datos para prevenir pérdida de información.
Comunicación directa	Consumidores y productores deben poder comunicarse mediante chat en tiempo real.
	Tabla 25 Identificar las necesidades del cliente

Actividad 5: Identificar obstáculos y limitaciones
Con base en la entrevista (pregunta 15), se identificaron los siguientes obstáculos potenciales:


Obstáculo	Descripción	Estrategia de mitigación
Resistencia al cambio	Algunos productores pueden mostrarse reacios a usar tecnología.	Capacitación presencial y diseño de interfaz sencilla.
Acceso limitado a internet	En zonas rurales de Azua, la conectividad puede ser deficiente.	Optimizar la aplicación para funcionar con conexiones lentas; reducir tamaño de imágenes.
Baja educación digital	Productores con poca experiencia en dispositivos móviles.	Diseño intuitivo, uso de iconos grandes, textos claros.
Sostenibilidad económica	La plataforma requiere mantenimiento continuo.	Buscar auspiciadores o patrocinadores; presupuestar mantenimiento.
Personal administrativo	ONPECO necesita personal dedicado a gestionar la plataforma.	Capacitar al personal existente de ONPECO.
	Tabla 26 Identificar obstáculos y limitaciones
	
Actividad 6: Elaborar informe de levantamiento de información (E01)
Se consolidó toda la información recolectada en un documento formal (E01) que incluye: ficha técnica de la entrevista (fecha, lugar, participantes), respuestas completas a las 20 preguntas, identificación de actores, listado de necesidades funcionales, obstáculos y limitaciones identificados, y expectativas del cliente para los primeros 6 meses. Este informe sirvió como insumo principal para las fases de análisis y diseño del sistema.
Entregable E01 completado.
B. Análisis del sistema actual

Actividad 7: Describir el sistema actual de comercialización
Se documentó el proceso actual de comercialización de productos agrícolas en Azua, identificando que los productores utilizan métodos informales como contactos telefónicos con intermediarios conocidos, acuerdos verbales sin contratos formales y venta directa en mercados locales cuando es posible.
Flujo actual:
 Este flujo incluye múltiples intermediarios que incrementan el precio final sin beneficiar al productor original
Actividad 8: Determinar las instituciones y departamentos involucrados
Se identificaron las siguientes instituciones en el ecosistema actual:
Institución	Rol actual
Productores individuales	Cultivan y venden su cosecha a intermediarios.
Intermediarios (no regulados)	Compran a bajo precio, almacenan y revenden a mayoristas.
Mayoristas	Compran grandes volúmenes a intermediarios.
Minoristas (colmados, mercados)	Venden al consumidor final a precio elevado.
ONPECO	No tiene participación en el proceso actual.
Ministerio de Agricultura	Ofrece asistencia técnica pero no interviene en precios.
Tabla 27 Determinar las instituciones y departamentos involucrados
Actividad 9: Diagrama de flujo del sistema actual
Se elaboró un diagrama de flujo representando el proceso actual de comercialización. El flujo inicia con el productor (agricultor), quien vende su cosecha a bajo precio a un intermediario. El intermediario compra los productos antes de la cosecha, fija un precio bajo y luego revende con margen a un mayorista. El mayorista, a su vez, revende con otro margen a un minorista. Finalmente, el minorista vende los productos al consumidor a un precio elevado. Este flujo incluye múltiples intermediarios que incrementan el precio final sin beneficiar al productor original.
Diagrama de flujo del sistema actual:
:  
 
Actividad 10: Narrativa de los procesos del sistema actual

El proceso detallado comienza cuando el productor cultiva sus productos, como aguacates, tomates o plátanos. Antes de la cosecha, los intermediarios contactan al productor y ofrecen comprar toda su producción a un precio fijo, generalmente bajo. El productor acepta por necesidad, ya que no tiene otros canales de venta. El intermediario cosecha o recoge los productos y los transporta a centros de acopio. Luego, el intermediario revende los productos a mayoristas, aplicando un margen de ganancia del 30 al 50 por ciento. Los mayoristas distribuyen a minoristas, como colmados, supermercados y mercados públicos, aplicando otro margen del 20 al 40 por ciento. Finalmente, el consumidor compra el producto en el minorista, pagando un precio que puede ser dos o tres veces superior al que recibió el productor.
Ejemplo concreto:
Producto	Precio al productor	Precio al consumidor	Margen total
Tomates	20 DOP/libra	60 DOP/libra	200%
Aguacates	15 DOP/unidad	50 DOP/unidad	233%
Plátanos	5 DOP/unidad	20 DOP/unidad	300%
	Tabla 28 Narrativa de los procesos del sistema actual
Actividad 11: Identificar debilidades del sistema actual
Debilidad	Descripción	Impacto
Falta de transparencia	Los productores no conocen el precio final de sus productos en el mercado.	Venden a precios injustos.
Múltiples intermediarios	Cada intermediario agrega un margen sin agregar valor real.	Precio final inflado.
Ausencia de canales directos	Productores y consumidores no tienen forma de contactarse directamente.	Dependencia de intermediarios.
Pérdidas económicas	Productores reciben solo el 30-40% del precio final.	Bajos ingresos, pobreza rural.
Productos no vendidos	Cuando los intermediarios no compran, los productos se pierden.	Desperdicio de alimentos.
Sin supervisión	ONPECO no tiene forma de monitorear precios abusivos.	Abusos sin consecuencias.
	Tabla 29 Identificar debilidades del sistema actual
	
Actividad 12: Elaborar informe de análisis del sistema actual (E02)
Se consolidó el análisis del sistema actual en un documento formal (E02) que incluye la descripción detallada del proceso actual de comercialización, el diagrama de flujo, la narrativa de procesos, la tabla de debilidades con sus impactos cuantificados y la comparación de precios entre lo que recibe el productor y lo que paga el consumidor.
Entregable E02 completado.
Estudios de factibilidad
Actividad 13: Realizar estudio de factibilidad técnica
Se evaluó la viabilidad técnica del proyecto considerando:
Componente	Evaluación	Conclusión
Lenguaje Python	Tecnología madura, amplia comunidad, documentación extensa.	Factible
Framework Django	Ideal para aplicaciones web con autenticación, bases de datos y paneles de administración.	Factible
Daphne + Channels	Soporte nativo para WebSockets, necesario para chat en tiempo real.	Factible
SQLite	Suficiente para el volumen de datos esperado (cientos de productos, miles de usuarios).	Factible
Bootstrap 5	Framework CSS responsive, facilita diseño accesible para dispositivos móviles.	Factible
Chart.js	Librería ligera para gráficos, se integra fácilmente con Django.	Factible
	Tabla 30 Realizar estudio de factibilidad técnica
	
Conclusión: El proyecto es técnicamente factible. Todas las tecnologías elegidas son de código abierto, gratuitas y tienen soporte activo.
Actividad 14: Realizar estudio de factibilidad económica
Se estimó el presupuesto total del proyecto en $835,560 DOP, desglosado de la siguiente manera:
Categoría	Costo (DOP)
Recursos Humanos (504 horas)	504,000
Hardware (equipos, UPS, regulador, disco externo)	204,000
Infraestructura y conectividad (1 año)	51,600
Contingencias (10%)	75,960
TOTAL $835,560             Tabla 31 Realizar estudio de factibilidad económica
Conclusión: El proyecto es económicamente factible, con una inversión inicial razonable
Actividad 15: Realizar estudio de factibilidad operacional
Se evaluó la capacidad de los usuarios para utilizar el sistema:
Factor	Evaluación	Mitigación
Nivel tecnológico de productores	Básico (usan WhatsApp, Facebook)	Interfaz sencilla, iconos grandes, textos claros
Acceso a internet	Limitado en zonas rurales	Optimización para conexiones lentas
Capacidad de ONPECO para administrar	Personal existente puede ser capacitado	Capacitación incluida en el proyecto
Resistencia al cambio	Posible en productores mayores	Capacitación presencial y soporte continuo
	Tabla 32 Realizar estudio de factibilidad operacional

Conclusión: El proyecto es operacionalmente factible, siempre que se acompañe de un plan de capacitación adecuado.
Actividad 16: Elaborar informe de estudio de factibilidad

Se consolidaron los tres estudios de factibilidad en un documento formal que incluye factibilidad técnica con las tecnologías, recursos y conocimientos del equipo; factibilidad económica con el presupuesto detallado y flujo de caja; y factibilidad operacional con la capacidad de usuarios, riesgos y mitigaciones.
Actividad 17: Describir la plataforma "Ventas Precio Justo ONPECO-UASD"
Se definió la plataforma como una aplicación web desarrollada en Python con Django, accesible desde navegadores web en computadoras y dispositivos móviles. La plataforma permite el registro de usuarios con roles diferenciados como productor, consumidor, suplidor y regulador; la publicación y consulta de productos agrícolas; la creación y seguimiento de denuncias por precios abusivos; la comunicación en tiempo real mediante chat; la generación de reportes y estadísticas para ONPECO; y el respaldo automático de la base de datos
Actividad 18: Redactar la justificación del proyecto
El proyecto se justifica por las siguientes razones: existe un problema social identificado donde los pequeños y medianos productores de Azua reciben ingresos reducidos por sus cosechas debido a la intervención de intermediarios, mientras que los consumidores pagan precios elevados. No existe actualmente una plataforma digital que conecte directamente a productores y consumidores en la provincia de Azua. Los precios inflados de los productos agrícolas impactan negativamente en la economía de las familias de Azua, encareciendo la canasta familiar. El deterioro de productos no vendidos y los bajos precios de venta generan pérdidas significativas para los productores. El proyecto cuenta con el respaldo institucional de ONPECO, UASD, CONASSAN y el Ministerio de Agricultura.

Actividad 19: Definir la metodología de desarrollo
Se utilizó una metodología iterativa incremental, organizada en fases:
Fase	Descripción	Duración estimada	Período
Fase 1	Configuración del entorno de desarrollo	1 día	28/05/2026
Fase 2	Configuración de la documentación del proyecto	1 día	29/05/2026
Fase 3	Creación de modelos de datos	2 días	30/05/2026 - 31/05/2026
Fase 4	Sistema de autenticación y roles	2 días	01/06/2026 - 02/06/2026
Fase 5	Creación de templates HTML (interfaces)	3 días	03/06/2026 - 05/06/2026
Fase 6	Sistema de aprobación de productores/suplidores	2 días	06/06/2026 - 07/06/2026
Fase 7	Módulo de marketplace (productos)	3 días	08/06/2026 - 10/06/2026
Fase 8	Sistema de denuncias y seguimiento	3 días	11/06/2026 - 13/06/2026
Fase 9	Sistema de respaldos automáticos	2 días	14/06/2026 - 15/06/2026
Fase 10	Chat en tiempo real con WebSockets	2 días	16/06/2026 - 17/06/2026
Fase 11	Reportes, gráficos y dashboard ONPECO	2 días	18/06/2026 - 19/06/2026
Fase 12	Pruebas, documentación y cierre	5 días	20/06/2026 - 26/06/2026
Fase 13	Ajustes finales y entrega	2 días	27/06/2026 - 30/06/2026
Tabla 33. Metodología de desarrollo por fases.
Cada fase generaba entregables parciales que eran revisados antes de continuar con la siguiente.
Actividad 20: Diagrama de flujo de datos del sistema propuesto
Se elaboró el siguiente diagrama de flujo de datos para el sistema propuesto:   
  

Actividad 21: Diagrama de casos de uso del sistema propuesto
Se elaboró el diagrama de casos de uso identificando los siguientes actores y sus interacciones:
Actores:
	Consumidor (no autenticado / autenticado)
	Productor (aprobado por ONPECO)
	Suplidor (aprobado por ONPECO)
	Regulador ONPECO
	Administrador del sistema
Casos de uso por acto:
Actor	Casos de uso
Consumidor	Registrarse, Iniciar sesión, Ver catálogo de productos, Ver detalle de producto, Buscar productos, Filtrar por categorías, Crear denuncia, Ver seguimiento de denuncias, Contactar a productor por chat, Editar perfil
Productor	Registrarse (solicita aprobación), Iniciar sesión, Publicar producto, Editar producto, Eliminar producto, Ver mis productos, Ver alertas de stock bajo, Responder chat, Editar perfil
Suplidor	Registrarse (solicita aprobación), Iniciar sesión, Publicar producto (declarando productor origen), Editar producto, Eliminar producto, Ver mis productos, Editar perfil
Regulador ONPECO	Iniciar sesión, Ver dashboard, Aprobar productores, Aprobar suplidores, Ver todas las denuncias, Cambiar estado de denuncia, Agregar comentario de seguimiento, Ver gráfico de denuncias por mes, Ver ranking de productos más consultados, Gestionar backups, Restaurar sistema
Administrador	Acceso total al panel de Django admin, Gestionar usuarios, Gestionar productos, Gestionar denuncias, Ver logs del sistema
Tabla 34 Casos de uso por actor
	Actividad 22: Elaborar informe de análisis del sistema propuesto (E03)
	Se consolidó el análisis del sistema propuesto en un documento formal (E03) que incluye descripción general del sistema, objetivos generales y específicos, justificación completa, metodología de desarrollo organizada en fases, diagrama de flujo de datos, diagrama de casos de uso, diccionario de datos lógico y físico, y diseño del sistema.
Actividad 23: Diseñar la arquitectura del sistema
Se definió una arquitectura cliente-servidor con los siguientes componentes:
Capa	Tecnología	Función
Cliente (Frontend)	HTML5, CSS3, Bootstrap 5, JavaScript	Interfaz de usuario responsive, consume APIs REST, WebSockets para chat
Servidor Web (ASGI)	Daphne 4.0.0	Maneja peticiones HTTP y conexiones WebSocket en tiempo real
Backend (Aplicación)	Django 5.x	Procesa solicitudes, aplica lógica de negocio, interactúa con BD
WebSockets	Django Channels 4.0.0	Gestiona conexiones persistentes para chat en tiempo real
Base de Datos	SQLite3	Almacenamiento persistente de datos (usuarios, productos, denuncias)
Respaldo	JSON + script batch	Backup automático de la base de datos
Tabla 35 Diseñar la arquitectura del sistema

Actividad 24: Diseñar la base de datos (modelos)
Se diseñaron los siguientes modelos (tablas) principales para la base de datos:
Modelo User (apps. users. models): Incluye campos como username, email, password, role (consumidor, productor, suplidor, regulador), phone, address, business_name, is_approved y is_staff. Este modelo extiende el usuario de Django para agregar roles y campos personalizados.

Modelo Product (apps.marketplace.models): Incluye campos como vendedor (Foreign key a User), productor_origen (para suplidores), name, description, category, price, unit, stock, stock_minimo, available, view_count, image, created_at y updated_at.
Modelo Complaint (apps.complaints.models): Incluye campos como ticket_number (formato CD-XXXXXX), consumidor, productor, producto, title, description, complaint_type (price, quality, delivery, other), priority (high, medium, low), status (pending, investigating, resolved, rejected), created_at y updated_at.
Modelo ComplaintUpdate (apps.complaints.models): Incluye campos como complaint (Foreign key a Complaint), comment, old_status, new_status, created_by y created_at.

Actividad 25: Diseñar diagramas de conexión (red, eléctrica, ADSL)
Se elaboraron los siguientes diagramas (incluidos en el punto IV.3 de este documento):
Diagrama de conexión de red (arquitectura cliente-servidor)
Diagrama de conexión eléctrica (UPS, regulador, equipo)
Diagrama de conexión ADSL/Internet (módem, router, acceso a la plataforma)

Actividad 26: Diseñar las pantallas del sistema
Se diseñaron las siguientes pantallas principales:
Pantalla	Descripción	Elementos clave
Página de inicio	Landing page con presentación del proyecto	Tarjetas para consumidores y productores, botones de registro/login
Registro de consumidor	Formulario para registrarse como consumidor	Campos: username, email, password, confirmación
Registro de productor	Formulario para registrarse como productor	Campos adicionales: business_name, phone, address
Inicio de sesión	Formulario de autenticación	Campos: username, password
Perfil de usuario	Visualización y edición de datos personales	Campos editables según rol
Catálogo de productos	Listado de productos disponibles (tarjetas)	Imagen, nombre, precio, categoría, botón "Ver detalle"
Detalle de producto	Información completa del producto	Nombre, precio, stock, descripción, vendedor, botón "Denunciar"
Mis productos (productor)	Listado de productos del productor	Tabla con nombre, precio, stock, botones editar/eliminar, alertas stock bajo
Crear/Editar producto	Formulario de producto	Campos: nombre, descripción, categoría, precio, unidad, stock, stock_mínimo, imagen
Crear denuncia	Formulario de denuncia	Campos: título, tipo, prioridad, descripción
Mis denuncias (consumidor)	Listado de denuncias del consumidor	Tabla con tickets, título, estado, fecha
Detalle de denuncia	Seguimiento completo	Tickets, estado actual, historial de actualizaciones
Portal ONPECO	Dashboard de regulador	Tarjetas KPI, botones de acceso rápido
Gráfico de denuncias	Visualización estadística	Gráfico de barras (Chart.js) con denuncias por mes
Ranking de productos	Productos más consultados	Tabla ordenada por view_count
Gestión de respaldos	Listado de backups	Tabla con archivos JSON, botones restaurar/eliminar
	Tabla 36 Diseñar las pantallas del sistema

Actividad 27: Describir los campos de los formularios
A continuación, se describe la especificación de los campos principales de los formularios del sistema:
Formulario de registro de productor:
Campo	Tipo	Requerido	Validación	Descripción
username	Text	Sí	Mínimo 4 caracteres, único	Nombre de usuario
email	Email	Sí	Formato email válido, único	Correo electrónico
password	Password	Sí	Mínimo 8 caracteres	Contraseña
confirm_password	Password	si	Debe coincidir con password	Confirmación de contraseña
business_name	Text	si	Máximo 100 caracteres	Nombre del negocio/productor
phone	Text	Si
	Formato teléfono dominicano (xxx)  xxx-xxxx	Nombre del negocio/productor
address	Text	Si
	Máximo 200 caracteres	Dirección física
	Tabla 37 Describir los campos de los formularios

Formulario de creación de producto:
Campo	Tipo	Requerido	Validación	Descripción
name	Text	si	Máximo 100 caracteres	Nombre del producto
description	Textarea	si	Máximo 500 caracteres	Descripción detallada
category	Select	si	Opciones predefinidas	Frutas, verduras, granos, tubérculos, otros
price	Decimal	si	Valor positivo (mínimo 1 DOP)	Precio en pesos dominicanos
unit	Select	si	kg, lb, unidad, docena	Unidad de medida
stock	Number	si	Entero positivo	Cantidad disponible
stock_minimo	Number	si	Entero positivo (default 5)	Stock mínimo para alerta
image	File	si	JPG, PNG (máximo 5MB)	Foto del producto
	Tabla 38 Formulario de creación de producto
Formulario de creación de denuncia:
Campo	Tipo
	Requerido	Validación	Descripción
title	Text	si	Máximo 100 caracteres	Título de la denuncia
complaint_type	Select	si	price, quality, delivery, other	Tipo de denuncia
priority	Select	si	high, medium, low	Prioridad
description	Textarea	si	Máximo 500 caracteres	Descripción detallada del problema
product_id	Hidden	NO	-	Producto asociado (si aplica
Tabla 39 Formulario de creación de denuncia
Actividad 28: Describir los botones del sistema
A continuación, se describe la función de los botones principales del sistema:
Pantalla	Botón	Función que realiza
Navbar (global)	Iniciar Sesión	Redirige al formulario de login
Navbar (global)	Registrarse	Redirige a la página de selección de rol (consumidor/productor/suplidor)
Navbar (global)	Productos	Redirige al catálogo de productos
Navbar (global)	Mis Productos	(Solo productores) Redirige al listado de productos del productor
Navbar (global)	Mis Denuncias	(Solo consumidores) Redirige al listado de denuncias del consumidor
Navbar (global)	Aprobar Productores	(Solo ONPECO) Redirige a la lista de productores pendientes
Navbar (global)	Portal ONPECO	(Solo ONPECO) Redirige al dashboard con gráficos
Navbar (global)	Perfil	Redirige a la página de edición de perfil
Navbar (global)	Cerrar Sesión	Cierra la sesión actual y redirige al inicio
Catálogo de productos	Ver Detalle	Redirige a la página de detalle del producto seleccionado
Detalle de producto	Denunciar este producto	Redirige al formulario de denuncia con el producto pre-seleccionado
Mis productos (productor)	Crear Producto	Redirige al formulario de creación de producto
Mis productos (productor)	Editar	Redirige al formulario de edición del producto seleccionado
Mis productos (productor)	Eliminar	Elimina el producto (soft delete: available=False) y muestra mensaje de éxito
Portal ONPECO	Ver Gráfico de Denuncias	Redirige a la página con gráfico de denuncias por mes
Portal ONPECO	Ver Productos Top	Redirige al ranking de productos más consultados
Portal ONPECO	Gestionar Backups	Redirige a la lista de respaldos disponibles
Gestión de respaldos	Crear punto de restauración	Genera un archivo JSON con el estado actual de la base de datos
Gestión de respaldos	Restaurar	(Sobre un backup) Restaura la base de datos desde el archivo seleccionado
Aprobar productores	Aprobar	Cambia is_approved de False a True para el productor seleccionado
Aprobar productores	Rechazar	Cambia is_approved = False y opcionalmente elimina la cuenta pendiente
Gestionar denuncias (ONPECO)	Ver Detalle	Redirige al detalle completo de la denuncia
Detalle de denuncia (ONPECO)	Cambiar Estado	Actualiza el estado (pendiente, investigación, resuelto, rechazado) y guarda el comentario
Chat	Contactar al productor	Inicia una sala de chat privada con el productor seleccionado
Chat	Enviar mensaje	Envía un mensaje a través del WebSocket a la sala de chat
	Tabla 40 Describir los botones del sistema
	
	
	
	
	Actividad 29: Desarrollo del sistema (codificación)
	El desarrollo del sistema se realizó en varias etapas. Se configuró el entorno de desarrollo con Python, Django y Daphne. Se desarrolló el módulo de usuarios con registro, login, perfiles y roles, incluyendo la aprobación de productores y suplidores por ONPECO.
	Se implementó el módulo de marketplace para la publicación, edición y eliminación de productos, con alertas de stock bajo y contador de visitas.
	Se desarrolló el módulo de denuncias con tickets únicos, historial de seguimiento y gestión por ONPECO. Se creó el portal ONPECO con dashboard, gráficos Chart.js y ranking de productos más consultados. Se implementó el sistema de respaldos automáticos con comandos personalizados y programación en Windows.
	Se desarrolló el módulo de chat en tiempo real con WebSockets y Daphne. Se implementó el carrito de compras, pedidos y checkout con selección de tipo de entrega. Se desarrolló el centro de acopio con desglose de pagos y balance de ventas para productores. Se agregaron exportaciones a PDF y Excel, calificaciones de productores, gestión de reputación por ONPECO, rankings de productores y checkbox de visibilidad de perfil.
	
	Actividad 30: Realizar pruebas unitarias
	Se realizaron pruebas unitarias en los siguientes componentes del sistema. Se probó el modelo User verificando la creación de usuarios, la asignación de roles y la validación de is_approved. Se probó el modelo Product verificando la creación, edición, eliminación y el correcto funcionamiento de la propiedad stock_bajo. Se probó el modelo Complaint verificando la generación automática de tickets único y los cambios de estado. También se probaron los formularios, validando que los campos requeridos funcionen correctamente y que los formatos de email y teléfono sean válidos.
	
	Actividad 31: Realizar pruebas de integración
	Se realizaron pruebas de integración entre los distintos módulos del sistema. Se verificó que el botón "Denunciar" en el detalle de producto redirija correctamente al formulario de denuncia con el producto pre-seleccionado. Se probó el flujo completo de aprobación de productores: registro, estado pendiente, aprobación por ONPECO y posterior habilitación para crear productos.
	Se verificó la creación de salas de chat privadas y el envío de mensajes en tiempo real. También se probó el sistema de respaldos, verificando la generación de archivos JSON y la restauración desde un backup.
	
	Actividad 32: Realizar pruebas de roles y permisos
	Se verificó que cada rol tenga acceso únicamente a las funcionalidades correspondientes. El consumidor puede ver el catálogo, crear denuncias, ver sus denuncias y usar el chat, pero no puede crear productos ni aprobar usuarios. El productor puede crear, editar y eliminar productos, usar el chat y ver su perfil, pero no puede aprobar usuarios ni ver todas las denuncias. El suplidor tiene permisos similares al productor, con la restricción de declarar productor origen. El regulador ONPECO puede aprobar usuarios, gestionar denuncias, ver gráficos y gestionar backups, pero no puede crear productos.
	
	Actividad 33: Realizar pruebas de WebSockets y chat en tiempo real
	Se probó el chat en tiempo real con dos usuarios simultáneos. Se verificó que la conexión WebSocket se establezca correctamente al abrir una sala de chat entre consumidor y productor. Se probó el envío de mensajes, confirmando que el productor recibe instantáneamente el mensaje enviado por el consumidor. Se verificó que múltiples salas de chat funcionen de forma independiente sin mezclar mensajes. También se probó la reconexión automática al cerrar y volver a abrir el navegador, confirmando que el historial de mensajes se mantenga visible.
	
	Actividad 34: Realizar pruebas de respaldos automáticos y restauración
	Se probó el sistema de respaldos en sus diferentes modalidades. Se verificó que el comando python manage.py auto_backup genere correctamente un archivo JSON en la carpeta backups. Se confirmó que la limpieza automática mantenga solo los últimos 10 backups, eliminando los más antiguos. Se probó la restauración desde un backup existente con el comando python manage.py restaurar_backup --backup-file backup_auto_xxx.json, verificando que los datos se restauren correctamente. También se confirmó que la tarea programada en Windows se ejecute a las 2:00 AM según lo configurado.
	
	Actividad 35: Documentar errores encontrados y soluciones aplicadas
	Se documentaron los principales errores encontrados durante el desarrollo y sus soluciones. El error NoReverseMatch perfil se solucionó cambiando url perfil por url users perfil.
	El error AttributeError restaurar backup se resolvió agregando la función correspondiente en complaints views. El error ModuleNotFoundError No module named users se corrigió agregando el prefijo apps en INSTALLED_APPS. El error Cannot use ImageField because Pillow is not installed se solucionó instalando Pillow con pip install Pillow. El error de usuario ONPECO regulador apareciendo como Consumidor se corrigió cambiando user role a regulador mediante el Shell de Django.
	
	Actividad 36: Redactar manual de usuario
	Se redactó un manual de usuario con instrucciones para cada tipo de rol. Para consumidores, se incluyeron pasos para registrarse, iniciar sesión, ver el catálogo de productos, ver el detalle de un producto, crear una denuncia, ver el seguimiento de denuncias, contactar a un productor por chat y editar el perfil. Para productores, se incluyeron pasos para registrarse, saber si ya fueron aprobados, crear, editar y eliminar productos, ver alertas de stock bajo, responder mensajes de chat y editar el perfil. Para reguladores ONPECO, se incluyeron pasos para acceder al portal, aprobar productores y suplidores, gestionar denuncias, ver el gráfico de denuncias por mes, ver el ranking de productos más consultados y gestionar backups.
	
	Actividad 37: Redactar manual técnico
	Se redactó un manual técnico con las siguientes secciones: requisitos del sistema incluyendo hardware, software y dependencias; instalación con clonar repositorio, crear entorno virtual e instalar dependencias; configuración de settings, asgi y variables de entorno; ejecución del servidor con Daphne; mantenimiento con backups automáticos, logs y solución de problemas comunes; estructura del proyecto con descripción de carpetas y archivos clave; base de datos con modelos, relaciones y comandos de migración; y despliegue con recomendaciones para producción.
	
	
	
	Actividad 38: Entregar sistema funcional a ONPECO
	La entrega final incluyó los siguientes elementos: código fuente completo en carpeta ZIP, base de datos con datos de prueba, archivo requirements.txt con todas las dependencias, documentación en PDF y Word con manual de usuario y manual técnico, scripts de respaldo con auto_backup.bat y comando auto_backup, instrucciones de instalación en README.md y los anexos con guía de entrevista, diccionario de datos y manual de usuario.
	
	Actividad 39: Capacitar al personal de ONPECO
	Se realizó una capacitación presencial de 2 horas dirigida al personal de ONPECO. Los temas cubiertos incluyeron introducción al sistema con presentación, objetivos y alcance; gestión de usuarios para aprobar productores y suplidores y editar perfiles; gestión de denuncias para ver denuncias, cambiar estado y agregar comentarios; reportes y gráficos para interpretar el gráfico de denuncias por mes y usar el ranking de productos; y backups y mantenimiento para crear puntos de restauración, restaurar backups y ejecutar backups automáticos. Se entregó el manual de usuario en formato impreso y digital.
	
	Actividad 40: Realizar reunión de cierre y obtener acta de conformidad
	Se realizó una reunión de cierre con los representantes de ONPECO y el equipo de desarrollo. Se presentó un resumen de los entregables completados, se realizó una demostración del sistema funcionando, se revisaron los manuales de usuario y técnico, y se acordó un período de soporte post-entrega de 1 mes. El cliente ONPECO firmó el acta de conformidad, aceptando el sistema como entregado según los alcances definidos.
	
	
Creación de templates HTML (interfaces)
VIII. MATRIZ DE SECUENCIA
A continuación, se presenta la matriz de secuencia de actividades del proyecto "Ventas Precio Justo ONPECO-UASD" (VPJ), indicando el orden lógico de ejecución y las dependencias entre fases.


Fase	Descripción	Actividades incluidas	
1	Configuración del entorno de desarrollo	31	-
2	Configuración de la documentación del proyecto	-	-
3	Creación de modelos de datos	25	Fase 1
4	Sistema de autenticación y roles	32	Fase 1, Fase 3
5	Creación de templates HTML (interfaces)	38	Fase 4
6	Sistema de aprobación de productores/suplidores	32	Fase 4
7	Módulo de marketplace (productos)	33	Fase 3, Fase 4
8	Sistema de denuncias y seguimiento	34	Fase 3, Fase 4
9	Sistema de respaldos automáticos	36	Fase 3
10	Chat en tiempo real con WebSockets	37	Fase 1
11	Reportes, gráficos y dashboard ONPECO	35	Fase 4, Fase 7, Fase 8
12	Módulo de carrito, pedidos y checkout	39	Fase 4, Fase 7
13	Centro de acopio y balance de ventas	40	Fase 12
14	Exportaciones, calificaciones y reputación	41	Fase 4, Fase 7
15	Rankings y visibilidad de perfil	42	Fase 4, Fase 7
16	Pruebas unitarias	43	Fase 1 a 15
17	Pruebas de integración	44	Fase 1 a 15
18	Pruebas de roles y permisos	45	Fase 16
19	Pruebas de WebSockets y chat	46	Fase 10, Fase 16
20	Pruebas de respaldos	47	Fase 9, Fase 16
21	Documentación de errores y soluciones	48	Fase 16 a 20
22	Redacción de manuales, entrega y cierre	49	Fase 21
Tabla 41 Matriz de secuencia de actividades.
IX. MATRIZ DE TIEMPO
Para el cálculo de los tiempos estimados de cada actividad se utilizó la fórmula PERT (Program Evaluation and Review Technique): T = (O + 4M + P) / 6, donde O es el tiempo óptimo, M el tiempo medio y P el tiempo pésimo. Esta metodología permite obtener una estimación ponderada que minimiza el riesgo de sobreestimación o subestimación.
La jornada laboral establecida fue de 8 horas diarias, de lunes a viernes (9:00 AM a 5:00 PM), con una duración total de 28 días hábiles para el desarrollo del proyecto.
Etapa
	Actividades	Tiempo estándar total (horas)	Días hábiles (8h/día)
Levantamiento de información	1 - 6	16.51	2.06
Análisis del sistema actual	7 - 12	17.51	2.19
Estudios de factibilidad	13 - 16	13.51	1.69
Análisis del sistema propuesto	17 - 23	21.85	2.73
Diseño del sistema	24 - 30	26.01	3.25
Desarrollo del sistema (codificación)	31 - 38	61.00	7.63
Pruebas y calidad	39 – 44	27.01	3.38
Documentación y cierre	45 - 49	20.17	
TOTAL	1 – 49	203.57 horas	25.45 días
Tabla 42 Resumen de tiempos por etapa.

Como se puede observar en la tabla, el tiempo total estimado para el desarrollo del proyecto es de 203.57 horas distribuidas en 49 actividades, equivalentes a 25.45 días hábiles considerando una jornada de 8 horas diarias. La etapa de desarrollo (codificación) es la que mayor tiempo demanda con 61 horas (7.63 días), seguida por las pruebas con 27.01 horas (3.38 días). Este tiempo está dentro del período disponible de 28 días hábiles (del 28 de mayo al 6 de julio de 2026), lo que permite una ejecución holgada y sin presión.

X. MATRIZ DE INFORMACIÓN
A continuación, se presenta la matriz de información del proyecto, que integra la secuencia de ejecución y el tiempo estimado para cada fase.
Fase
	Descripción	Actividades incluidas	Dependencias	Tiempo (horas)
1	Configuración del entorno de desarrollo	31	-	3.17
2	Configuración de la documentación del proyecto	-	-	-
3	Creación de modelos de datos	25	Fase 1	4.17
4	Sistema de autenticación y roles	32	Fase 1, Fase 3	8.33
5	Creación de templates HTML (interfaces)	38	Fase 4	10.33
6	Sistema de aprobación de productores/suplidores	32	Fase 4	8.33
7	Módulo de marketplace (productos)	33	Fase 3, Fase 4	10.50
8	Sistema de denuncias y seguimiento	34	Fase 3, Fase 4	8.33
9	Sistema de respaldos automáticos	36	Fase 3	6.00
10	Chat en tiempo real con WebSockets	37	Fase 1	7.17
11	Reportes, gráficos y dashboard ONPECO	35	Fase 4, Fase 7, Fase 8	7.17
12	Módulo de carrito, pedidos y checkout	39	Fase 4, Fase 7	8.33
13	Centro de acopio y balance de ventas	40	Fase 12	6.00
14	Exportaciones, calificaciones y reputación	41	Fase 4, Fase 7	4.17
15	Rankings y visibilidad de perfil	42	Fase 4, Fase 7	3.17
16	
Pruebas unitarias
	43	Fase 1 a 15	6.00
17	Pruebas de integración	44	Fase 16	5.33
18	Pruebas de roles y permisos	45	Fase 16	4.17
19	Pruebas de WebSockets y chat	46	Fase 10, Fase 16	4.17
20	Pruebas de respaldos	47	Fase 9, Fase 16	3.17
21	Documentación de errores y soluciones	48	Fase 16 a 20	4.17
22	Redacción de manuales, entrega y cierre	49	Fase 21	20.17
Tabla 43 Matriz de información del proyecto.


XI. Matriz de Costos (determinar el costo de cada actividad en función del tiempo)
A continuación, se presenta la matriz de costos del proyecto "Ventas Precio Justo ONPECO-UASD" (VPJ), que determina el costo de cada actividad en función del tiempo estándar estimado.
No	Descripción	Costo (DOP)	Tiempo (h)
1	Diseñar guía de entrevista	3,170	3.17
2	Realizar entrevista a responsables de ONPECO	2,000	2.00
3	Identificar actores involucrados	2,170	2.17
4	Identificar necesidades del cliente	3,170	3.17
5	Identificar obstáculos y limitaciones	2,000	2.00
6	Elaborar informe de levantamiento (E01)	4,000	4.00
7	Describir el sistema actual de comercialización	3,170	3.17
8	Determinar instituciones involucradas	2,000	2.00
9	Diagrama de flujo del sistema actual	3,000	3.00
10	Narrativa de los procesos del sistema actual	3,170	3.17
11	Identificar debilidades del sistema actual	3,000	3.00
12	Elaborar informe de análisis actual (E02)	3,170	3.17
13	Realizar estudio de factibilidad técnica	3,170	3.17
14	Realizar estudio de factibilidad económica	4,170	4.17
15	Realizar estudio de factibilidad operacional	3,170	3.17
16	Elaborar informe de factibilidad	3,000	3.00
17	Describir la plataforma propuesta	3,170	3.17
18	Definir objetivos generales y específicos	2,000	2.00
19	Redactar justificación del proyecto	3,000	3.00
20	Definir metodología de desarrollo	2,000	2.00
21	Diagrama de flujo de datos del sistema propuesto	4,170	4.17
22	Diagrama de casos de uso del sistema propuesto	4,170	4.17
23	Elaborar informe de análisis propuesto (E03)	3,170	3.17
24	Diseñar arquitectura del sistema	3,170	3.17
25	Diseñar base de datos (modelos)	4,170	4.17
26	Diseñar diagramas de conexión (red, eléctrica, ADSL)	3,000	3.00
27	Diseñar pantallas del sistema (catálogo, perfil, etc.)	5,330	5.33
28	Diseñar pantallas del portal ONPECO	4,170	4.17
29	Describir campos de formularios	3,170	3.17
30	Describir botones del sistema	3,000	3.00
31	Configurar entorno de desarrollo	3,170	3.17
32	Desarrollar módulo de usuarios	8,330	8.33
33	Desarrollar módulo de marketplace	10,500	10.50
34	Desarrollar módulo de denuncias	8,330	8.33
35	Desarrollar portal ONPECO (gráficos y reportes)	7,170	7.17
36	Desarrollar sistema de respaldos (backups)	6,000	6.00
37	Desarrollar módulo de chat en tiempo real	7,170	7.17
38	Desarrollar templates HTML con Bootstrap	10,330	10.33
39	Realizar pruebas unitarias	6,000	6.00
40	Realizar pruebas de integración	5,330	5.33
41	Realizar pruebas de roles y permisos	4,170	4.17
42	Realizar pruebas de WebSockets y chat	4,170	4.17
43	Realizar pruebas de respaldos y restauración	3,170	3.17
44	Documentar errores y soluciones	4,170	4.17
45	Redactar manual de usuario	7,170	7.17
46	Redactar manual técnico	6,000	6.00
47	Entregar sistema funcional a ONPECO	2,000	2.00
48	Capacitar al personal de ONPECO	3,000	3.00
49	Realizar reunión de cierre y obtener acta	2,000	2.00
	SUBTOTAL	203,570	203.57
	Contingencias (10%)	20,357	-
	TOTAL	223,927	203.57
Tabla 44  Matriz de costo
XII. MATRIZ DE RIESGO
A continuación, se presenta la matriz de riesgo del proyecto "Ventas Precio Justo ONPECO-UASD" (VPJ), que determina la probabilidad de incidencias durante el desarrollo del proyecto y sus posibles soluciones.
Metodología de evaluación
Nivel	Probabilidad (%)	Impacto	Descripción
Bajo	Bajo	Leve	No afecta el cronograma ni el presupuesto
Medio	31% - 60%	Moderado	Puede retrasar actividades menores o aumentar costos ligeramente
Alto	61% - 100%	Severo	Puede retrasar el proyecto significativamente o aumentar costos considerablemente
	Tabla 45 Metodología de evaluación
Matriz de Riesgo
Riesgo	Probabilidad (%)	Impacto	Respuesta al riesgo
Resistencia al cambio por parte de los productores	70%	Alto	Realizar capacitaciones presenciales antes del lanzamiento. Diseñar una interfaz sencilla e intuitiva. Designar "embajadores" entre los productores más jóvenes para motivar a los demás. Ofrecer soporte telefónico durante el primer mes.
Falta de acceso a internet en zonas rurales de Azua	65%	Alto	Optimizar la aplicación para funcionar con conexiones de baja velocidad (2 Mbps). Permitir uso offline limitado (visualización de catálogo sin conexión). Reducir el tamaño de las imágenes de productos. Considerar alianzas con proveedores de internet comunitario.
Baja educación digital de los productores	60%		Diseñar tutoriales en video cortos (menos de 2 minutos). Incluir tooltips y ayudas contextuales en cada pantalla. Realizar pruebas de usabilidad con productores reales durante el desarrollo. Crear un manual de usuario con imágenes paso a paso.
Retrasos en la aprobación de usuarios por parte de ONPECO	50%	Medio	Automatizar notificaciones por correo (trabajo futuro). Establecer un SLA (acuerdo de nivel de servicio) con ONPECO para aprobar usuarios en menos de 48 horas. Crear un dashboard de pendientes con alertas visuales.
Errores técnicos en el servidor Daphne (WebSockets)	45%	Medio	Implementar reconexión automática de WebSockets en el cliente. Configurar logs detallados para identificar fallos. Tener un script de reinicio automático del servidor en caso de caída. Realizar pruebas de estrés antes del lanzamiento.
Fuga de datos o vulneración de información personal	40%	Severo	Implementar HTTPS en producción (trabajo futuro). Encriptar contraseñas con PBKDF2 (por defecto en Django). Limitar intentos de login para prevenir ataques de fuerza bruta. Realizar auditorías de seguridad periódicas. Cumplir con la Ley de Protección de Datos Personales de República Dominicana.
Falta de mantenimiento después de la entrega	55%	Medio	Incluir en el contrato un período de soporte post-entrega (1 mes). Capacitar al personal de ONPECO para realizar mantenimiento básico. Documentar procedimientos de solución de problemas comunes. Presupuestar mantenimiento continuo (8,800 DOP/mes según punto V).
Pérdida de datos por fallo del disco duro	35%	Severo	Implementar backups automáticos diarios (ya desarrollado). Configurar backups en disco externo o en la nube. Realizar pruebas de restauración periódicas. Mantener los últimos 10 backups automáticamente (ya implementado).
Inundación o daño físico al servidor	15%	Severo	Recomendar a ONPECO ubicar el servidor en un lugar seguro. Mantener backups en ubicación física separada (disco externo). Considerar respaldos en la nube (AWS S3, Google Drive) como trabajo futuro.
Bajo volumen de adopción por parte de consumidores	50%	Medio	Realizar campaña de promoción en redes sociales y medios locales de Azua. Ofrecer incentivos a los primeros consumidores registrados. Solicitar apoyo del Ministerio de Agricultura para difundir la plataforma.
Conflictos entre productores y suplidores por precios	60%	Medio	ONPECO debe mediar en los conflictos. El sistema permite denuncias y seguimiento. Registrar el productor origen en los productos de suplidores para trazabilidad. Publicar rangos de precios de referencia.
Obsolescencia tecnológica (Python/Django)	25%	Bajo	Utilizar versiones estables y de largo plazo (LTS). Documentar el proceso de actualización. Mantener el código modular para facilitar migraciones futuras.
Rotación del equipo de desarrollo	20%	Medio	Documentar todo el código con comentarios claros. Mantener un repositorio centralizado (Git). Realizar reuniones diarias de sincronización. Distribuir el conocimiento entre los 3 desarrolladores.
Cambio en los requisitos del cliente durante el desarrollo	40%	Medio	Utilizar metodología iterativa para incorporar cambios controlados. Documentar y priorizar nuevos requisitos. Evaluar impacto en cronograma y presupuesto antes de aceptar cambios. Mantener acta de acuerdos con ONPECO.
Dificultades técnicas con la implementación de WebSockets	35%	Medio	Utilizar Daphne y Channels que tienen buena documentación. Realizar pruebas unitarias específicas para WebSockets. Tener un plan B (chat basado en polling si falla WebSockets).
	Tabla 46 Matriz de Riesgo
Resumen de riesgos por categoría
Categoría	Riesgos	Riesgo más crítico
Usuarios y adopción	4	Resistencia al cambio (70%)
Infraestructura y conectividad	3	Falta de acceso a internet (65%)
Seguridad y datos	3	Fuga de datos (40%)
Técnicos y desarrollo	4	Errores en servidor Daphne (45%)
Organizacionales y gestión	5	Falta de mantenimiento post-entrega (55%)
	Tabla 47 Resumen de riesgos por categoría

Plan de respuesta a los 5 riesgos más críticos
#	Riesgo	Probabilidad	Respuesta planificada	Responsable
1	Resistencia al cambio por parte de los productores	70%	Capacitaciones presenciales, interfaz sencilla, embajadores locales	Equipo de desarrollo + ONPECO
2	Falta de acceso a internet en zonas rurales de Azua	65%	Optimización para conexiones lentas, imágenes comprimidas, alianzas con ISP comunitarios	Equipo de desarrollo
3	Baja educación digital de los productores	60%	Tutoriales en video, tooltips, pruebas de usabilidad, manual ilustrado	Equipo de desarrollo
4	Conflictos entre productores y suplidores por precios	60%	Mediación de ONPECO, trazabilidad del productor origen, rangos de precios de referencia	ONPECO
5	Falta de mantenimiento después de la entrega	55%	Período de soporte de 1 mes, capacitación al personal, documentación de solución de problemas	Equipo de desarrollo + ONPECO
	Tabla 48 Plan de respuesta a los 5 riesgos más críticos
Acciones preventivas y correctivas por tipo de riesgo
Tipo de riesgo	Acciones preventivas	Acciones correctivas
Técnicos	Pruebas unitarias y de integración continuas. Documentación del código. Entorno de pruebas separado.	Revertir a backup funcional. Depuración con logs. Consultar documentación oficial de Django/Daphne.
Organizacionales	Reuniones semanales con ONPECO. Actas de acuerdos. Plan de capacitación definido.	Reunión extraordinaria para resolver conflictos. Ajuste de cronograma.
Usuarios	Pruebas de usabilidad con usuarios reales. Interfaz intuitiva. Manuales ilustrados.	Capacitación adicional. Soporte telefónico. Videos tutoriales.
Infraestructura	Backups automáticos diarios. UPS y regulador de voltaje. Antivirus actualizado.	Restauración desde backup. Reemplazo de hardware dañado. Conexión alternativa (4G).
Seguridad	HTTPS (producción). Encriptación de contraseñas. Limitación de intentos de login.	Cambio de contraseñas comprometidas. Notificación a usuarios afectados. Auditoría de seguridad.
	Tabla 49 Acciones preventivas y correctivas por tipo de riesgo
XIII. DESCRIPCIÓN DE LAS LIMITACIONES DE RECURSOS
A continuación, se presentan las limitaciones identificadas durante el desarrollo del proyecto "Ventas Precio Justo ONPECO-UASD" (VPJ), las cuales pueden incidir en la correcta ejecución del mismo. Estas limitaciones se clasifican en recursos humanos, económicos, materiales, tecnológicos y de tiempo.
	Limitaciones de Recursos Humanos
Las principales limitaciones de recursos humanos identificadas son: un equipo reducido de 3 desarrolladores, lo que reduce la productividad en un 33% ante la ausencia de uno; disponibilidad de tiempo limitada por responsabilidades académicas; falta de experiencia previa en WebSockets y Daphne, lo que genera curvas de aprendizaje; capacitación limitada del personal de ONPECO; y resistencia de los productores a usar tecnología.
Para mitigar estos riesgos, se plantea distribuir el conocimiento entre el equipo, documentar el código, priorizar funcionalidades críticas, realizar capacitaciones presenciales y diseñar una interfaz sencilla e intuitiva.
	Limitaciones de Recursos Económicos
Las limitaciones económicas incluyen un presupuesto limitado por el contexto académico, la ausencia de ingresos por monetización, el costo de conectividad en zonas rurales y el costo de mantenimiento post-entrega. Se mitigan utilizando software de código abierto, aprovechando equipos existentes, optimizando la aplicación para bajo consumo de datos y presupuestando un mantenimiento mensual de 8,800 DOP.
	Limitaciones de Recursos Materiales
En cuanto a recursos materiales, se identificaron equipos de desarrollo personales con capacidades limitadas, un servidor de producción que podría ser de baja capacidad, la ausencia de UPS en zonas rurales, conectividad de internet limitada y la falta de impresora para manuales. Se mitiga optimizando el código, recomendando especificaciones mínimas para el servidor, implementando backups automáticos y entregando manuales en formato digital.
	Limitaciones Tecnológicas
Las limitaciones tecnológicas incluyen el uso de SQLite, que puede ser insuficiente para alta concurrencia; entorno de desarrollo en Windows; chat basado en InMemoryChannelLayer; ausencia de despliegue en la nube; falta de certificado SSL/HTTPS; y ausencia de notificaciones push o por correo. Se mitiga documentando la migración a PostgreSQL, utilizando rutas relativas, recomendando channels_redis para producción y configurando HTTPS en el futuro.
	Limitaciones de Tiempo
Las limitaciones de tiempo incluyen un plazo de entrega ajustado de aproximadamente 4 semanas, disponibilidad limitada de los entrevistados de ONPECO, tiempo de capacitación reducido (2 horas) y tiempo de aprobación de usuarios. Se mitiga priorizando funcionalidades críticas, programando reuniones con anticipación y estableciendo un SLA de 48 horas para aprobaciones.
	Limitaciones de Acceso a Información
Se identificaron limitaciones en el acceso a información: falta de estudios previos que respalden cuantitativamente la problemática, datos limitados de productores de Azua y ausencia de precios de referencia oficiales. Se mitiga basando el diagnóstico en percepciones cualitativas, solicitando colaboración al Ministerio de Agricultura y definiendo rangos de precios de referencia por ONPECO.
	Limitaciones Legales y Normativas
Las limitaciones legales incluyen la protección de datos personales, la responsabilidad sobre la gestión de denuncias y la propiedad intelectual del código. Se mitiga implementando medidas de seguridad básicas, capacitando al personal de ONPECO e incluyendo cláusulas en el acta de conformidad.

Nota importante
Las limitaciones aquí descritas han sido identificadas a partir del cuestionario de entrevista a ONPECO, especialmente la pregunta 15 sobre obstáculos; de la documentación de desarrollo, incluyendo limitaciones técnicas de SQLite, Daphne y WebSockets; del contexto geográfico de la provincia de Azua y sus zonas rurales; y de la naturaleza académica del proyecto, con presupuesto limitado y tiempo ajustado.
XIV. CALENDARIO DE EJECUCIÓN DE PROYECTOS
A continuación, se presenta el calendario de ejecución del proyecto "Ventas Precio Justo ONPECO-UASD" (VPJ), describiendo las fechas de inicio y finalización de las actividades más importantes, considerando una jornada laboral de 8 horas diarias, de lunes a viernes, con un equipo de 3 desarrolladores trabajando en paralelo.
14.1 Fechas relevantes (Entregables del proyecto)
Código	Entregable	Fecha de entrega
E01	Informe de levantamiento de información	02/06/2026
E02	Informe de análisis del sistema actual	04/06/2026
E03	Informe de análisis del sistema propuesto	06/06/2026
E04	Prototipo funcional (versión alpha)	12/06/2026
E05	Sistema completo versión final	29/06/2026
E06	Capacitación al personal de ONPECO	02/07/2026
E07	Acta de conformidad y cierre del proyecto	06/07/2026
Tabla 50 Fechas relevantes de los entregables del proyecto.


Calendario detallado de actividades por día
A continuación, se presenta el calendario de ejecución día por día, considerando una jornada de 8 horas diarias por desarrollador (24 horas diarias de trabajo en equipo), de lunes a viernes.
Semana 1: Levantamiento, análisis y diseño
Día	Fecha	Actividades	Responsable	Entregable asociado
1	28/05/2026	Diseñar guía de entrevista (Act. 1). Realizar entrevista a ONPECO (Act. 2). Identificar actores, necesidades y obstáculos (Act. 3, 4, 5).	Equipo completo	Borrador E01
2	29/05/2026	Elaborar informe de levantamiento E01 (Act. 6). Describir sistema actual (Act. 7). Determinar instituciones (Act. 8). Diagrama de flujo actual (Act. 9).	Equipo completo	E01
3	30/05/2026	Narrativa del sistema actual (Act. 10). Identificar debilidades (Act. 11). Elaborar E02 (Act. 12). Estudios de factibilidad técnica, económica, operacional (Act. 13, 14, 15).	Equipo completo	E02
4	31/05/2026	Elaborar informe de factibilidad (Act. 16). Describir plataforma propuesta (Act. 17). Definir objetivos (Act. 18). Redactar justificación (Act. 19). Definir metodología (Act. 20).	Equipo completo	Borrador E03
5	01/06/2026	Diagrama de flujo de datos propuesto (Act. 21). Diagrama de casos de uso (Act. 22). Elaborar E03 (Act. 23). Diseñar arquitectura (Act. 24). Diseñar base de datos (Act. 25).	Equipo completo	E03
6	02/06/2026	Diseñar diagramas de conexión (Act. 26). Diseñar pantallas del sistema (Act. 27). Diseñar pantallas portal ONPECO (Act. 28). Describir campos y botones (Act. 29, 30).	Equipo completo	Diseño completo
	Tabla 51 Semana 1: Levantamiento, análisis y diseño.

Semana 2: Desarrollo (codificación)
Día	Fecha	Actividades	Responsable	Entregable asociado
7	03/06/2026	Configurar entorno de desarrollo (Act. 31). Desarrollar módulo de usuarios (Act. 32 - inicio).	Equipo completo	-
8	04/06/2026	Completar módulo de usuarios (Act. 32). Desarrollar módulo de marketplace (Act. 33 - inicio).	Equipo completo	-
9	05/06/2026	Completar módulo de marketplace (Act. 33). Desarrollar módulo de denuncias (Act. 34 - inicio).	Equipo completo	E04 (Prototipo funcional alpha)
10	06/06/2026	Completar módulo de denuncias (Act. 34). Desarrollar portal ONPECO (Act. 35)	Equipo completo	-
11	07/06/2026	Desarrollar sistema de respaldos (Act. 36). Desarrollar módulo de chat en tiempo real (Act. 37).	Equipo completo	-
12	08/06/2026	Desarrollar módulo de carrito y pedidos (Act. 39).	Equipo completo	-
13	09/06/2026	Desarrollar centro de acopio y balance de ventas (Act. 40).	Equipo completo	-
14	10/06/2026	Desarrollar exportaciones, calificaciones y reputación (Act. 41).	Equipo completo	_
15	11/06/2026	Desarrollar rankings y visibilidad de perfil (Act. 42). Desarrollar templates HTML con Bootstrap (Act. 38 - inicio)	Equipo completo	-
	Tabla 52 Semana 2: Desarrollo (codificación).
Semana 3: Desarrollo y pruebas
Día	Fecha	Actividades	Responsable	Entregable asociado
16	12/06/2026	Completar templates HTML (Act. 38). Realizar pruebas unitarias (Act. 43).	Equipo completo	-
17	13/06/2026	Pruebas de integración (Act. 44). Pruebas de roles y permisos (Act. 45).	Equipo completo	-
18	14/06/2026	Pruebas de WebSockets y chat (Act. 46). Pruebas de respaldos (Act. 47).	Equipo completo	Borradores manuales
19	5/06/2026	Documentar errores y soluciones (Act. 48).	Equipo completo	E05 (Sistema completo)
20	6/06/2026	Redactar manual de usuario (Act. 49 - inicio).	Equipo completo	Borradores manuales
21	17/06/2026	Redactar manual técnico (Act. 49).	Equipo completo	Borradores manuales
Tabla 53 Semana 3: Desarrollo y pruebas.

Semana 4: Documentación, entrega y cierre
Día	Fecha	Responsable	Entregable asociado
22	18/06/2026	Completar manuales (Act. 49).	_
23	19/06/2026	Preparar entrega final (Act. 49).	_
24	20/06/2026	Revisión final y ajustes.	_
25	21/06/2026	Revisión final y ajustes.	E05 (Sistema completo)
26	22/06/2026	Capacitar al personal de ONPECO (Act. 49)	E06 (Capacitación)
27	23/06/2026	Ajustes post-capacitación.	_
28	24/06/2026	Realizar reunión de cierre. Obtener acta de conformidad (Act. 49).	E07 (Acta de conformidad)
Tabla 54 Semana 4: Documentación, entrega y cierre.
Resumen del calendario:
Aspecto	Valor
Fecha de inicio	28 de mayo de 2026
Fecha de finalización	6 de julio de 2026
Días hábiles totales	28 días
Horas por día	8 horas
Días por semana	5 días (lunes a viernes)
Equipo	3 desarrolladores
Tabla 55 Resumen del calendario
Resumen de hitos:
Hito	Fecha
Inicio del proyecto	28/05/2026
Entrega E01	02/06/2026
Entrega E02	04/06/2026
Entrega E03	06/06/2026
Entrega E04 (Prototipo funcional)	12/06/2026
Entrega E05 (Sistema completo)	29/06/2026
Entrega E06 (Capacitación)	02/07/2026
Entrega E07 (Acta de conformidad)	06/07/2026
Tabla 56 Resumen de hitos

XV. DIAGRAMA DE GANTT
A continuación, se presenta el diagrama de Gantt del proyecto "Ventas Precio Justo ONPECO-UASD" (VPJ), que muestra la programación temporal de las actividades agrupadas por fases, considerando una jornada laboral de 8 horas diarias, de lunes a viernes, con fecha de inicio el 28 de mayo de 2026 y fecha de finalización el 6 de julio de 2026.
Diagrama de Gantt (MS Project)
   
   
XVI. HERRAMIENTAS DE SEGUIMIENTO Y CONTROL
En este apartado se describen las herramientas y métodos utilizados durante el desarrollo del proyecto "Ventas Precio Justo ONPECO-UASD" (VPJ) para garantizar el cumplimiento de los objetivos, el control de calidad, la gestión del tiempo y la comunicación efectiva entre los miembros del equipo y con el cliente (ONPECO).
Tabla XVI.1. Herramientas de gestión del proyecto
Herramienta	Propósito	Uso en el proyecto
Microsoft Project	Planificación y seguimiento del cronograma	Elaboración del diagrama de Gantt con 49 actividades. Control de fechas, duraciones y dependencias. Identificación de la ruta crítica.
Diagrama de Gantt	Visualización del avance del proyecto	Representación gráfica de las 49 actividades distribuidas en 5 semanas (28/05/2026 al 06/07/2026).
Lista de actividades (Punto VI)	Desglose estructurado del trabajo	49 actividades organizadas por etapas: levantamiento, análisis, factibilidad, diseño, desarrollo, pruebas, documentación y cierre.
Matriz de secuencia (Punto VIII)	Control de dependencias entre actividades	Establece el orden lógico de ejecución y evita cuellos de botella.
Matriz de tiempo (Punto IX)	Estimación de duraciones	Utiliza la fórmula PERT (O + 4M + P) / 6 para calcular tiempos estándar.
Matriz de costos (Punto XI)	Control presupuestario	Asigna costo por actividad (1,000 DOP/hora) y totaliza el proyecto en 223,927 DOP.
Matriz de riesgo (Punto XII)	Identificación y mitigación de riesgos	Registra 15 riesgos con su probabilidad, impacto y respuesta planificada.
Calendario de ejecución (Punto XIV)	Control de fechas clave	Define hitos y fechas de entrega de los 7 entregables (E01 al E07).
Tabla 57 Herramientas de gestión del proyecto.

2. Herramientas de control de versiones y código fuente
Herramienta	Propósito	Uso en el proyecto
Git	Control de versiones del código fuente	Permite rastrear cambios, revertir errores y mantener un historial de modificaciones.
Repositorio local	Almacenamiento del código	Carpeta cosecha_directa/ con toda la estructura del proyecto Django
Archivo DOCUMENTACION.md	Registro de cambios y decisiones	Documentación técnica de cada fase, comandos ejecutados, problemas y soluciones.
Tabla 58 Herramientas de control de versiones y código fuente.
Tabla XVI.3. Herramientas de comunicación y coordinación del equipo
Herramienta	Propósito	Uso en el proyecto
WhatsApp	Comunicación diaria del equipo	Grupo de WhatsApp creado para coordinación rápida entre los 3 desarrolladores y con ONPECO (según entrevista, pregunta 20).
Reuniones presenciales	Sincronización semanal	Reuniones cada lunes para revisar avances, resolver bloqueos y planificar la semana siguiente.
Reunión con ONPECO	Validación con el cliente	Reunión de seguimiento programada para el 16/06/2026 (según entrevista, pregunta 17).
Correo electrónico	Comunicación formal	Envío de entregables (E01, E02, E03, E04, E05) para revisión y aprobación.
Tabla 59 Herramientas de comunicación y coordinación del equipo.
4. Herramientas de gestión de calidad y pruebas
Herramienta	Propósito	Uso en el proyecto
Pruebas unitarias	Validación de componentes individuales	Prueba de modelos (User, Product, Complaint), vistas y formularios de forma aislada.
Pruebas de integración	Validación de interacción entre módulos	Prueba de denuncias desde productos, chat entre consumidor y productor, respaldos desde el admin.
Pruebas de roles y permisos	Validación de seguridad por rol	Verificación de que consumidores, productores, suplidores y reguladores tengan accesos correctos.
Pruebas de WebSockets	Validación del chat en tiempo real	Verificación de conexión, envío y recepción de mensajes simultáneos.
Pruebas de respaldos	Validación del sistema de backups	Verificación de generación manual y automática de archivos JSON, y restauración.
Registro de errores	Documentación de incidencias	Archivo DOCUMENTACION.md con problemas encontrados y soluciones aplicadas.
	Tabla 60 Herramientas de gestión de calidad y pruebas.
5. Herramientas de seguimiento con el cliente (ONPECO)
Herramienta	Propósito	Uso en el proyecto
Grupo de WhatsApp con ONPECO	Comunicación directa y seguimiento	Establecido según entrevista, pregunta 20. Para consultas rápidas y coordinación de reuniones.
Informes de avance (E01, E02, E03)	Documentación formal del progreso	Entregables con el estado del proyecto en cada fase.
Reuniones de seguimiento	Validación presencial	Reunión programada para el 16/06/2026 (pregunta 17 de la entrevista).
Acta de conformidad (E07)	Aceptación formal del proyecto	Documento firmado por ONPECO al finalizar el proyecto.
Manual de usuario (A03)	Capacitación y soporte	Guía para que ONPECO pueda administrar la plataforma después de la entrega.
Tabla 61 Herramientas de seguimiento con el cliente (ONPECO).
6. Herramientas de seguimiento técnico
Herramienta	Propósito	Uso en el proyecto
Servidor Daphne	Control del servidor ASGI	Permite monitorear logs de acceso, errores y conexiones WebSocket.
Backups automáticos	Control de integridad de datos	Generación diaria de respaldos JSON en carpeta /backups. Limpieza automática (mantiene últimos 10).
Logs del sistema	Registro de eventos	Archivo backup_log.txt con registro de ejecución de respaldos.
Panel de administración de Django	Control de datos en tiempo real	Acceso a http://127.0.0.1:8000/admin para gestionar usuarios, productos y denuncias.
Portal ONPECO	Monitoreo de métricas clave	Dashboard con gráfico de denuncias por mes y ranking de productos más consultados.
Tabla 62 Herramientas de seguimiento técnico.

XVII. CONCLUSIONES Y RECOMENDACIONES

17.1.1. Conclusiones sobre la problemática identificada

Se identificó que la provincia de Azua enfrenta un problema estructural en la comercialización de productos agrícolas, donde la presencia de múltiples intermediarios provoca que los productores reciban precios reducidos (hasta un 70% menos del precio final) mientras que los consumidores adquieren los mismos productos a precios elevados, incrementando el costo de la canasta familiar.

Se confirmó, mediante la entrevista realizada a ONPECO, que no existen antecedentes de soluciones tecnológicas formales para esta problemática en la región. Los productores dependen de métodos informales como contactos telefónicos y acuerdos verbales, lo que limita su capacidad de comercialización y genera pérdidas económicas por productos no vendidos.
Se identificaron los principales obstáculos para la adopción de la plataforma: resistencia al cambio por parte de los productores (70% de probabilidad), falta de acceso a internet en zonas rurales (65%) y baja educación digital (60%), según la matriz de riesgo desarrollada.
17.1.2. Conclusiones sobre el desarrollo técnico
se desarrolló exitosamente una plataforma web funcional en Python con Django, que permite el registro diferenciado de usuarios por roles (consumidor, productor, suplidor y regulador ONPECO), la publicación y gestión de productos agrícolas, un sistema de denuncias con tickets único y seguimiento, y un chat en tiempo real mediante WebSockets con Daphne.
Se implementó un sistema de respaldos automáticos que genera archivos JSON diarios a las 2:00 AM mediante el Programador de Tareas de Windows, manteniendo automáticamente los últimos 10 backups y permitiendo la restauración del sistema en caso de fallos.
Se desarrolló un portal exclusivo para ONPECO con dashboard personalizado, gráfico de denuncias por mes utilizando Chart.js, ranking de productos más consultados (ordenados por view_count), y gestión completa de aprobación de productores y suplidores.
La arquitectura técnica implementada (Django + Daphne + SQLite + Bootstrap) demostró ser adecuada para el alcance del proyecto, permitiendo la integración de WebSockets para chat en tiempo real y una interfaz responsive accesible desde dispositivos móviles
17.1.3. Conclusiones sobre la planificación y gestión del proyecto
El proyecto se planificó con 49 actividades distribuidas en 8 etapas (levantamiento, análisis actual, factibilidad, análisis propuesto, diseño, desarrollo, pruebas, documentación y cierre), con una duración total estimada de 28 días hábiles (28/05/2026 al 06/07/2026) y una carga de 40 horas semanales por desarrollador (8 horas diarias × 5 días).
Se estimó un costo total del proyecto de 223,927 DOP, considerando 203.57 horas de desarrollo a una tarifa de 1,000 DOP/hora, más un 10% de contingencias. Este presupuesto no incluye equipos de hardware (asumiendo equipos personales de los desarrolladores) ni costos operativos anuales del cliente.
Se identificaron 15 riesgos potenciales, siendo los más críticos: resistencia al cambio de los productores (70% de probabilidad), falta de acceso a internet en zonas rurales (65%), y responsabilidad legal sobre la gestión de denuncias. Para cada riesgo se definió una estrategia de mitigación específica.
17.1.4. Conclusiones sobre el cumplimiento de objetivos
Se cumplió el objetivo general de desarrollar una plataforma digital en Python que permite la interacción directa entre productores y consumidores de la provincia de Azua, facilitando el acceso a información sobre precios, oferta y disponibilidad de productos agrícolas.
Se cumplieron los cuatro objetivos específicos: identificación de necesidades mediante entrevista a ONPECO; diseño de plataforma con reducción de intermediación; definición de funcionalidades como publicación, búsqueda, comparación y denuncias; y promoción de visibilidad de productos locales mediante ranking y portal ONPECO.
Se entregaron los 7 entregables planificados (E01 al E07) en las fechas establecidas en el calendario de ejecución, incluyendo informes de análisis, prototipo funcional, sistema completo, manuales y acta de conformidad.
17.1.5. Conclusiones sobre el impacto esperado
La plataforma tiene el potencial de reducir la dependencia de intermediarios al conectar directamente a productores y consumidores, lo que podría aumentar los ingresos de los agricultores (estimado en un 30-40%) y reducir los precios para los consumidores (estimado en un 20-25%), según estudios previos referenciados en los antecedentes.
El sistema de denuncias con seguimiento permitirá a ONPECO ejercer su rol regulador de manera efectiva, con trazabilidad de cada reporte, historial de cambios de estado y posibilidad de agregar comentarios en cada actualización.
Los respaldos automáticos garantizan la integridad de los datos ante fallos técnicos, cortes de energía o pérdida de información, aspecto crítico considerando las limitaciones de infraestructura eléctrica en zonas rurales de Azua.

17.2.1. Recomendaciones para ONPECO (cliente)
Se recomienda a ONPECO adquirir un UPS (Sistema de Alimentación Ininterrumpida) para el equipo que alojará la plataforma, con el fin de proteger la integridad de la base de datos ante cortes de energía eléctrica, frecuentes en zonas rurales de Azua. El costo estimado es de 5,500 DOP.
Se sugiere designar un administrador dedicado dentro de ONPECO para la gestión diaria de la plataforma, incluyendo la aprobación de productores, revisión de denuncias y monitoreo de respaldos. Este rol requiere aproximadamente 4 horas semanales.
Es recomendable realizar campañas de difusión de la plataforma entre productores y consumidores de Azua, utilizando canales como radios locales, redes sociales (WhatsApp, Facebook) y coordinación con la UASD Recinto Azua y el Ministerio de Agricultura.
Se recomienda establecer un protocolo de respuesta a denuncias que defina plazos máximos para cada estado (por ejemplo, de pendiente a en investigación en un máximo de 48 horas) y asigne responsables específicos dentro de ONPECO.
Se sugiere presupuestar mantenimiento continuo de la plataforma, estimado en 8,800 DOP mensuales según el punto V, incluyendo actualizaciones de seguridad, corrección de errores y soporte a usuarios.
Finalmente, se recomienda capacitar al personal de ONPECO en el uso del portal y la gestión de denuncias, utilizando el manual de usuario entregado (A03). Se sugiere una capacitación de refuerzo a los 3 meses de uso.
17.2.2. Recomendaciones técnicas para trabajos futuros
Se recomienda migrar a PostgreSQL como base de datos en lugar de SQLite cuando el volumen de usuarios y transacciones lo requiera, ya que PostgreSQL soporta mejor las escrituras concurrentes y tiene mayor escalabilidad.
Se sugiere implementar notificaciones por correo electrónico para alertar a ONPECO sobre nuevas denuncias de prioridad alta y a productores sobre productos con stock bajo, mejorando la experiencia de los usuarios.
Es recomendable configurar HTTPS con certificado SSL (por ejemplo, Let's Encrypt gratuito) para garantizar la seguridad de los datos de los usuarios, cumpliendo con la Ley de Protección de Datos Personales de República Dominicana.
Se recomienda desarrollar una aplicación móvil nativa (iOS o Android) o un Progressive Web App (PWA) para mejorar la experiencia en dispositivos móviles y permitir notificaciones push.
Se sugiere implementar una pasarela de pagos (como Yappy, PayPal o tarjeta de crédito) para facilitar las transacciones entre consumidores y productores directamente dentro de la plataforma.
Se recomienda agregar geolocalización y mapas para que los consumidores puedan visualizar la ubicación de los productores y calcular distancias para la compra o entrega.
Se sugiere implementar exportación de reportes a Excel y PDF para que ONPECO pueda generar informes oficiales de denuncias, productos y usuarios.
Es recomendable migrar de InMemoryChannelLayer a Redis para el chat en tiempo real cuando se requiera mayor escalabilidad o se despliegue en múltiples servidores.
Finalmente, se recomienda desplegar la plataforma en la nube (AWS, Google Cloud, Azure o DigitalOcean) para garantizar disponibilidad 24/7 y acceso remoto desde cualquier ubicación, eliminando la dependencia de un servidor físico local.
17.2.3. Recomendaciones para la adopción por parte de los productores
Se recomienda realizar talleres presenciales en las comunidades rurales de Azua para capacitar a los productores en el uso de la plataforma, aprovechando la colaboración de la UASD Recinto Azua y el Ministerio de Agricultura, con el fin de mitigar la resistencia al cambio (70% de riesgo).
Se sugiere optimizar las imágenes de los productos (compresión, reducción de tamaño) para que la plataforma funcione correctamente en zonas con conexiones de internet lentas (2 Mbps), mitigando así la falta de acceso a internet (65% de riesgo).
Se recomienda designar "embajadores digitales" entre los productores más jóvenes o con mayor afinidad tecnológica, para que ayuden a otros productores a registrarse y publicar sus productos, mitigando la baja educación digital (60% de riesgo).
Finalmente, se sugiere ofrecer incentivos iniciales, como destacar productos gratis durante el primer mes, a los primeros productores que se registren y publiquen productos, para fomentar la adopción temprana.
17.2.4. Recomendaciones para trabajos de investigación futuros
Se recomienda realizar un estudio cuantitativo sobre el impacto económico de la plataforma en los ingresos de los productores y el gasto de los consumidores después de 6 meses de uso, para validar los supuestos de la justificación del proyecto.
Se sugiere investigar la viabilidad de expansión de la plataforma a otras provincias de República Dominicana, como San Juan, Barahona y La Vega, que tienen características agrícolas similares a Azua.
Se recomienda evaluar la integración con programas gubernamentales existentes, como CONASSAN y el Ministerio de Agricultura, para fortalecer la seguridad alimentaria y el apoyo a pequeños agricultores.
Resumen ejecutivo de conclusiones y recomendaciones
Categoría	Cantidad
Conclusiones totales	16
Recomendaciones para ONPECO	6
Recomendaciones técnicas para trabajos futuros	9
Recomendaciones para adopción de productores	4
Recomendaciones para investigación futura	3
TOTAL	38 puntos
	Tabla 63 Resumen ejecutivo de conclusiones y recomendaciones.
XVIII. BIBLIOGRAFÍA Y REFERENCIAS ELECTRÓNICAS
A continuación, se presentan las fuentes bibliográficas y electrónicas consultadas para el desarrollo del proyecto "Ventas Precio Justo OnPECO-UASD" (VPJ), organizadas según las normas APA (7ª edición).
	Martínez, J. (2021). Mercados digitales para pequeños agricultores en América Latina: Impacto en la reducción de intermediarios. Editorial Universidad de Costa Rica.
	Pérez, R., & Gómez, L. (2019). Comercio justo y economía colaborativa: Modelos alternativos para el desarrollo rural. Fondo Editorial de la Pontificia Universidad Javeriana.
	República Dominicana, Ley No. 172-13 sobre Protección de Datos Personales. (2013). Gaceta Oficial No. 10723. Santo Domingo: Congreso Nacional de la República Dominicana.
	Sampieri, R. H., Fernández, C., & Baptista, P. (2018). Metodología de la investigación (6ª ed.). McGraw-Hill.
2. Artículos de revistas científicas
Referencia
	Rodríguez, M., & Díaz, E. (2022). Impacto de los intermediarios en la cadena de valor de productos agrícolas en República Dominicana. Revista Dominicana de Economía Agrícola, 15(2), 45-62.
	Vargas, C., & Méndez, F. (2020). Tecnologías de código abierto para el desarrollo de plataformas de comercio electrónico rural. Revista Latinoamericana de Ingeniería de Software, 8(3), 112-128.


3. Documentación técnica y manuales oficiales
Referencia
	Django Software Foundation. (2023). Documentación de Django 4.2. Recuperado de https://docs.djangoproject.com/en/4.2/
	Python Software Foundation. (2023). Documentación oficial de Python 3.11. Recuperado de https://docs.python.org/3.11/
4. Sitios web y recursos en línea
	Aula Fácil. (2023). Curso de Gestión de Proyectos con Microsoft Project: Diagrama de Gantt. Recuperado de https://www.aulafacil.com/cursos/excel-word-powerpoint-access/gestion-de-proyectos-microsoft-project/diagrama-de-gantt-l12890
	Efiempresa. (2023). El objetivo de cualquier proyecto consiste en satisfacer necesidades. Recuperado de https://efiempresa.com/blog/el-objetivo-de-cualquier-proyecto-consiste-en-satisfacer-necesidades-las-cuales-son-su-fuerza-impulsora-su-seguimiento-permitira-realizar-todo-el-proceso-de-gestion/
	Montse Peñarroya. (2023). Cómo hacer un resumen ejecutivo para un plan de empresa. Recuperado de https://www.montsepenarroya.com/como-hacer-un-resumen-ejecutivo-para-un-plan-de-empresa/
	Universidad Autónoma de Santo Domingo (UASD). (2023). Guía para la elaboración de monografías y trabajos de grado. Recuperado de https://www.uasd.edu.do/investigacion
	UBJ Online. (2023). ¿En qué consiste el alcance del proyecto? Recuperado de https://www.ubjonline.mx/en-que-consiste-el-alcance-del-proyecto/
	Universidad Rafael Landívar (URL). (2010). Verbos observables para la definición de objetivos de investigación. Recuperado de http://courseware.url.edu.gt/Facultades/Facultad%20de%20Ciencias%20Econ%C3%B3micas/T%C3%A9cnicas%20B%C3%A1sicas%20de%20Investigaci%C3%B3n/Segundo%20ciclo%202010/Planteamiento%20del%20problema/01%20Planteamiento%20del%20problema/verbos_para_objetivos_generales_y_objetivos_especficos.html
5. Entrevista y fuentes primarias
Referencia
González, R., González, L., Rivas, L. A., & Cabreras, N. (2026, 28 de mayo). Entrevista para el levantamiento de información del proyecto "Ventas Precio Justo ONPECO-UASD" Documento no publicado. ONPECO, Santo Domingo, República Dominicana.
6. Normas y estándares técnicos
Referencia
	International Organization for Standardization (ISO). (2015). *ISO 9001:2015 - Sistema de gestión de calidad*. Ginebra: ISO.
	World Wide Web Consortium (W3C). (2022). HTML5: A vocabulary and associated APIs for HTML and XHTML. Recuperado de https://www.w3.org/TR/html5/
7. Herramientas de desarrollo utilizadas (referencias técnicas)
Referencia
	Microsoft Corporation. (2023). *Windows 10/11: Documentación técnica para desarrolladores*. Recuperado de https://docs.microsoft.com/es-es/windows/
	SQLite Consortium. (2023). SQLite Documentation. Recuperado de https://www.sqlite.org/docs.html
	Git SCM. (2023). Git documentation. Recuperado de https://git-scm.com/doc
	Visual Studio Code. (2023). VS Code documentation. Recuperado de https://code.visualstudio.com/docs
Resumen de referencias por categoría
Categoría	Cantidad
Libros y documentos académicos	4
Artículos de revistas científicas	2
Documentación técnica y manuales oficiales	7
Sitios web y recursos en línea	6
Entrevistas y fuentes primarias	1
Normas y estándares técnicos	2
Herramientas de desarrollo	4
TOTAL	26 referencias
Tabla 64 Resumen de referencias por categoría.


XIX. ANEXOS
A01. Guía de entrevista (Primera visita - 28 de mayo de 2026)
Entrevistados:
Primera visita
	Rita González (Coordinadora ejecutiva)
	Leonor González (Coordinadora operativa)
	Leonel A. Rivas P. (Coordinador técnico)
	Nayeli Cabrera (Administración)
Institución: ONPECO (Oficina Nacional de Protección al Consumidor)
Objetivo: Recolectar información sobre la problemática de precios de productos agrícolas en la provincia de Azua, identificar necesidades y funcionalidades deseadas.

Bloque 1 – Entendiendo el problema
Pregunta 1: ¿Cuál es el problema concreto que han identificado en Azua con los precios de los productos agrícolas?
Respuesta: El principal problema identificado es la existencia de intermediarios que acaparan los productos agrícolas incluso antes de ser cosechados. Esto provoca que los consumidores adquieran los productos a precios muy elevados, mientras que los productores reciben una cantidad menor por su producción. Esta problemática afecta a productores de distintas provincias que enfrentan dificultades para comercializar sus productos, generando pérdidas económicas y deterioro de productos no vendidos.
Pregunta 2: ¿Qué consecuencias tiene ese problema para los agricultores? ¿Y para los consumidores?
Respuesta: Los agricultores reciben un pago menor por sus productos debido a la intervención de intermediarios. Los pequeños y medianos productores enfrentan dificultades para competir en el mercado y, en algunos casos, no logran vender toda su producción, generando pérdidas económicas. Los consumidores se ven perjudicados al tener que adquirir los productos a precios más altos, aumentando el gasto de la canasta familiar y reduciendo el acceso a productos frescos.
Pregunta 3: ¿Han intentado resolverlo antes? ¿Qué han probado y por qué no funcionó?
Respuesta: No se han realizado intentos previos para solucionar esta problemática. Señalaron la importancia de desarrollar una iniciativa orientada a visibilizar el fortalecimiento de los productos locales y crear una plataforma innovadora que fomente el comercio electrónico entre productores y consumidores.
Pregunta 4: ¿Tienen algún dato o estudio que respalde que este es un problema real?
Respuesta: No existe un estudio previo que permita conocer un diagnóstico formal de la problemática. No se dispone de encuestas, estadísticas ni grupos focales que respalden la situación; sin embargo, existe la percepción de que el comercio no es justo para los pequeños productores.
Bloque 2 – Conociendo a los usuarios
Pregunta 5: ¿Quiénes son las personas que usarían esta aplicación?
Respuesta: Los usuarios principales son los productores agrícolas y los consumidores de la provincia de Azua. Los productores utilizarían la plataforma para promocionar y comercializar sus productos de manera directa. Los consumidores la emplearían para acceder a información, comparar precios y realizar compras.
Pregunta 6: ¿Qué saben hacer con la tecnología?
Respuesta: La mayoría de los productores posee conocimientos básicos en el manejo de dispositivos electrónicos, utilizando herramientas como WhatsApp y Facebook para sus actividades diarias.
Pregunta 7: ¿Tienen acceso a internet?
Respuesta: Los productores cuentan con acceso a internet en la mayoría de las zonas, facilitando el uso de plataformas digitales para la comunicación y comercialización.
Bloque 3 – Funcionalidades deseadas
Pregunta 8: Si pudieran tener una aplicación que resuelva el problema de los precios, ¿qué debería hacer?
Respuesta: La aplicación debe permitir comprar y pagar de forma directa, visualizar fotografías, comparar precios, consultar ofertas, gestionar productos, organizar por categorías, mostrar disponibilidad de inventario y enviar notificaciones.
Pregunta 9: Para la parte de denuncias, ¿qué tipo de denuncias esperan recibir?
Respuesta: Se requiere un sistema de retroalimentación que permita a los consumidores expresar quejas, sugerencias y opiniones, generando una base de datos organizada para almacenar y gestionar la información.
Pregunta 10: ¿Qué información sería indispensable que tenga la aplicación?
Respuesta: La aplicación debe incorporar información detallada sobre los insumos agrícolas, tipo de productos, disponibilidad, ofertas, notificaciones, contenidos educativos, indicadores de efectividad y una interfaz amigable.
Bloque 5 – Expectativas y limitaciones
Pregunta 14: ¿Qué esperarían que logre esta aplicación en sus primeros 6 meses?
Respuesta: Alcanzar un alto nivel de satisfacción entre productores y consumidores, lograr que los usuarios reconozcan la utilidad de la plataforma y generar un volumen significativo de transacciones comerciales.
Pregunta 15: ¿Qué obstáculos anticipan para que los agricultores usen la aplicación?
Respuesta: Resistencia al cambio, limitaciones en el acceso a internet, dificultades con educación digital, necesidad de auspiciadores, personal para administración y actitud favorable de los usuarios.
Pregunta 16: ¿Hay algún requisito legal que debamos conocer?
Respuesta: Garantizar la protección y seguridad de los datos de los usuarios, evitando vulneración de información personal y asegurando respeto a la privacidad.
Bloque 6 – Logística para el monográfico
Pregunta 17: ¿Qué disponibilidad de tiempo tienen para reunirse?
Respuesta: Se programó un encuentro para el 16 de junio de 2026, a la 1:00 p.m.
Pregunta 18: ¿Podríamos realizar entrevistas a profundidad más adelante?
Respuesta: Se programó una visita a la provincia de Azua con autoridades de ONPECO.
Pregunta 19: ¿Hay algún documento que nos puedan compartir?
Respuesta: Se facilitará una tesis relacionada con los requerimientos para el desarrollo de la aplicación.
Pregunta 20: ¿Cuál es la mejor forma de contactarlos para dar seguimiento?
Respuesta: Se estableció un grupo de WhatsApp como medio principal de comunicación y seguimiento.
A02. Diccionario de datos físico de la base de datos
Tabla: users_user (Usuarios del sistema - modelo personalizado)
Campo	Tipo	Nulo	Descripción
Id	Integer (Auto)	No	Identificador único del usuario
username	String (150)	No	Nombre de usuario único
Email	String (254)	No	Correo electrónico
password	String (128)	No	Contraseña encriptada
Role	String (20)	No	Rol: consumidor, productor, suplidor, regulador, acopio
Pone	String (15)	Si	Número de teléfono
address	Text	Si	Dirección física
business_name	String (100)	Si	Nombre del negocio (para productores/suplidores)
is_approved	Boolean	No	Aprobado por ONPECO (False por defecto)
is_staff	Boolean	No	Acceso al panel de administración
is_active	Boolean	No	Usuario activo
date_joined	DateTime	No	Fecha de registro
last_login	DateTime	Si Nulo	Último inicio de sesión
Tabla 65 Diccionario de datos físico de la base de datos




Tabla: marketplace_product (Productos agrícolas)
Campo	Tipo	Nulo	Descripción
Id	Integer (Auto)	No	Identificador único del producto
vendedor_id	Integer (FK)	No	Usuario que vende (productor o suplidor)
productor_origen_id	Integer (FK)	Si	Productor original (para suplidores)
Name	String (100)	No	Nombre del producto
description	Text	No	Descripción detallada
category	String (20)	No	Categoría: frutas, verduras, granos, tubérculos, otros
Price	Decimal (10,2)	No	Precio en pesos dominicanos
Unit	String (10)	No	Unidad: kg, lb, unidad, docena
Stock	Integer	No	Cantidad disponible
stock_minimo	Integer	No	Stock mínimo para alerta (default: 5)
available	Boolean	No	Disponible para venta
view_count	Integer	No	Contador de visitas
Image	String (100)	Si	Ruta de la imagen del producto
created_at	DateTime	No	Fecha de creación
updated_at	DateTime	No	Fecha de última actualización
Tabla 66 marketplace_product (Productos agrícolas)
Tabla: complaints_complaint (Denuncias)
Campo	Tipo	Nulo	Descripción
Id	Integer (Auto)	No	Identificador único
complaint_id	Integer (FK)	No	Denuncia asociada
comment	Text	No	Comentario de seguimiento
old_status	String (20)	Estado anterior	Estado anterior
new_status	String (20)	No	Estado nuevo
created_by_id	Integer (FK)	No	Usuario que hizo la actualización
created_at	DateTime	No	Fecha de la actualización
Tabla 67 complaints_complaint (Denuncias)

Tabla: cart_cart (Carrito de compras)
Campo	Tipo	Nulo	Descripción
Id	Integer (Auto)	No	Identificador único del carrito
user_id	Integer (FK)	No	Usuario propietario del carrito
created_at	DateTime	No	Fecha de creación
updated_at	DateTime	No	Fecha de última actualización
Tabla 69 cart_cart (Carrito de compras)
Tabla: cart_cartitem (Ítems del carrito)
Campo	Tipo	Nulo	Descripción
Id	Integer (Auto)	No	Identificador único
cart_id	Integer (FK)	No	Carrito al que pertenece
product_id	Integer (FK)	No	Producto agregado
quantity	Integer	No	Cantidad del producto
added_at	DateTime	No	Fecha de adición
Tabla 70 cart_cartitem (Ítems del carrito)
Tabla: cart_order (Pedidos)
Campo	Tipo	Nulo	Descripción
Id	Integer (Auto)	No	Identificador único del pedido
user_id	Integer (FK)	No	Consumidor que realizó el pedido
seller_id	Integer (FK)	No	Vendedor (productor o suplidor)
acopio_id	Integer (FK)	Si	Centro de acopio que gestiona el pedido
created_at	DateTime	No	Fecha de creación
updated_at	DateTime	No	Fecha de actualización
estatus	String (20)	No	Estado: pending, confirmed, preparing, delivered, cancelled
total_amount	Decimal (10,2)	No	Monto total del pedido
delivery_type	String (20)	No	Tipo: delivery, pickup
shipping_address	Text	Si	Dirección de entrega
pickup_location	String (255)	Si	Punto de recogida
phone_number	String (20)	Si	Teléfono de contacto
delivery_instructions	Text	Si	Instrucciones adicionales
payment_breakdown	JSON	Si	Desglose de pagos por productor
payment_status	String (20)	No	Estado: pending, partial, paid
payment_date	DateTime	Si	Fecha de pago
Tabla 71 cart_order (Pedidos)
Tabla: cart_orderitem (Ítems del pedido)
Campo	Tipo	Nulo	Descripción
Id	Integer (Auto)	No	Identificador único
order_id	Integer (FK)	No	Pedido al que pertenece
product_id	Integer (FK)	No	Producto vendido
quantity	Integer	No	Cantidad vendida
Price	Decimal (10,2)	No	Precio unitario al momento de la venta
Tabla 72 cart_orderitem (Ítems del pedido)

A03. Manual de usuario
	Manual de Usuario - Ventas Precio Justo ONPECO-UASD (VPJ)
	Instrucciones para Consumidores
	Instrucciones para Productores
	Instrucciones para Reguladores ONPECO
	Instrucciones para el Centro de Acopio
	Solución de problemas comunes

Paso	Acción
1	Registrarse en la plataforma seleccionando el rol "Consumidor"
2	Iniciar sesión con usuario y contraseña
3	Navegar por el catálogo de productos en la sección "Productos"
4	Ver detalle de un producto haciendo clic en "Ver Detalle"
5	Agregar productos al carrito haciendo clic en "Agregar al Carrito"
6	Ver el carrito en "Mi Carrito" para revisar productos seleccionados
7	Proceder al pago en "Checkout" completando datos de entrega
8	Confirmar el pedido y recibir número de seguimiento
9	Ver historial de pedidos en "Mis Pedidos"
10	Crear denuncias en "Mis Denuncias" si detecta precios abusivos
Paso	Acción
1	Registrarse seleccionando el rol "Productor"
2	Esperar aprobación de ONPECO (recibirá notificación)
3	Iniciar sesión una vez aprobado
4	Publicar productos en "Mis Productos" → "Crear Producto"
5	Completar datos: nombre, descripción, precio, stock, categoría, imagen
6	Gestionar productos (editar, eliminar, actualizar stock)
7	Ver ventas realizadas en "Mis Ventas"
8	Consultar balance en "Balance de Ventas" (total vendido, pagado, pendiente)
9	Responder mensajes de consumidores en "Mis Conversaciones"
Paso	Acción
1	Iniciar sesión con usuario proporcionado por ONPECO
2	Acceder al portal ONPECO desde el menú principal
3	Aprobar productores en "Aprobar Productores" (pendientes listados)
4	Aprobar suplidores en "Aprobar Suplidores"
5	Gestionar denuncias en "Gestionar Denuncias"
6	Cambiar estado de denuncia (pendiente → investigación → resuelto/rechazado)
7	Agregar comentarios de seguimiento en cada actualización
8	Ver gráfico de denuncias por mes en "Reportes"
9	Ver ranking de productos más consultados en "Productos Top"
10	Gestionar respaldos en "Gestión de Backups"
Paso	Acción
1	Iniciar sesión con usuario centro acopió
2	Acceder a "Centro de Acopio" en el menú principal
3	Ver lista de pedidos recibidos
4	Ver detalle de cada pedido con desglose por productor
5	Registrar pagos a productores actualizando payment_status
6	Coordinar entregas con consumidores según tipo seleccionado
Problema	Solución
No puedo iniciar sesión	Verificar usuario y contraseña. Usar opción "Recordar contraseña"
Mi producto no aparece en el catálogo	Verificar que esté aprobado y que available = True
El carrito no guarda mis productos	Verificar que la sesión esté activa. Cerrar y abrir navegador
El chat no envía mensajes	Verificar conexión a internet. Recargar la página
No veo el botón "Mis Ventas"	Solo visible para productores y suplidores aprobados
Tabla 73 Manual de usuario

Primera visita
  



Segunda Visita
  



A04. Capturas de pantalla del sistema
(Incluir aquí las capturas de pantalla de las principales interfaces del sistema)
Figura A04.1   Página de inicio de VPJ
 
Figura A04.2 Catálogo de productos
 
Figura A04.4 Carrito de compras
 
Figura A04.5 Proceso de checkout(compra)
 


Figura A04.6 Mis pedidos (consumidor)
 
Figura A04.7 panel entidad reguladora (1)
 


Panel entidad reguladora (2)
 
Figura A04.9 Gestión de denuncias (ONPECO) 1
 


Figura A04.10 Balance de ventas (productor)
 
Figura A04.11 Centro de Acopio - Pedidos recibidos
 


Pedidos centro de acopio
 
Actualización de estado centro de acopio
 


Pedidos a distintos productores
 
 



Figura A04.12 Chat en tiempo real
 
Perfil de productore
 


Calificar a un productor
 

Mis Productos
 


Perfil del Productor
 
 Hacer mi perfil público
  

 Inicio de Sesión
 

Aprobar Productores
 
  Productores aprobados
 


Aprobar suplidores
 Suplidores aprobados
 Gestionar Reputación
 


Productos más consultados o más visitado
 Productores más Denunciados
 
