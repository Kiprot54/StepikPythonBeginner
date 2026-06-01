import turtle as t

from functions import get_color, get_float, get_int
from turtle_functions import run_turtle


def get_colors(n):
    # colors = ['red', 'blue', 'yellow', 'green', 'purple', 'orange']
    colors = [get_color(f'° Введи {i+1} цвет в формате HEX: ') for i in range(n)]
    return colors

@run_turtle
def colored_spiral(size, colors):
    side = 1
    pensize = 1
    t.pensize(pensize)

    while side <= size:
        for el in colors:
            t.color(el)
            t.forward(side)
            t.left(45)
            side += 2
            if side == size + 1:
                break
            pensize += 0.1
            t.pensize(pensize)


n = get_int('Введи количество цветов: ')
colors = get_colors(n)
size = get_int('Введи максимальный размер элемента спирали: ')
colored_spiral(size, colors)