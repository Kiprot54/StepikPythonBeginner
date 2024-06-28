print('Пересечение отрезков')
print()
while True:
    a1 = input('Введи координату a1: ')
    if a1.isdigit() and a1 != 0:
        a1 = int(a1)
        break
    else:
        print('Нужно ввести целое положительное число')
        print()
while True:
    b1 = input('Введи координату b1: ')
    if b1.isdigit() and b1 != 0:
        b1 = int(b1)
        break
    else:
        print('Нужно ввести целое положительное число')
        print()
while True:
    a2 = input('Введи координату a2: ')
    if a2.isdigit() and a2 != 0:
        a2 = int(a2)
        break
    else:
        print('Нужно ввести целое положительное число')
        print()
while True:
    b2 = input('Введи координату b2: ')
    if b2.isdigit() and b2 != 0:
        b2 = int(b2)
        break
    else:
        print('Нужно ввести целое положительное число')
        print()
print()
if b1 < a1:
    b1, a1 = a1, b1
if b2 < a2:
    b2, a2 = a2, b2
if a1 > a2:
    a1, a2 = a2, a1
    b1, b2 = b2, b1
if b1 < a2:
    print(f'Отрезки [{a1};{b1}] и [{a2}; {b2}] не пересекаются')
elif b1 == a2:
    print(f'У отрезков [{a1};{b1}] и [{a2}; {b2}] одна общая точка {b1}')
elif a2 < b1:
    if b2 >= b1:
        print(f'Пересечение отрезков [{a1};{b1}] и [{a2}; {b2}] - {a2}, {b1}')
    else:
        print(f'Пересечение отрезков [{a1};{b1}] и [{a2}; {b2}] - {a2}, {b2}')
