import turtle as t

from lib.functions import get_int
from lib.turtle_functions import run_turtle

def circles_up_down(r):

    t.circle(r)
    t.circle(-r)

@run_turtle
def flower(n):
    r = 50
    t.pensize(2)
    for i in range(n):
        circles_up_down(r)
        t.left(180 / n)


def main():
    while True:
        n = get_int('Введи количество окружностей: ')
        if n % 2 != 0:
            print('Надо ввести чётное число')
        else:
            break
    flower(n // 2)

main()