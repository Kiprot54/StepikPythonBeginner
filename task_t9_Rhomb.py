import turtle as t

def rhomb(side, angle):
    for _ in range(2):
        t.forward(side)
        t.left(angle)
        t.forward(side)
        t.left(180 - angle)

t.speed(0)
rhomb(100, 90)
t.done()