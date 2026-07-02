import turtle as t

from lib.functions import get_color, get_float
from lib.turtle_functions import run_turtle, go_to

def circle(r, isAngle = False):
    t.circle(r, 180 if isAngle else 360)

def get_colors(text):
    colors = get_color(f'° Введи цвет {text} для смайлика в формате HEX: ')
    return colors

@run_turtle
def smiley(size, color_head, color_eyes, color_nose, color_mouth):

    # голова
    t.fillcolor(color_head)
    t.begin_fill()
    circle(size)
    t.end_fill()

    # глаза
    go_to(-size * 0.5, size * 1.3)
    t.fillcolor(color_eyes)
    t.begin_fill()
    circle(size * 0.15)
    t.end_fill()

    go_to(size * 0.5, size * 1.3)
    t.begin_fill()
    circle(size * 0.15)
    t.end_fill()

    # нос
    go_to(0, size * 1.15)
    t.color(color_nose)
    t.pensize(size * 0.1)
    t.right(90)
    t.forward(size * 0.3)

    # рот
    go_to(-size * 0.5, size * 0.6)
    t.color(color_mouth)
    circle(size * 0.5, True)

def main():
    size = get_float('Введите размер смайлика: ')
    head = get_colors('головы')
    eyes = get_colors('глаз')
    nose = get_colors('носа')
    mouth = get_colors('рты')

    smiley(size, head, eyes, nose, mouth)

main()