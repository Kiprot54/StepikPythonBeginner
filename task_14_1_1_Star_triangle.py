print('Звёздный треугольник')
print()

def draw_triangle():
    num = 8
    for i in range(1, num + 1):
        print(' ' * (num - i) + '*' * (2 * i - 1))

draw_triangle()