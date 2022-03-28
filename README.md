# Situacion Evaluativa Al Estudiante

| Sigla   | Nombre Asignatura | Horas semana |
| :---:   |      :----:       |     :---:    |
| PGY3121 | Programación Web  |     6 h      |

|           Ítem           |  Puntaje  | % Ponderación |
|           :---:          |   :----:  |     :---:     |
| Competencia Especialidad | 45 puntos |      25%      |

## Instrucciones generales:

- La Entrega de Encargo con Presentación tiene un 100% de ponderación del puntaje total de esta Evaluación.
- El tiempo para desarrollar la Presentación es de 10 minutos por equipo, más 5 minutos para una ronda de preguntas.
- Deberá entregar: 
	1. Presentación del sistema.
	2. Código fuente del proyecto
- Los equipos de trabajo tendrán **las sesiones de la semana 4 para desarrollar** este encargo a partir de la fecha de entrega de las instrucciones por parte del docente.
* Puntos en color tenue son para entregas POSTERIORES.

### Entregables
El desarrollo del sistema debe realizarse según las consideraciones de diseño y requerimientos enunciadas. La interfaz de usuario debe ser diseñada por cada equipo y debe considerar ser adaptable a tres tamaños de pantalla: Smartphone, Tablet y PC de escritorio, el uso de grilla de 12 columnas y el uso de algún framework frontend.

- El modelo de datos debe adaptarse al desarrollo del proyecto.
- El back-end del proyecto debe desarrollarse utilizando Python.
- Base de datos debe ser Oracle.

Esta presentación tendrá una duración máxima de 10 minutos, dejando 5 minutos para las preguntas que
realizará el docente de la asignatura.
La Presentación (slides en formato .ppt / .pptx / .odp)
- Presentación del Proyecto
- Solución propuesta
- Principales características del producto desarrollado
- Presentación del producto desarrollado.
- Conclusión

Los trabajos entregados fuera de plazo serán calificados con una 1.0

### Requisitos específicos: 
(requisitos en color tenue son para entregas siguientes)

Para el desarrollo del sistema solicitado, los equipos de trabajo deben considerar los siguientes aspectos:
- Desarrolla el proyecto de software con una correcta implementación de arquitectura, separando frontend y back-end.
- Desarrolla una interfaz que se adapta a 3 tamaños de pantalla para su utilización en dispositivos móviles basada en una grilla de 12 columnas.
- Utiliza un framework de back-end para realizar trabajo integrado con el servidor.
- Genera un modelo de datos dentro del framework que cumpla con las necesidades de la organización.
- Implementa un servicio Rest que será parte de la solución planteada.
- Maneja y organiza el trabajo grupal utilizando repositorios. 

## Caso: Forma B

Los vecinos de una comunidad comenzaron a realizar la venta de productos para jardinería como maceteros, tierra de hojas, flores y arbustos, todo esto para ayudar a una fundación sin fines de lucro, todo partió a través de las redes sociales, pero en la actualidad es casi imposible dar abasto a la demanda a través de las redes sociales.

Por eso, a contactado a los alumnos del Duoc para que puedan ayudarles a construir una aplicación web que permita a sus usuarios elaborar listas de compras con la intención de permitir a los vecinos a ordenar sus presupuestos, mejorar sus finanzas, realizar el aporte a la fundación sin fines de lucro y mejorar la venta y el despacho de sus productos. 

### Los principales objetivos de la aplicación web son:
- Contar con una plataforma en internet para promover sus productos a usuarios registrados, que indique
el stock real de productos disponibles
- Entregar el servicio venta en línea.
- Permitir al cliente para monitorear sus compras.
- Mejorar el proceso de logística de sus productos a los clientes mediante el seguimiento del despacho.
- Permitir generar descuentos o promociones en la página principal
- Permitir subscribirse con una donación a la fundación sin fines de lucro, esta información ira directamente a la fundación. Con el fin de motivar a sus clientes, se otorgará un 5% de descuento en el total de la venta a todos los clientes que estén suscritos. 

### Funcionalidades del Sistema
- El sistema debe permitir registrar clientes para acceder a los servicios de ventas.
- El sistema debe permitir a los clientes generar una compra, descontando los productos del stock una vez
creada la venta y realizar descuentos en caso de tratarse de una promoción o de un cliente suscrito.
- Para los usuarios registrados el sistema debe permitir ver un historial de ventas realizadas, además, del
estado del despacho de las ventas.
- Para el despacho de los productos, el sistema WEB debe entregar una traza de seguimiento del despacho en el caso de los envíos a domicilio de clientes registrados, mostrando fecha y hora en que se toma el pedido, se despacha y es recibido por el cliente, cerrando el ciclo.
- El sistema debe permitir a los usuarios registrados poder subscribirse o des suscribirse de la donación a la fundación sin fines de lucro.
- Se deben crear mantenedores para la información relativa a clientes, usuarios, productos, promociones o descuentos.
- El sistema debe permitir mostrar las opciones de acuerdo con los perfiles de cada usuario. 

### Características del producto
- La aplicación por desarrollar debe ser en ambiente web, con acceso desde internet, ya que será necesario
el registro de clientes, la publicación de productos u solicitudes de venta línea.
- El sistema debe ser construido en arquitectura web mediante modelo de capas, logrando una separación
de la interfaz gráfica, reglas de negocio y repositorio de datos.
- El sistema debe considerar acceder a servicios Rest al momento de simular la suscripción con la fundación,
se debe generar un servicio que permita registrar y eliminar las suscripciones (simulación).
- Es sistema debe considerar acceder a el servicio Rest de la fundación al momento de la venta para validar
si el cliente este o no suscrito y aplicar el descuento al total de la venta.
- Se debe crear un servicio Rest que simulé pertenecer a la fundación y proporcione tres servicios:
	1. Ingresar Suscriptores 
	2. Eliminar Suscriptores
	3. Consultar vigencia de los suscriptores

### Restricciones
- La aplicación debe utilizar la base de datos ORACLE

### Para esta entrega considerar:
- SOLO SE DEBE DESARROLLAR LOS ASPECTOS QUE INDICA LA RUBRICA PARA LA EVALUACIÓN N°1







