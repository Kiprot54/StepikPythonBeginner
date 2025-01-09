import ifnumber
from math import sqrt

print('Евклидово расстояние')
print()

while True:
    x1 = input('Введи первую координату (x1) первой точки: ')
    if_number = ifnumber.if_number(x1)
    if (if_number == 'int' or if_number == 'float') and float(x1) > 0:
        x1 = float(x1)
        break
    else:
        print('Данные введены некорректно! Нужно ввести положительное число')
    print()
while True:
    y1 = input('Введи вторую координату (y1) первой точки: ')
    if_number = ifnumber.if_number(y1)
    if (if_number == 'int' or if_number == 'float') and float(y1) > 0:
        y1 = float(y1)
        break
    else:
        print('Данные введены некорректно! Нужно ввести положительное число')
    print()
while True:
    x2 = input('Введи первую координату (x2) второй точки: ')
    if_number = ifnumber.if_number(x2)
    if (if_number == 'int' or if_number == 'float') and float(x2) > 0:
        x2 = float(x2)
        break
    else:
        print('Данные введены некорректно! Нужно ввести положительное число')
    print()
while True:
    y2 = input('Введи вторую координату (y2) второй точки: ')
    if_number = ifnumber.if_number(y2)
    if (if_number == 'int' or if_number == 'float') and float(y2) > 0:
        y2 = float(y2)
        break
    else:
        print('Данные введены некорректно! Нужно ввести положительное число')
    print()

p = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
print(f'Евклидово расстояние между двумя точками с координатами ({x1}; {y1}) и ({x2}; {y2}) равняется {p}')
