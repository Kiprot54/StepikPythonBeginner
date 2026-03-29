import turtle as t

def draw_polygon(n, side, dot_size):
    angle_polygon = 180 * (n - 2)
    angle = angle_polygon / n
    for i in range(n):
        t.pensize(dot_size/2)
        t.dot()
        t.pensize(1)
        t.forward(side)
        t.left(180 - angle)

def dotted_polygon():
    n = int(input("Введи количество сторон многоугольника: "))
    side = int(input("Введи длину стороны многоугольника: "))
    dot_size = int(input("Введи размер точки: "))
    draw_polygon(n, side, dot_size)


t.speed(0)
dotted_polygon()
t.done()