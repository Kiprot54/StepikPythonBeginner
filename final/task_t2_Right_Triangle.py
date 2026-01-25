import turtle as t

def right_triangle(side, rotate_angle):
    angle = 60
    t.left(rotate_angle)
    for _ in range(3):
        t.forward(side)
        t.left(180 - angle)

right_triangle(100, 30)
t.exitonclick()