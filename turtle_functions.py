import turtle as t

def run_turtle(func):
    def wrapper(*args, **kwargs):
        t.speed(0)
        func(*args, **kwargs)
        t.hideturtle()
        t.done()

    return wrapper

def rectangle(width, height):
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

def right_polygon(n, side):
    angle = 360 / n
    for _ in range(n):
        t.forward(side)
        t.left(angle)

def rhomb(side, angle):
    for _ in range(2):
        t.forward(side)
        t.left(angle)
        t.forward(side)
        t.left(180 - angle)

def line(side, is_stamp=False):
    t.forward(side)
    if is_stamp:
        t.stamp()
    t.backward(side)