import turtle as t

from lib.functions import get_int, get_float
from lib.turtle_functions import run_turtle, line


@run_turtle
def web(n, size, side):
    t.pensize(size)
    t.dot()
    t.shape('triangle')
    for i in range(n):
        line(side, True)
        t.left(360 / n)
n = get_int('Введи количество лучей паутины: ')
size = get_float('Введи толщину луча паутины: ')
side = get_float('Введи длину луча паутины: ')
web(n, size, side)