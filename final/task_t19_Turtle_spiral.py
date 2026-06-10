import turtle as t

from lib.turtle_functions import run_turtle, get_shape
from lib.functions import get_color, get_int
def run():
    arrow = get_shape('стрелки')
    bg_color = get_color('Введи цвет фона: ')
    count = get_int('Введи количество рисунков: ')

    t.penup()
    t.Screen().bgcolor(bg_color)
    spiral(count, arrow)

@run_turtle
def spiral(count, arrow):
    t.shape(arrow)
    distance = 5
    for i in range(count):
        t.stamp()
        t.forward(distance)
        t.right(25)
        distance += 2
run()