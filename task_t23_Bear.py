import turtle as t

from lib.functions import get_float
from lib.turtle_functions import run_turtle, go_to

@run_turtle
def bear(r):
    k = r / 114
    offset_y = -190 * k
    if r < 0:
        offset_y = abs(offset_y)

    go_to(0, offset_y)
    if abs(r) < 50:
        t.pensize(1)
    else:
        t.pensize(3)
    t.circle(r)

    go_to(0, offset_y + 40 * k)

    t.left(90)
    t.forward(130 * k)
    t.right(90)
    t.circle(18 * k)

    go_to(0, offset_y)

    t.circle(190 * k)

    go_to(-100 * k,offset_y + 201 * k)

    t.begin_fill()
    t.circle(18 * k)
    t.end_fill()

    go_to(100 * k, offset_y + 201 * k)

    t.begin_fill()
    t.circle(18 * k)
    t.end_fill()

    go_to(-164 * k, offset_y + 320 * k)
    t.circle(60 * k)


    go_to(164 * k, offset_y + 320 * k)
    t.circle(60 * k)

# def bear(r=114):
#     offset_y = -200
#
#     go_to(0, offset_y)
#     t.pensize(3)
#     t.circle(r)
#
#     go_to(0, -160)
#
#     t.left(90)
#     t.forward(130)
#     t.right(90)
#     t.circle(18)
#
#     go_to(0, offset_y)
#
#     t.circle(190)
#
#     go_to(-100, 1)
#
#     t.begin_fill()
#     t.circle(18)
#     t.end_fill()
#
#     go_to(100, 1)
#
#     t.begin_fill()
#     t.circle(18)
#     t.end_fill()
#
#     go_to(-164, 120)
#     t.circle(60)
#
#     go_to(164, 120)
#     t.circle(60)


r = get_float('Введи радиус мордочки медведя: ', True)
bear(r)