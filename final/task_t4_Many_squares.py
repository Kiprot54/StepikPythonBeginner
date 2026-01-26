import turtle as t

def small_square(side):
    small_side = side / 2
    for i in range(4):
        t.forward(small_side)
        t.left(90)

def big_square(side):
    for i in range(4):
        small_square(side)
        t.left(90)

def squares(n, side):
    for i in range(n):
        big_square(side)
        t.left(90 / n)


t.speed(0)
t.hideturtle()
squares(100, 300)
t.exitonclick()