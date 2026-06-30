import turtle as t
from lib.turtle_functions import run_turtle
from lib.functions import get_color, get_float, get_int

@run_turtle
def colored_rays(params: dict):
    x1 = -300
    x2 = abs(x1)
    s = x2 * 2
    n = 20

    for i in range(n):
        t.pensize(params['rays_size'])
        t.color(params['rays_color'])
        t.goto(x1, params['last_y'])
        t.color(params['last_color'])
        t.dot(params['last_size'])
        t.penup()
        x1 += s / n
        t.goto(0, 0)
        t.pendown()

    t.color(params['start_color'])
    t.dot(params['start_size'])



def main():
    # params = {'start_size': 20,
    #           'start_color': '#a5c',
    #           'rays_count': 10,
    #           'rays_size': 3,
    #           'rays_color': '#bc9',
    #           'last_y': 300,
    #           'last_size': 10,
    #           'last_color': '#92d'}
    start_size = get_float('Введи размер точки начала: ')
    start_color = get_color('Введи цвет точки начала в формате HEX: ')

    rays_count = get_int('Введи количество лучей: ')
    rays_size = get_float('Введи толщину лучей: ')
    rays_color = get_color('Введи цвет лучей в формате HEX: ')

    last_y = get_float('Введи координату Y конечных точек: ', True)
    last_size = get_float('Введи размер конечных точек: ')
    last_color = get_color('Введи цвет конечных точек: ')
    params = {'start_size': start_size,
              'start_color': start_color,
              'rays_count': rays_count,
              'rays_size': rays_size,
              'rays_color': rays_color,
              'last_y': last_y,
              'last_size': last_size,
              'last_color': last_color}
    colored_rays(params)
main()