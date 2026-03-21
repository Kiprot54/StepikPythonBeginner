import turtle as t

def line(side):
    t.forward(side)
    t.backward(side)

def lines(n, side):
    for i in range(n):
        line(side)
        t.left(360 / n)

lines(12, 100)
t.done()