import turtle as t
from lib.turtle_functions import run_turtle, go_to


def arc(r):
    t.circle(-r, 180)

@run_turtle
def spring(n, r):
    t.left(90)
    go_to(-200, 0)
    for i in range(n):
        arc(r)
        if i != n - 1:
            arc(r / 6)


spring(5, 50)