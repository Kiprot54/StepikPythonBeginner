import turtle as t

from lib.functions import get_int
from lib.turtle_functions import run_turtle

def circles_up_down(r):

    t.circle(r)
    t.circle(-r)

@run_turtle
def butterfly(n):
    r = 25
    t.left(90)
    for i in range(n):
        circles_up_down(r)
        r += 5

def main():
    while True:
        n = get_int('Введи количество окружностей: ')
        if n % 2 != 0:
            print('Надо ввести чётное число')
        else:
            break
    butterfly(n // 2)

main()