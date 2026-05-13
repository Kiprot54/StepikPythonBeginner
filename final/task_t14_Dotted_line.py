import turtle as t

def dotline(n, size, step):
    t.penup()
    t.pensize(size/2)
    for i in range(n):
        t.dot()
        t.forward(size + step)

dotline(10, 30, 10)
t.done()