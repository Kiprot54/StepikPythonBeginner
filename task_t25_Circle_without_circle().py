import turtle as t

from functions import get_int
from turtle_functions import run_turtle


@run_turtle
def circle_without_circle(n):
    for i in range(n):
        t.forward(10)
        t.left(360/n)
circle_without_circle(8)