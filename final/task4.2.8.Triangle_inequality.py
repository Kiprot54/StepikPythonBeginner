print('Неравенство треугольника')
print()
while True:
    a = input('Введи первую сторону треугольника: ')
    if a.isdigit():
        a = int(a)
        break
    else:
        print('Нужно ввести целое положительное число')
        print()
print()
while True:
    b = input('Введи вторую сторону треугольника: ')
    if b.isdigit():
        b = int(b)
        break
    else:
        print('Нужно ввести целое положительное число')
        print()
print()
while True:
    c = input('Введи третью сторону треугольника: ')
    if c.isdigit():
        c = int(c)
        break
    else:
        print('Нужно ввести целое положительное число')
        print()
print()
if a + b > c and a + c > b and b + c > a:
    print(f'Треугольник со сторонами {a}, {b}, {c} существует')
else:
    print(f'Треугольник со сторонами {a}, {b}, {c} не существует')