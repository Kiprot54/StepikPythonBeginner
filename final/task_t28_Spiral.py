import turtle as t
from math import cos, sin, pi

from lib.functions import get_float
from lib.turtle_functions import run_turtle

@run_turtle
def spiral(n: float, b: float):
    angle = 0
    l = 2 * n * pi
    while angle < l:
        r = b * angle
        x = r * cos(angle)
        y = r * sin(angle)
        second_angle = t.towards(x, y)
        t.setheading(second_angle)
        t.goto(x, y)
        angle += 0.1

n = get_float('Введи количество витков спирали: ')
b = get_float('Введи шаг спираль: ')
spiral(n, b)