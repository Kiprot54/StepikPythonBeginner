import turtle as t

def get_shape(target):
    shape_list = ['turtle', 'arrow', 'triangle']
    while True:
        try:
            shape = input(f'Введи рисунок {target} (arrow, turtle, triangle): ')
            if shape not in shape_list:
                raise ValueError('Shape не из списка')
            return shape
        except ValueError:
            print('Нужно ввести рисунок из списка')
        except IndexError:
            print('Пустая строка')

def get_bg_color():
    hex_color = '0123456789abcdef'
    while True:
        try:
            color = input('Введи цвет фона: ')

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

def get_count():
    while True:
        try:
            count = int(input('Введи количество рисунков: '))
            if count <= 0:
                raise ValueError('Нужно ввести количество рисунков')
            return count
        except ValueError:
            print('Нужно ввести положительное число')
        except IndexError:
            print('Пустая строка')

def run():
    arrow = get_shape('стрелки')
    bg_color = get_bg_color()
    count = get_count()

    t.penup()
    t.Screen().bgcolor(bg_color)
    spiral(count, arrow)

def spiral(count, arrow):
    t.shape(arrow)
    distance = 5
    for i in range(count):
        t.stamp()
        t.forward(distance)
        t.right(25)
        distance += 2

t.speed(0)
run()
t.done()