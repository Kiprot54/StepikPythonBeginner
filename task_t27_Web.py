import turtle as t

from functions import get_int
from turtle_functions import line, run_turtle


@run_turtle
def web(n):
    side = 100
    for i in range(n):
        t.right(360 / n)
        line(side, True)

n = get_int('Введи количество лапках: ')
web(n)