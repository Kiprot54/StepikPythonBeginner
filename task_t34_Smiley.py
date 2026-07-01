import turtle as t

from lib.turtle_functions import run_turtle, go_to


@run_turtle
def smiley():
    t.fillcolor('yellow')
    t.begin_fill()
    t.circle(100)
    t.end_fill()

    go_to(-50, 130)
    t.fillcolor('blue')
    t.begin_fill()
    t.circle(15)
    t.end_fill()

    go_to(50, 130)
    t.begin_fill()
    t.circle(15)
    t.end_fill()

    go_to(0, 115)
    t.pensize(10)
    t.right(90)
    t.forward(30)

    go_to(-50, 60)
    t.color('red')
    t.circle(50, 180)


smiley()