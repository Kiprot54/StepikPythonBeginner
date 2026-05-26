from turtle_functions import rectangle, run_turtle
from functions import get_int

@run_turtle
def run_rectangle(width, height):
    rectangle(width, height)

width = get_int('Введи ширину прямоугольника: ')
height = get_int('Введи длину прямоугольника: ')

run_rectangle(width, height)