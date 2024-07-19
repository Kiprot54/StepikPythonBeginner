import ifnumber
from math import pi

print('Площадь и длина')
print()

while True:
    r = input('Введи число: ')
    if_number = ifnumber.if_number(r)
    if (if_number == 'int' or if_number == 'float') and float(r) > 0:
        r = float(r)
        break
    else:
        print('Данные введены некорректно! Нужно ввести положительное число')
    print()

print()
S = pi * r ** 2
C = 2 * pi * r
print(f'Площадь окружности с радиусом {r} равна {S}')
print(f'Длина окружности с радиусом {r} равна {C}')
