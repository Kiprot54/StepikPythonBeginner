print('Шахматная доска')
print()
while True:
    x1 = input('Введи координату X первой клетки: ')
    if x1.isdigit() and 1 <= int(x1) <= 8:
        x1 = int(x1)
        break
    else:
        print('Нужно ввести целое число от 1 до 8')
        print()
while True:
    y1 = input('Введи координату Y первой клетки: ')
    if y1.isdigit() and 1 <= int(y1) <= 8:
        y1 = int(y1)
        break
    else:
        print('Нужно ввести целое число от 1 до 8')
        print()
while True:
    x2 = input('Введи координату X второй клетки: ')
    if x2.isdigit() and 1 <= int(x2) <= 8:
        x2 = int(x2)
        break
    else:
        print('Нужно ввести целое число от 1 до 8')
        print()
while True:
    y2 = input('Введи координату Y второй клетки: ')
    if y2.isdigit() and 1 <= int(y2) <= 8:
        y2 = int(y2)
        break
    else:
        print('Нужно ввести целое число от 1 до 8')
        print()
print()
if (x1 % 2 != 0  and y1 % 2 != 0) or (x1 % 2 == 0 and y1 % 2 == 0):
    if (x2 % 2 != 0 and y2 % 2 != 0) or (x2 % 2 == 0 and y2 % 2 == 0):
        print(f'Клетки с координатами ({x1};{y1}) и ({x2};{y2}) одинакового цвета - белого')
    else:
        print(f'Клетки с координатами ({x1};{y1}) и ({x2};{y2}) разного цвета')
else:
    if (x2 % 2 != 0 and y2 % 2 != 0) or (x2 % 2 == 0 and y2 % 2 == 0):
        print(f'Клетки с координатами ({x1};{y1}) и ({x2};{y2}) разного цвета')
    else:
        print(f'Клетки с координатами ({x1};{y1}) и ({x2};{y2}) одинакового цвета - чёрного')

