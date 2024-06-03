print('Сумма трёх чисел')
print()
while True:
    n1 = input('Введи первое число: ')

    if n1.isdigit() or (n1[0] == '-' and n1[1:].isdigit()):
        n1 = int(n1)
        break
    else:
        print('Нужно ввести целое число')
        print()
while True:
    n2 = input('Введи второе число: ')

    if n2.isdigit() or (n2[0] == '-' and n2[1:].isdigit()):
        n2 = int(n2)
        break
    else:
        print('Нужно ввести целое число')
        print()
while True:
    n3 = input('Введи третье число: ')

    if n3.isdigit() or (n3[0] == '-' and n3[1:].isdigit()):
        n3 = int(n3)
        break
    else:
        print('Нужно ввести целое число')
        print()
print()
print('Сумма введённых чисел:', n1 + n2 + n3)
