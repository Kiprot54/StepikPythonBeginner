import turtle as t
import random as r
from lib.functions import get_int, get_float
from lib.turtle_functions import run_turtle, go_to


def star(k, size):
    angle = 180 - (180 / k)
    for i in range(k):
        t.forward(size)
        t.left(angle)

@run_turtle
def draw_star(m, size):
    for i in range(1, m + 1):
        n = r.choice([j for j in range(5, 22) if j % 2 != 0])


        # lst = []
        # for j in range(5, 22):
        #     if n % 2 != 0:
        #         lst.append(j)

        star(n, size)

        t.penup()
        t.forward(size + 25)
        t.pendown()

def main():
    m = get_int('Введи количество звёзд: ')
    size = get_float('Введи размер звёздочки: ')
    go_to(-800, 0)
    draw_star(m, size)

main()