import turtle as t

def line(side):
    t.forward(side)
    t.shape('triangle')
    t.stamp()
    t.backward(side)

def web(n, size, side):
    t.pensize(size)
    t.dot()
    for i in range(n):
        line(side)
        t.left(360 / n)


web(8, 20, 100)
t.done()