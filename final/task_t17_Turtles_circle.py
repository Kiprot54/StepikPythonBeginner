import turtle as t

def turtle_line(side):
    t.penup()
    t.forward(side)
    t.stamp()
    t.backward(side)


def turtle_circle(n, side):
    t.shape('turtle')
    t.stamp()
    for i in range(n):
        turtle_line(side)
        t.left(360 / n)

t.speed(0)
turtle_circle(12, 200)
t.done()