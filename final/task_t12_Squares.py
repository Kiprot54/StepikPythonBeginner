import turtle as t

from functions import get_int, get_float
from turtle_functions import run_turtle, right_polygon

def square(side):
    for i in range(4):
        t.left(90)
        t.forward(side)

@run_turtle
def squares(n, step, start):
    side = start
    for i in range(n):
        square(side)
        side += step

n = get_int('Введи количество квадратов: ')
step = get_int('Введи на сколько будет расширяться один квадрат: ')
side = get_float('Введи длину стороны квадрата: ')
squares(n, step, side)