import turtle as t

from functions import get_int, get_float
from turtle_functions import run_turtle

@run_turtle
def lines(n, step):
    side = 10
    for i in range(n):
        t.forward(side)
        t.left(90)
        side += step
n = get_int('Введи количество узоров: ')
step = get_float('Введи на сколько узор будет увеличиваться: ')
lines(n, step)