# Fundamentos de los Sistemas Inteligentes
## Prácticas de Fundamentos de los Sistemas Inteligentes
### Heurística

Esta práctica tiene como objetivo el desarrollo de una heurística para
un juego de conecta 4.

Durante el transcurso de la práctica hemos ideado varias formas para
evaluar el tablero y hemos implementado finalmente una heurística que
calcula la calidad del tablero para el jugador problema y para el adversario.

Si no hay ningún posible cuatro en raya, se devuelve la resta  de estas 
heurísticas, en caso contrario se devuelve infinito o menos infinito 
respectivamente.

Para el cálculo de la heurística se coge cada movimiento legal del tablero
(la posición de cada columna donde se puede colocar una ficha), y se 
calcula la puntuación de cada línea que se da en él a partir de esa posición
(verticales, horizontales y diagonales).

Para cada línea se baja una posición y se recorre el tablero con un 
desplazamiento dado. Para cada posición se comprueba si es una ficha 
del jugador que se está tratando, y se suma una cantidad, si es una posición
vacía se suma una cantidad menor a la puntuación, y si es una ficha contraria 
se acaba el recorrido. Al final si se tienen cuatro fichas propias seguidas
se devuelve una puntuación infinita, sino se suma una cierta cantidad en
base a las fichas seguidas y se devuelve la puntuación.

### Otros detalles implementados

- El juego ahora permite seleccionar una dificultad que cambia la profundidad
a la que se explora en el algoritmo MIN MAX.

- Se puede seleccionar el jugador que empieza a jugar, la máquina o la persona,
el primer jugador siempre va a tener las X y el segundo las O.

- Se ha implementado el memoize para acelerar el cálculo de la heurística
a partir de un estado específico


:white_circle: :white_circle: :white_circle: :white_circle: :white_circle: :white_circle: :white_circle:

:white_circle: :white_circle: :white_circle: :white_circle: :white_circle: :white_circle: :white_circle:

:white_circle: :white_circle: :white_circle: :white_circle: :red_circle: :white_circle: :white_circle:

:white_circle: :white_circle: :white_circle: :red_circle: :large_blue_circle: :white_circle: :white_circle:

:white_circle: :white_circle: :red_circle: :large_blue_circle: :large_blue_circle: :white_circle: :white_circle:

:white_circle: :red_circle: :large_blue_circle: :red_circle: :large_blue_circle: :white_circle: :white_circle:
