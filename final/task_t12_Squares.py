import turtle as t

from functions import get_int, get_float
from turtle_functions import run_turtle, right_polygon

@run_turtle
def squares(n, step, start):
    side = start
    t.left(90)
    for i in range(n):
        right_polygon(4, side)
        side += step

n = get_int('Введи количество квадратов: ')
step = get_float('Введи расстояние между квадратами: ')
side = get_float('Введи длину стороны квадрата: ')
squares(n, step, side)