from random import randrange
from turtle import *

from freegames import vector


ball = vector(-200, -200) 
speed = vector(0, 0)
targets = []             


def tap(x, y):
    """
    Responde a un clic en la pantalla.
    
    Parámetros:
    x (float): Coordenada x del clic.
    y (float): Coordenada y del clic.
    
    Si la bala está fuera de la pantalla (no se ha disparado), se reposiciona
    en la posición inicial y se le da una velocidad basada en la posición
    del clic.
    """
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 15 
        speed.y = (y + 200) / 15 


def inside(xy):
    """
    Verifica si un vector está dentro de los límites de la pantalla.
    
    Parámetros:
    xy (vector): Vector que contiene las coordenadas (x, y) a verificar.
    
    Retorna:
    bool: True si el vector está dentro de la pantalla, False si no lo está.
    """
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    """
    Dibuja la bala y los objetivos en la pantalla.
    
    Limpia la pantalla, luego dibuja cada objetivo en azul y la bala en rojo si
    está dentro de los límites de la pantalla.
    """
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue') 

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')  

    update()  


def move():
    """
    Mueve la bala y los objetivos en la pantalla.
    
    - Crea un nuevo objetivo en una posición aleatoria en el eje y en el borde derecho de la pantalla.
    - Mueve todos los objetivos hacia la izquierda.
    - Aplica gravedad a la bala y la mueve si está dentro de la pantalla.
    - Detecta colisiones entre la bala y los objetivos y elimina los objetivos alcanzados.
    - Reposiciona los objetivos que salen del lado izquierdo para que reaparezcan a la derecha.
    """
    if randrange(40) == 0: 
        y = randrange(-150, 150)
        target = vector(200, y) 
        targets.append(target)

    for target in targets:
        target.x -= 2 

    if inside(ball):
        speed.y -= 0.35  
        ball.move(speed)  


    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        # Si la bala no golpea al objetivo, lo mantiene en la lista
        if abs(target - ball) > 13:
            targets.append(target)

    draw() 

    # Reposiciona los objetivos que salen de la pantalla
    for target in targets:
        if not inside(target):
            target.x = 200  
            target.y = randrange(-150, 150)

    ontimer(move, 50)  


# Configuración inicial del juego
setup(420, 420, 370, 0) 
hideturtle() 
up()  
tracer(False)
onscreenclick(tap) 
move()
done()  
