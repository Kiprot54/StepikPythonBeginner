import turtle as t

from lib.functions import get_float, get_int
from lib.turtle_functions import run_turtle, right_polygon

@run_turtle
def run(n, side):
    right_polygon(n, side)

n = get_int('Введи количество углов: ')
side = get_float('Введи длину стороны многоугольника: ')
t.penup()
t.goto(0, -20)
t.pendown()
run(n, side)
