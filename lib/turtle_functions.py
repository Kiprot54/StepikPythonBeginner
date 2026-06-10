import turtle as t

def run_turtle(func):
    def wrapper(*args, **kwargs):
        t.speed(0)
        func(*args, **kwargs)
        t.hideturtle()
        t.done()

    return wrapper

def rectangle(width: float | int, height: float | int) -> None:
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

def right_polygon(n: int, side: float | int) -> None:
    angle = 360 / n
    for _ in range(n):
        t.forward(side)
        t.left(angle)

def rhomb(side: float | int, angle: float | int) -> None:
    for _ in range(2):
        t.forward(side)
        t.left(angle)
        t.forward(side)
        t.left(180 - angle)

def line(side: float | int, is_stamp: bool=False) -> None:
    t.forward(side)
    if is_stamp:
        t.stamp()
    t.backward(side)

def get_shape(target: str) -> str | None:
    shape_list = ['turtle', 'arrow', 'triangle']
    while True:
        try:
            shape = input(f'Введи рисунок {target} (arrow, turtle, triangle): ')
            if shape not in shape_list:
                raise ValueError('Shape не из списка')
            return shape
        except ValueError:
            print('Нужно ввести рисунок из списка')
        except IndexError:
            print('Пустая строка')

def go_to(x: float | int, y: float | int) -> None:
    t.penup()
    t.goto(x, y)
    t.pendown()