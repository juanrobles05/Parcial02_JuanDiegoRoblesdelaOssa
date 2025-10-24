## ANÁLISIS: Modificación del Diseño para Comunicación con Servicio de Historial

### Pregunta
*"¿Cómo modificaría su diseño si este microservicio tuviera que comunicarse con otro servicio que almacena el historial de cálculos en una base de datos externa?"*

### Respuesta
Modificaria el microservicio para que enviaría una solicitud HTTP (POST) al otro servicio cada vez que realice un cálculo, enviando en el cuerpo del mensaje el número, su factorial y la etiqueta de paridad. De esta forma, el segundo servicio se encargaría de guardar el historial sin que el microservicio principal tenga que preocuparse por la lógica de almacenamiento en esa base de datos externa.

La comunicación entre los dos servicios sería sencilla: el microservicio principal seguiría funcionando igual para responder a los usuarios, pero además, después de generar el resultado, haría una llamada al otro servicio usando su dirección o endpoint, algo como http://servicio-historial/api/calculos. Si por alguna razón el servicio del historial no está disponible, el microservicio deberia de guardar temporalmente la información y volver a intentar más tarde, para no perder los datos.

De esta forma, Tener a los 2 servicios trabajando en equipo pero de forma independiente: uno se enfoca en los cálculos y el otro en almacenar la información. Logrando una independencia y disponibilidad importante ademas de permitirnos utilizar ese microservicio de factorial desde cualquier otro microservicio.