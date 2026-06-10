import turtle as t

from lib.functions import get_int, get_float
from lib.turtle_functions import run_turtle


@run_turtle
def dotline(n, size, step):
    t.penup()
    t.pensize(size/2)
    for i in range(n):
        t.dot()
        t.forward(size + step)


n = get_int("Введи количество точек в линии: ")
size = get_float("Введи размер точек: ")
step = get_float("Введи расстояние между точками: ")
t.penup()
t.goto(-200, 0)
t.pendown()
dotline(n, size, step)