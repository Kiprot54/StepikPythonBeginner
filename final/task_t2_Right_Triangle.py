import turtle as t
from turtle_functions import right_triangle, run_turtle
from functions import get_int

@run_turtle
def right_triangle_angle(side, rotate_angle):
    t.left(rotate_angle)
    right_triangle(side)

side = get_int('Введи длину стороны правильного треугольника: ')
angle = get_int('Введи угол поворота: ')

right_triangle_angle(side, angle)