print('Значение функции')
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
print()
print(f'3 * ({a} + {b}) ^ 3 + 275 * {b} ^ 2 - 127 * {a} - 41 = {3 * (a + b) * (a + b) * (a + b) + 275 * b * b - 127 * a - 41}')
