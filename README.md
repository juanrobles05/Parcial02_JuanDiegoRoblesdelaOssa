## ANÁLISIS: Modificación del Diseño para Comunicación con Servicio de Historial

### Pregunta
*"¿Cómo modificaría su diseño si este microservicio tuviera que comunicarse con otro servicio que almacena el historial de cálculos en una base de datos externa?"*

### Respuesta
Modificaria el microservicio para que enviaría una solicitud HTTP (POST) al otro servicio cada vez que realice un cálculo, enviando en el cuerpo del mensaje el número, su factorial y la etiqueta de paridad. De esta forma, el segundo servicio se encargaría de guardar el historial sin que el microservicio principal tenga que preocuparse por la lógica de almacenamiento.