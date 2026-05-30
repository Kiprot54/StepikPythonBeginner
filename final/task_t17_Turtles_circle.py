import turtle as t

from functions import get_int, get_float
from turtle_functions import run_turtle, line

@run_turtle
def turtle_circle(n, side):
    t.penup()
    t.shape('turtle')
    t.stamp()
    for i in range(n):
        line(side, True)
        t.left(360 / n)

n = get_int('Введи количество черепашек: ')
side = get_float('Введи расстояние от центра: ')
turtle_circle(n, side)