import turtle as t

from functions import get_int, get_float
from turtle_functions import run_turtle, line

@run_turtle
def lines(n, side):
    for i in range(n):
        line(side)
        t.left(360 / n)

n = get_int('Введи количество лучей звезды: ')
side = get_float('Введи длину луча звезды: ')
lines(n, side)