import turtle as t

def square(side):
    for i in range(4):
        t.forward(side)
        t.left(90)

def three_squares(side, angle):
    t.left((90 - 2*angle) / 2)
    for _ in range(3):
        square(side)
        t.left(angle)


three_squares(100, 450)
t.exitonclick()