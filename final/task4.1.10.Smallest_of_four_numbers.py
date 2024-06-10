print('Наименьшее из четырёх чисел')
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
while True:
    n4 = input('Введи четвёртое число: ')
    if n4.isdigit() or (n4[0] == '-' and n4[1:].isdigit()):
        n4 = int(n4)
        break
    else:
        print('Нужно ввести целое число')
        print()
print()
n_min = n1
if n2 < n_min:
    n_min = n2
if n3 < n_min:
    n_min = n3
if n4 < n_min:
    n_min = n4
print(f'Наименьшее из чисел {n1}, {n2}, {n3}, {n4} - {n_min}')
