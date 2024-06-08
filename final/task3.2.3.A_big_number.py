print('Большое число')
print()
while True:
    a = input('Введи первое число: ')
    if a.isdigit() or (a[0] == '-' and a[1:].isdigit()):
        a = int(a)
        break
    else:
        print('Нужно ввести целое число')
        print()
while True:
    b = input('Введи второе число: ')
    if b.isdigit() or (b[0] == '-' and b[1:].isdigit()):
        b = int(b)
        break
    else:
        print('Нужно ввести целое число')
        print()
while True:
    c = input('Введи третье число: ')
    if c.isdigit() or (c[0] == '-' and c[1:].isdigit()):
        c = int(c)
        break
    else:
        print('Нужно ввести целое число')
        print()
while True:
    d = input('Введи четвёртое число: ')
    if d.isdigit() or (d[0] == '-' and d[1:].isdigit()):
        d = int(d)
        break
    else:
        print('Нужно ввести целое число')
        print()
print(f'{a} ^ {b} + {c} ^ {d} = {a ** b + c ** d}')