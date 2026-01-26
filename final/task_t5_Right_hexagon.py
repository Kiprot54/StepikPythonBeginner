import turtle as t

def hexagon(side):
    hexagon_angles = (6 - 2) * 180
    hexagon_angle = hexagon_angles / 6
    angle = 180 - hexagon_angle
    for i in range(6):
        t.forward(side)
        t.left(angle)

t.hideturtle()
t.speed(0)
hexagon(100)
t.done()