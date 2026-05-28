from functions import get_float
from turtle_functions import  run_turtle, rhomb

@run_turtle
def run(side, angle):
    rhomb(side, angle)

side = get_float('Введи длину стороны ромба: ')
angle = get_float('Введи один из углов ромба: ')
run(side, angle)