import turtle as t

def right_polygon(n, side):
    angles_polygon = (n - 2) * 180
    angle_polygon = angles_polygon / n
    angle = 180 - angle_polygon
    for i in range(n):
        t.forward(side)
        t.left(angle)

t.penup()
t.goto(0,-200)
t.pendown()
right_polygon(30, 30)
t.speed(0)
t.done()
