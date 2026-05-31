def get_int(text, is_negative=False):
    while True:
        try:
            n = int(input(text))
        except ValueError:
            print('Нужно ввести целое число')
            continue

        if not is_negative and n <= 0:
            print('Нужно ввести положительное число')
            continue

        return n

def get_float(text, is_negative=False):
    while True:
        try:
            n = float(input(f'{text}'))
        except ValueError:
            print('Нужно ввести число')
            continue

        if not is_negative and n <= 0:
            print('Нужно ввести положительное число')
            continue

        return n

def get_color(text):
    hex_color = '0123456789abcdef'
    while True:
        try:
            color = input(f'{text}')
            if color[0] != '#':
                raise ValueError('Нет символа #')
            if len(color) not in (4, 7):
                raise ValueError('Неверная длина')
            for char in color[1:]:
                if char.lower() not in hex_color:
                    raise ValueError('Не HEX формат')
            return color
        except ValueError:
            print('Цвет введён неправильно')
        except IndexError:
            print('Пустая строка')

def get_time(start, end):
    while True:
        try:
            time = get_int(f'Введи время на часах от {start} до {end}: ')
            if not start <= time <= end:
                raise ValueError('Время введено неправильно')
            return int(time)
        except ValueError:
            print('Время введено неправильно')
        except IndexError:
            print('Пустая строка')