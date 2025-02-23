from math import sqrt

import ifnumber

print('Корни уравнения')
print()

def solve(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return 'NO', 'NO'
    elif d == 0:
        x = -b / (2 * a)
        return x, x
    else:
        x1 = (-b - sqrt(d)) / (2 * a)
        x2 = (-b + sqrt(d)) / (2 * a)
        return min(x1, x2), max(x1, x2)

def get_num(name):
    while True:
        num = input(f'Введи число {name}: ')
        if_number = ifnumber.if_number(num)
        if if_number == 'int':
            num = int(num)
            if name != 'a':
                return num
            else:
                if num == 0:
                    print('Данные введены некорректно! Число не должно быть равно нулю')
                    print()
                else:
                    return num
        elif if_number == 'float':
            num = float(num)
            if name != 'a':
                return num
            else:
                if num == 0:
                    print('Данные введены некорректно! Число не должно быть равно нулю')
                    print()
                else:
                    return num
        else:
            print('Данные введены некорректно! Нужно ввести число')
            print()

a, b, c = get_num('a'), get_num('b'), get_num('c')
x1, x2 = solve(a, b, c)

print(f'В уравнении {a} * x ** 2 + {b} * x + {c} = 0')
if x1 == 'NO':
    print('Нет корней')
elif x1 == x2:
    print(f'один корень: {x1}')
else:
    print(f'два корня: {x1} и {x2}')
