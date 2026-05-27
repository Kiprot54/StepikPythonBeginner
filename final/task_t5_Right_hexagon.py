import turtle as t

from functions import get_float
from turtle_functions import run_turtle, right_polygon

@run_turtle
def hexagon(side):
    right_polygon(6, side)

side = get_float('Введи длину стороны правильного шестиугольника: ')
hexagon(side)