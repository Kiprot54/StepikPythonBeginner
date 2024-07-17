import ifnumber
from math import pi, tan
print('Правильный многоугольник')
print()
while True:
    n = input('Введи количество сторон правильного многоугольника: ')
    if_number = ifnumber.if_number(n)
    if if_number == 'int' and int(n) > 0:
        n = int(n)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное число')
    print()
while True:
    a = input('Введи длину стороны правильного многоугольника: ')
    if_number = ifnumber.if_number(a)
    if if_number == 'int' and int(a) > 0:
        a = int(a)
        break
    elif if_number == 'float' and float(a) > 0:
        a = float(a)
        break
    else:
        print('Данные введены некорректно! Нужно ввести положительное число')
    print()
print()
S = n * a ** 2 / (4 * tan(pi / n))
print(f'Плошадь правильного {n}-угольника со стороной {a} равна {S}')
