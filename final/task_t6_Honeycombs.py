import turtle as t

from lib.turtle_functions import run_turtle, right_polygon
from lib.functions import get_float

@run_turtle
def honeycombs(side):
    hexagon_angles = (6 - 2) * 180
    hexagon_angle = hexagon_angles / 6
    angle = 180 - hexagon_angle

    for i in range(6):
        right_polygon(6, side)
        t.penup()
        t.forward(side)
        t.right(angle)
        t.pendown()

side = get_float('Введи длину стороны правильного шестиугольника: ')
honeycombs(side)