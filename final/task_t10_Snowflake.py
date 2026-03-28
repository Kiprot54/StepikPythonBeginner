import turtle as t

def rhomb(side, angle):
    for _ in range(2):
        t.forward(side)
        t.right(angle)
        t.forward(side)
        t.right(180 - angle)

def snowflake(n, side, angle):
    t.left(angle / 2)
    for _ in range(n):
        rhomb(side, angle)
        t.right(360 / n)

t.speed(0)
snowflake(12, 100, 0)
t.done()