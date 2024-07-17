import ifnumber
from math import pi
print('Площадь и длина')
print()
while True:
    r = input('Введи число: ')
    if_number = ifnumber.if_number(r)
    if if_number == 'int' and int(r) > 0:
        r = int(r)
        break
    elif if_number == 'float' and float(r) > 0:
        r = float(r)
        break
    else:
        print('Данные введены некорректно! Нужно ввести число')
    print()
print()
S = pi * r ** 2
C = 2 * pi * r
print(f'Площадь окружности радиуса {r} равна {S}')
print(f'Длина окружности радиуса {r} равна {C}')
