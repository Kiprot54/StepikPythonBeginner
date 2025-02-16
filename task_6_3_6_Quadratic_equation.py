import ifnumber
from math import sqrt

print('Квадратное уравнение')
print()

while True:
    s = input('Введи число A квадратного уравнения: ')
    if_number = ifnumber.if_number(s)
    if if_number == 'int':
        a = int(s)
        break
    elif if_number == 'float':
        a = float(s)
        break
    else:
        print('Данные введены некорректно! Нужно ввести число')
        print()
while True:
    s = input('Введи число B квадратного уравнения: ')
    if_number = ifnumber.if_number(s)
    if if_number == 'int':
        b = int(s)
        break
    elif if_number == 'float':
        b = float(s)
        break
    else:
        print('Данные введены некорректно! Нужно ввести число')
        print()
while True:
    s = input('Введи число C квадратного уравнения: ')
    if_number = ifnumber.if_number(s)
    if if_number == 'int':
        c = int(s)
        break
    elif if_number == 'float':
        c = float(s)
        break
    else:
        print('Данные введены некорректно! Нужно ввести число')
        print()

d = b ** 2 - 4 * a * c

if d < 0:
    print('Нет корней')
elif d == 0:
    x = -b / (2 * a)
    print(x)
else:
    x1 = (-b - sqrt(d)) / (2 * a)
    x2 = (-b + sqrt(d)) / (2 * a)
    print(min(x1, x2))
    print(max(x1, x2))
