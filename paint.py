# Importación de módulos necesarios
from turtle import *   # Módulo turtle para dibujo gráfico
from freegames import vector  # Importación de vector para manejo de coordenadas

def line(start, end, line_width=1):
    """
    Dibuja una línea desde el punto de inicio hasta el punto final.
    
    Parámetros:
    start (vector): Coordenadas del punto de inicio.
    end (vector): Coordenadas del punto final.
    line_width (int): Ancho de la línea (opcional, valor por defecto = 1).
    """
    width(line_width)
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end, line_width=1):
    """
    Dibuja un cuadrado desde el punto de inicio hasta el punto final.
    
    Parámetros:
    start (vector): Coordenadas del punto de inicio.
    end (vector): Coordenadas del punto final.
    line_width (int): Ancho de la línea (opcional, valor por defecto = 1).
    """
    width(line_width)
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def draw_circle(start, end, line_width=1):
    """
    Dibuja un círculo desde el punto de inicio hasta el punto final.
    
    Parámetros:
    start (vector): Coordenadas del punto de inicio.
    end (vector): Coordenadas del punto final (determina el radio).
    line_width (int): Ancho de la línea (opcional, valor por defecto = 1).
    """
    width(line_width)
    up()
    goto(start.x, start.y - ((end.x - start.x)**2 + (end.y - start.y)**2)**0.5)
    down()
    begin_fill()

    radius = ((end.x - start.x)**2 + (end.y - start.y)**2)**0.5
    circle(radius)

    end_fill()

def rectangle(start, end, line_width=1):
    """
    Dibuja un rectángulo desde el punto de inicio hasta el punto final.
    
    Parámetros:
    start (vector): Coordenadas del punto de inicio.
    end (vector): Coordenadas del punto final.
    line_width (int): Ancho de la línea (opcional, valor por defecto = 1).
    """
    width(line_width)
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2):
        forward(end.x - start.x)
        left(90)
        forward(end.y - start.y)
        left(90)

    end_fill()

def triangle(start, end, line_width=1):
    """
    Dibuja un triángulo desde el punto de inicio hasta el punto final.
    
    Parámetros:
    start (vector): Coordenadas del punto de inicio.
    end (vector): Coordenadas del punto final.
    line_width (int): Ancho de la línea (opcional, valor por defecto = 1).
    """
    width(line_width)
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    goto(end.x, start.y)
    goto((start.x + end.x) / 2, end.y)
    goto(start.x, start.y)

    end_fill()

def tap(x, y):
    """
    Almacena el punto de inicio o dibuja la forma.
    
    Parámetros:
    x (float): Coordenada x del clic del ratón.
    y (float): Coordenada y del clic del ratón.
    """
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)  # Llama a la función para dibujar la forma
        state['start'] = None

def store(key, value):
    """
    Almacena un valor en el estado actual.
    
    Parámetros:
    key (str): Clave que identifica el valor a almacenar.
    value (any): Valor a almacenar.
    """
    state[key] = value

# Estado inicial del programa
state = {'start': None, 'shape': line}

# Configuración de la ventana de dibujo
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()

# Configuración de teclas para deshacer y cambiar colores
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')

# Configuración de teclas para seleccionar diferentes formas
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', draw_circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')

# Finaliza la configuración y espera la interacción del usuario
done()

# board_templates = [
#     [
#         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#         0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
#         0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
#         0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
#         0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
#         0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
#         0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
#         0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
#         0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
#         0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
#         0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
#         0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
#         0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
#         0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
#         0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
#         0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
#         0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
#         0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
#         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#     ],
#         [
#         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#         0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0,
#         0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
#         0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
#         0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0,
#         0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0,
#         0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
#         0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
#         0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
#         0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
#         0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
#         0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
#         0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
#         0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
#         0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0,
#         0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
#         0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
#         0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
#         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#     ],
#     # Añade más tableros aquí con diferentes configuraciones
# ]