import turtle as t

def square(side):
    for i in range(4):
        t.left(90)
        t.forward(side)

def squares(n, step, start):
    side = start
    for i in range(n):
        square(side)
        side += step

t.speed(0)
squares(30, 7, 20)
t.exitonclick()