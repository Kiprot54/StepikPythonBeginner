import ifnumber

print('Середина отрезка')
print()

def get_middle_point(x1, y1, x2, y2):
    return (x1 + x2) / 2, (y1 + y2) / 2

def get_coord(coord):
    while True:
        num = input(f'Введи координату {coord}: ')
        if_number = ifnumber.if_number(num)
        if if_number == 'int':
            num = int(num)
            return num
        elif if_number == 'float':
            num = float(num)
            return num
        else:
            print('Данные введены некорректно! Нужно ввести число')
            print()

x1, y1 = get_coord('x1'), get_coord('y1')
x2, y2 = get_coord('x2'), get_coord('y2')

x, y = get_middle_point(x1, y1, x2, y2)
print(x, y)