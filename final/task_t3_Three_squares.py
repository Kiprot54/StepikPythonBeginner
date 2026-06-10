import turtle as t
from lib.turtle_functions import right_polygon, run_turtle
from lib.functions import get_float


@run_turtle
def three_squares(side, angle):
    t.left((90 - 2*angle) / 2)
    for _ in range(3):
        right_polygon(4, side)
        t.left(angle)

side = get_float('Введи длину стороны квадрата: ')
angle = get_float('Введи угол поворота: ')

three_squares(side, angle)