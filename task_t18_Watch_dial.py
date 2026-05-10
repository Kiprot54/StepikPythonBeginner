import turtle as t

def turtle_line(side):
    line = 20
    space = 15
    t.penup()
    t.forward(side - line - space)
    t.pendown()
    t.forward(line)
    t.penup()
    t.forward(space)
    t.stamp()
    t.backward(side)

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

def get_side():
    while True:
        try:
            side = input('Введи расстояние от центра: ')
            if not side.isdigit():
                raise ValueError('Нужно ввести число')
            return int(side)
        except ValueError:
            print('Нужно ввести число')
        except IndexError:
            print('Пустая строка')


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


def get_time():
    while True:
        try:
            time = input('Введи время на часах от 1 до 12: ')
            if not time.isdigit() or not 1 <= int(time) <= 12:
                raise ValueError('Время введено неправильно')
            return int(time)
        except ValueError:
            print('Время введено неправильно')
        except IndexError:
            print('Пустая строка')

def turtle_circle(side, watch, arrow, time):
    t.shape(arrow)
    t.left(90)
    t.right(360 / 12 * time)
    t.stamp()
    t.left(360 / 12 * time)
    t.shape(watch)
    for i in range(12):
        turtle_line(side)
        t.left(30)

def run():
    watch = get_shape('циферблата')
    arrow = get_shape('стрелки')
    side = get_side()
    bg_color = get_bg_color()
    time = get_time()


    t.hideturtle()
    t.Screen().bgcolor(bg_color)
    turtle_circle(side, watch, arrow, time)

t.speed(0)
run()
t.done()