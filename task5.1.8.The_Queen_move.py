print('Ход ферзя')
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
if (x2 - x1 == y2 - y1 or x2 - x1 == -(y2 - y1)) or ((x2 - x1 > 0 and y2 == y1) or (x1 - x2 > 0 and y2 == y1) or (x1 == x2 and y2 - y1 > 0) or (x1 == x2 and y1 - y2 > 0)):
    print(f'Ферзь может попасть с клетки с координатами ({x1}, {y1}) на клетку с координатами ({x2}, {y2})')
else:
    print(f'Ферзь НЕ может попасть с клетки с координатами ({x1}, {y1}) на клетку с координатами ({x2}, {y2})')