import ifnumber
from math import sqrt
print('Средние значения')
print()
while True:
    a = input('Введи число: ')
    if_number = ifnumber.if_number(a)
    if if_number == 'int':
        a = int(a)
        break
    elif if_number == 'float':
        a = float(a)
        break
    else:
        print('Данные введены некорректно! Нужно ввести число')
    print()
while True:
    b = input('Введи число: ')
    if_number = ifnumber.if_number(b)
    if if_number == 'int':
        b = int(b)
        break
    elif if_number == 'float':
        b = float(b)
        break
    else:
        print('Данные введены некорректно! Нужно ввести число')
    print()
print()
middle_arithm = (a + b) / 2
middle_geom = sqrt(a * b)
middle_garmon = 2 * a * b / (a + b)
middle_quadro = sqrt((a ** 2 + b ** 2) / 2)
print(f'Среднее арифметическое чисел {a} и {b}: {middle_arithm}')
print(f'Среднее геометрическое чисел {a} и {b}: {middle_geom}')
print(f'Среднее гармоническое чисел {a} и {b}: {middle_garmon}')
print(f'Среднее квадратичное чисел {a} и {b}: {middle_quadro}')


