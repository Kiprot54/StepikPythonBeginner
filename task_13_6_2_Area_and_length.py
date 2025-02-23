from math import pi
import ifnumber

print('Площадь и длина')
print()

def get_circle(radius):
    return 2 * pi * radius, pi * radius ** 2

def get_num():
    while True:
        num = input('Введи радиус окружности: ')
        if_number = ifnumber.if_number(num)
        if if_number == 'int' and int(num) > 0:
            num = int(num)
            return num
        elif if_number == 'float' and float(num) > 0:
            num = float(num)
            return num
        else:
            print('Данные введены некорректно! Нужно ввести положительное число')
            print()

radius = get_num()
c, s = get_circle(radius)
print(f'Длина окружности радиуса {radius} равна {c}')
print(f'Площадь круга радиуса {radius} равна {s}')
