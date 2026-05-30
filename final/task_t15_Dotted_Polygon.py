import turtle as t

from functions import get_int, get_float
from turtle_functions import run_turtle


@run_turtle
def draw_polygon(n, side, dot_size):
    angle_polygon = 180 * (n - 2)
    angle = angle_polygon / n
    for i in range(n):
        t.pensize(dot_size/2)
        t.dot()
        t.pensize(1)
        t.forward(side)
        t.left(180 - angle)


n = get_int("Введи количество сторон многоугольника: ")
side = get_float("Введи длину стороны многоугольника: ")
dot_size = get_float("Введи размер точки: ")
draw_polygon(n, side, dot_size)