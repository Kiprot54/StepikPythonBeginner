import turtle as t
from turtle_functions import rectangle

def three_squares(side, angle):
    t.left((90 - 2*angle) / 2)
    for _ in range(3):
        rectangle(side, side)
        t.left(angle)


three_squares(100, 450)
t.exitonclick()