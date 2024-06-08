print('Сумма квадратов VS квадрат суммы')
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
print(f'Квадрат суммы чисел {a} и {b} равен: {(a + b) ** 2}')
print(f'Сумма квадратов чисел {a} и {b} равна: {a ** 2 + b ** 2}')
