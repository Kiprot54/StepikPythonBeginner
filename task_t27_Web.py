import turtle as t

from lib.functions import get_int
from lib.turtle_functions import line, run_turtle


@run_turtle
def web(n):
    side = 100
    t.shape('turtle')
    for i in range(n):
        t.right(360 / n)
        line(side, True)

n = get_int('Введи количество лапок: ')
web(n)