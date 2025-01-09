print('Ход коня')
print()
while True:
    x1 = input('Введи координату x1: ')
    if x1.isdigit() and 1 <= int(x1) <= 8:
        x1 = int(x1)
        break
    else:
        print('Нужно ввести целое число от 1 до 8')
        print()
while True:
    y1 = input('Введи координату y1: ')
    if y1.isdigit() and 1 <= int(y1) <= 8:
        y1 = int(y1)
        break
    else:
        print('Нужно ввести целое число от 1 до 8')
        print()
while True:
    x2 = input('Введи координату x2: ')
    if x2.isdigit() and 1 <= int(x2) <= 8:
        x2 = int(x2)
        break
    else:
        print('Нужно ввести целое число от 1 до 8')
        print()
while True:
    y2 = input('Введи координату y2: ')
    if y2.isdigit() and 1 <= int(y2) <= 8:
        y2 = int(y2)
        break
    else:
        print('Нужно ввести целое число от 1 до 8')
        print()
print()
if (abs(x2 - x1) == 1 and abs(y2 - y1) == 2) or (abs(x2 - x1) == 2 and abs(y2 - y1) == 1):
    print(f'Конь может попасть с клетки с координатами ({x1}, {y1}) на клетку с координатами ({x2}, {y2})')
else:
    print(f'Конь НЕ может попасть с клетки с координатами ({x1}, {y1}) на клетку с координатами ({x2}, {y2})')
