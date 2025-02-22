import ifnumber

print('Середина отрезка')
print()

def get_middle_point(x1, y1, x2, y2):
    return (x1 + x2) / 2, (y1 + y2) / 2

def get_x1():
    while True:
        x1 = input('Введи координату x1: ')
        if_number = ifnumber.if_number(x1)
        if if_number == 'int':
            x1 = int(x1)
            return x1
        else:
            print('Данные введены некорректно! Нужно ввести число')
            print()

def get_y1():
    while True:
        y1 = input('Введи координату y1: ')
        if_number = ifnumber.if_number(y1)
        if if_number == 'int':
            y1 = int(y1)
            return y1
        else:
            print('Данные введены некорректно! Нужно ввести число')
            print()

def get_x2():
    while True:
        x2 = input('Введи координату x2: ')
        if_number = ifnumber.if_number(x2)
        if if_number == 'int':
            x2 = int(x2)
            return x2
        else:
            print('Данные введены некорректно! Нужно ввести число')
            print()

def get_y2():
    while True:
        y2 = input('Введи координату y2: ')
        if_number = ifnumber.if_number(y2)
        if if_number == 'int':
            y2 = int(y2)
            return y2
        else:
            print('Данные введены некорректно! Нужно ввести число')
            print()

x1, y1 = get_x1(), get_y1()
x2, y2 = get_x2(), get_y2()

print(get_middle_point(x1, y1, x2, y2))