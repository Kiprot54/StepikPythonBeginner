import turtle as t


from lib.functions import get_float
from lib.turtle_functions import run_turtle, go_to


@run_turtle
def traffic_light(height):
    width = height * 0.35
    height_space = height * 0.077
    radius = height * 0.1153

    t.fillcolor('#000')
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()
    colors = ['limegreen', 'yellow', 'red']

    for i in range(3):
        go_to(width / 2, i * 2 * radius + (i + 1) * height_space)
        circle_fill(colors[i], radius)


def circle_fill(color, size):
    t.fillcolor(color)
    t.begin_fill()
    t.circle(size)
    t.end_fill()

def main():
    height = get_float('Введи высоту светофора: ')
    traffic_light(height)

main()