import turtle as t
from turtle_functions import run_turtle, right_polygon
from functions import get_int, get_float

def small_square(side):
    small_side = side / 2
    right_polygon(4, small_side)

def big_square(side):
    for i in range(4):
        small_square(side)
        t.left(90)

@run_turtle
def squares(n, side):
    for i in range(n):
        big_square(side)
        t.left(90 / n)

n = get_int('Введи количество больших квадратов: ')
side = get_float('Введи длину стороны квадрата: ')
squares(n, side)