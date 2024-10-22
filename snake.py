from random import randrange, choice
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    """
    Cambia la dirección de la serpiente.
    
    Parámetros:
    x (int): Desplazamiento en el eje x.
    y (int): Desplazamiento en el eje y.
    """
    aim.x = x
    aim.y = y

def inside(head):
    """
    Verifica si la cabeza de la serpiente está dentro de los límites.

    Parámetros:
    head (vector): La posición de la cabeza de la serpiente.

    Retorna:
    bool: True si está dentro de los límites, False si no lo está.
    """
    return -200 < head.x < 190 and -200 < head.y < 190

def move_food():
    """
    Mueve la comida un paso aleatorio en cualquier dirección, asegurando
    que permanezca dentro de los límites de la ventana.
    """
    options = [vector(10, 0), vector(-10, 0), vector(0, 10), vector(0, -10)]
    move = choice(options)
    new_position = food + move
    
    if inside(new_position):
        food.move(move)

def draw_border():
    """
    Dibuja un borde alrededor del área de juego.
    """
    penup()
    goto(-200, -200)
    pendown()
    pencolor('blue')
    pensize(3)
    for _ in range(4):
        forward(400)
        left(90)
    penup()
    goto(0, 0)
    pendown()

def move():
    """
    Mueve la serpiente un segmento hacia adelante.
    """
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()
    draw_border()
    move_food()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
draw_border()
move()
done()
