import turtle as t
from random import uniform as r
from lib.functions import get_color, get_int
from lib.turtle_functions import run_turtle, line, go_to


def get_colors(n):
    # colors = ['cyan', 'black', 'red', 'yellow', 'green']
    colors = [get_color(f'° Введи цвет {i+1} кольца в формате HEX: ') for i in range(n)]
    return colors

def snowflake_line(sz):
    for i in range(3):
        t.forward(sz)
        t.left(45)
        line(sz)
        t.right(90)
        line(sz)
        t.left(45)
    t.forward(sz)




def snowflake(size):
    t.dot()

    for i in range(8):
        snowflake_line(size)
        t.penup()
        t.backward(size * 4)
        t.pendown()
        t.left(45)

@run_turtle
def snowflakes(n, colors):
    go_to(-400, -400)
    sizes = []
    for i in range(n):
        sizes.append(r(20, 100))
    coords = []
    for i in range(n):
        coords.append((r(0, 800), r(0, 800)))

    for i in range(n):
        t.color(colors[i])
        size = sizes[i] / 4
        go_to(coords[i][0] - 400, coords[i][1] - 400)
        # print(coords[i])
        # print(f'Size: {size}')
        snowflake(size)

def main():
    n = get_int('Введи количество снежинок: ')
    background = get_color('Введи цвет фона в формате HEX: ')
    colors = get_colors(n)
    t.bgcolor(background)
    snowflakes(n, colors)

main()