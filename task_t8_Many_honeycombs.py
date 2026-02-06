import turtle as t

def hexagon(side):
    hexagon_angles = (6 - 2) * 180
    hexagon_angle = hexagon_angles / 6
    angle = 180 - hexagon_angle
    for i in range(6):
        t.forward(side)
        t.left(angle)

def honeycomb_row(n, side):
    hexagon_angles = (6 - 2) * 180
    hexagon_angle = hexagon_angles / 6
    angle = 180 - hexagon_angle

    for i in range(n):
        t.pendown()
        hexagon(side)
        if i != n - 1:
            if i % 2 == 0:
                t.penup()
                t.forward(side)
                t.left(angle)
                t.forward(side)
                t.right(angle)
                t.pendown()
            else:
                t.penup()
                t.forward(side)
                t.right(angle)
                t.forward(side)
                t.left(angle)
                t.pendown()

def step_down(side):
    hexagon_angles = (6 - 2) * 180
    hexagon_angle = hexagon_angles / 6
    angle = 180 - hexagon_angle

    t.forward(side)
    t.left(angle)
    t.forward(side)
    t.right(angle)

def step_up(side):
    hexagon_angles = (6 - 2) * 180
    hexagon_angle = hexagon_angles / 6
    angle = 180 - hexagon_angle

    t.forward(side)
    t.right(angle)
    t.forward(side)
    t.left(angle)


def honeycomb_row_left(n, side):
    for i in range(n):
        t.pendown()
        hexagon(side)
        if i != n - 1:
            if i % 2 == 0:
                if n % 2 != 0:
                    step_up(side)
                else:
                    step_down(side)
            else:
                if n % 2 == 0:
                    step_up(side)
                else:
                    step_down(side)

def honeycomb(n, m, side):
    hexagon_angles = (6 - 2) * 180
    hexagon_angle = hexagon_angles / 6
    angle = 180 - hexagon_angle

    for i in range(m//2):
        honeycomb_row(n, side)
        t.penup()
        t.forward(side)
        t.right(180)
        t.pendown()
        honeycomb_row_left(n, side)
        t.penup()
        t.forward(side)
        t.left(angle)
        t.forward(side)
        t.left(angle)
        t.forward(side)
        t.right(angle)
        t.forward(side)
        t.left(angle)
        t.forward(side)
        t.left(angle)
        t.pendown()

    if m % 2 == 1:
        honeycomb_row(n, side)

# def honeycomb(n, m, side):
#     hexagon_angles = (6 - 2) * 180
#     hexagon_angle = hexagon_angles / 6
#     angle = 180 - hexagon_angle
#
#     for i in range(m):
#         position = t.pos()
#         honeycomb_row(n, side)
#         t.penup()
#         t.goto(position[0], position[1])
#         t.right(hexagon_angle)
#         t.forward(side)
#         t.left(angle)
#         t.forward(side)
#         t.left(angle)
#         t.pendown()

t.speed(0)
t.penup()
t.goto(-200, 200)
honeycomb(8, 7, 50)
t.done()