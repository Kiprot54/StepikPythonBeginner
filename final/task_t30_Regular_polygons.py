import turtle as t

from lib.functions import get_int
from lib.turtle_functions import run_turtle, go_to, right_polygon
from math import sin, pi


@run_turtle
def regular_polygon(n):
    r = 0
    step = 20

    for i in range(3, n + 3):
        r += step
        go_to(r, 0)

        angles = (i - 2) * 180
        angle = angles / i
        rotate_angle = 180 - angle / 2
        t.left(rotate_angle)

        side = 2 * r * sin(pi / i)
        right_polygon(i, side)

        t.right(rotate_angle)

n = get_int('Введи количество многоугольников: ')
regular_polygon(n)