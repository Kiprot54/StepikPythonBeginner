import turtle as t

from lib.functions import get_float
from lib.turtle_functions import run_turtle


@run_turtle
def draw_house(size):
    square = t.Turtle()
    square.fillcolor("cyan")
    square.begin_fill()
    for i in range(4):
        square.forward(size)
        square.right(90)
    square.end_fill()
    square.hideturtle()


    triangle = t.Turtle()
    triangle.fillcolor("brown")
    triangle.begin_fill()
    triangle.goto(size + 20, 0)
    triangle.goto(size / 2, size / 2 + 20)
    triangle.goto(size - size -20, 0)
    triangle.end_fill()

    triangle.hideturtle()



def main():
    size = get_float('Введи размер домика: ')
    t.hideturtle()
    draw_house(size)

main()