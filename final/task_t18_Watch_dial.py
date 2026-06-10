import turtle as t

from lib.functions import get_float, get_color, get_time
from lib.turtle_functions import run_turtle, get_shape


def turtle_line(side):
    line = 20
    space = 15
    t.penup()
    t.forward(side - line - space)
    t.pendown()
    t.forward(line)
    t.penup()
    t.forward(space)
    t.stamp()
    t.backward(side)

def run():
    @run_turtle
    def turtle_circle(side, watch, arrow, time):
        t.shape(arrow)
        t.left(90)
        t.right(360 / 12 * time)
        t.stamp()
        t.left(360 / 12 * time)
        t.shape(watch)
        for i in range(12):
            turtle_line(side)
            t.left(30)
    watch = get_shape('циферблата')
    arrow = get_shape('стрелки')
    side = get_float('Введи расстояние от центра: ')
    bg_color = get_color('Введи цвет фона: ')
    time = get_time(1, 12)
    t.Screen().bgcolor(bg_color)
    turtle_circle(side, watch, arrow, time)

run()