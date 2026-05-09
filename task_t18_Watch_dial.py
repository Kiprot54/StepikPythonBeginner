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
    color = ""
    while True:
        color = input('Введи цвет фона: ')
        len_color = len(color) == 4 or len(color) == 7
        hex_color = '0123456789abcdef'
        is_correct_hex = True

        for i in range(1, len(color)):
            if color[i] not in hex_color:
                is_correct_hex = False
                break


        if color[0] != '#' or not len_color or not is_correct_hex:
            print('Цвет введён неправильно')
            continue
        break
    return color

def get_side():
    while True:
        side = input('Введи расстояние от центра: ')
        if not side.isdigit():
            print('Нужно ввести число')
            continue
        return int(side)


def get_shape(target):
    shape = ''
    shape_list = ['turtle', 'arrow', 'triangle']
    while True:
        shape = input(f'Введи рисунок {target} (arrow, turtle, triangle): ')
        if shape not in shape_list:
            print('Неверный ввод')
            continue
        break
    return shape

def get_time():
    while True:
        time = input('Введи время на часах от 1 до 12: ')
        if not time.isdigit():
            print('Время введено неправильно')
            continue
        elif not 1 <= int(time) <= 12:
            print('Время введено неправильно')
            continue
        return int(time)

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