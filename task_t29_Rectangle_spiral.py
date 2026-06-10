import turtle as t

from lib.functions import get_int, get_float
from lib.turtle_functions import run_turtle


@run_turtle
def rectangle_spiral(n: int, step: float) -> None:
    side = step
    for i in range(n):
        t.forward(side)
        t.left(90)
        side += step

n = get_int('Введи количество элементов спирали: ')
step = get_float('Введи расстояние между элементами спирали: ')
rectangle_spiral(n, step)