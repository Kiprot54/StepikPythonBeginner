import turtle as t

from functions import get_color
from turtle_functions import run_turtle

def get_colors(n):
    # colors = ['cyan', 'black', 'red', 'yellow', 'green']
    colors = [get_color(f'° Введи цвет {i+1} кольца в формате HEX: ') for i in range(n)]
    colors.insert(0, colors.pop())
    return colors

@run_turtle
def circle(colors):

    positions = [
                 (118, -135),
                (-200, 0),
                 (9, 0),
                 (218, 0),
                 (-91, -135)]
    t.pensize(10)
    for i in range(5):
        t.color(colors[i])
        t.penup()
        t.goto(positions[i])
        t.pendown()
        t.circle(100)

colors = get_colors(5)
circle(colors)