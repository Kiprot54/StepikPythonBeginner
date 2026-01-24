import turtle as t

def rectangle(width, height):
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

rectangle(250, 5)
t.exitonclick()