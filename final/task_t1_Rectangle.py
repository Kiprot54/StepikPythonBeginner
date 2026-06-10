from lib.turtle_functions import rectangle, run_turtle
from lib.functions import get_float


@run_turtle
def run_rectangle(width, height):
    rectangle(width, height)

width = get_float('Введи ширину прямоугольника: ')
height = get_float('Введи длину прямоугольника: ')

run_rectangle(width, height)