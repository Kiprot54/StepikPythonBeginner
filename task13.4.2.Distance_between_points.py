from math import sqrt
import ifnumber

print('Расстояние между точками')
print()

def get_distance(x1, y1, x2, y2):
    p = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return p

def get_coord(symbol, number):
    while True:
        n = input(f'Введи координату {symbol}{number}: ')
        if_number = ifnumber.if_number(n)
        if if_number == 'int':
            n = int(n)
            return n
        else:
            print('Данные введены некорректно! Нужно ввести число')
            print()

coords = []
for i in range(4):
    symbol = 'x'
    if i % 2 == 1:
        symbol = 'y'
    number = 1
    if i > 1:
        number = 2
    coords.append(get_coord(symbol, number))

print(get_distance(coords[0], coords[1], coords[2], coords[3]))
