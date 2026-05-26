import turtle as t

def run_turtle(func):
    def wrapper(*args, **kwargs):
        t.speed(0)
        func(*args, **kwargs)
        t.done()
    return wrapper

def rectangle(width, height):
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

def right_triangle(side):
    for _ in range(3):
        t.forward(side)
        t.left(120)