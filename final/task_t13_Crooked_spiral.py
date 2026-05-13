import turtle as t

def lines(n, step):
    side = 10
    for i in range(n):
        t.forward(side)
        t.left(90)
        side += step

t.speed(0)
t.left(90)
lines(150, 5)
t.done()