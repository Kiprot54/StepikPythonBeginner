import turtle as t
from lib.functions import get_float, get_int
from lib.turtle_functions import  run_turtle, rhomb

@run_turtle
def snowflake(n, side, angle):
    t.left(angle / 2)
    for _ in range(n):
        rhomb(side, angle)
        t.right(360 / n)

n = get_int('Введи количество ромбов: ')
side = get_float('Введи длину стороны ромба: ')
angle = get_float('Введи один из углов ромба: ')
snowflake(n, side, angle)