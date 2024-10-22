# Evidencia de proyecto

### Instalación necesaria:
La instalación de Free Python Games es con pip:
```
$ python3 -m pip install freegames
```
Free Python Games soporta una interfaz de línea de comandos (CLI). La ayuda para la CLI está disponible usando:
```
$ python3 -m freegames --help
```
La CLI soporta tres comandos: list, copy y show. Para obtener una lista de todos los juegos, ejecuta:
```
$ python3 -m freegames list
```
Cualquiera de los juegos listados se puede jugar ejecutando el módulo de Python desde la línea de comandos. Para hacer referencia al módulo de Python, combina “freegames” con el nombre del juego. Por ejemplo, para jugar al juego “snake”, ejecuta:
```
$ python3 -m freegames.snake
```
Los juegos se pueden modificar copiando su código fuente. El comando copy creará un archivo Python en tu directorio local que podrás editar. Por ejemplo, para copiar y jugar al juego “snake”, ejecuta:
```
$ python3 -m freegames copy snake
$ python3 snake.py
```
### Descripción de los Juegos
1. **cannon.py** <br/>
En este juego, el jugador dispara balones desde un cañón para golpear objetivos en movimiento. Las modificaciones incluyen aumentar la velocidad del balón del cañón y asegurar que tanto los objetivos como los balones reaparezcan después de salir de la pantalla, haciendo el juego interminable.
2. **memory.py**<br/>
Un clásico juego de memoria en el que los jugadores deben emparejar pares de fichas ocultas. Las modificaciones incluyen centrar el texto en las fichas de un solo dígito, contar el número de toques (taps) y detectar cuándo todas las fichas se han destapado.
3. **pacman.py**<br/>
Una versión modificada del clásico juego de Pac-Man en la que se han añadido diferentes tableros aleatorios y se ha ajustado la velocidad de los fantasmas para hacer el juego más desafiante.
4. **paint.py**<br/>
Un programa de dibujo simple que permite a los usuarios dibujar diferentes formas y cambiar de color. Se ha mejorado la documentación para facilitar su uso.
5. **snake.py**<br/>
El clásico juego de la serpiente en el que la serpiente crece cada vez que come comida. Se ha añadido un cambio de color aleatorio para la serpiente y la comida en cada ejecución del juego, excepto el color rojo para evitar confusiones.
