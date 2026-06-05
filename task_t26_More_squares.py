import turtle as t

from functions import get_int
from turtle_functions import right_polygon, run_turtle, go_to


@run_turtle
def more_squares(n):
    x = 0
    y = 0
    step = 10
    side = 10
    for i in range(n):
        go_to(x, y)
        right_polygon(4, side)
        x -= step
        y -= step
        side += step * 2

n = get_int('Введи количество квадратов: ')
more_squares(n)