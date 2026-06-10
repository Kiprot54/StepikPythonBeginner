import turtle as t
from lib.turtle_functions import right_polygon, run_turtle
from lib.functions import get_float

@run_turtle
def right_triangle_angle(side, rotate_angle):
    t.left(rotate_angle)
    right_polygon(3, side)

side = get_float('Введи длину стороны правильного треугольника: ')
angle = get_float('Введи угол поворота: ')

right_triangle_angle(side, angle)