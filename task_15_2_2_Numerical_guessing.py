import random

print('Числовая угадайка')
print()

def is_valid(s):
    a = s.isdigit()
    if a:
        b = 1 <= int(s) <= 100
        if b:
            return True
    return False

def get_num():
    while True:
        numb = input('Нужно узнать диапазон, в котором вы будете угадывать число. Он начинается с 1. Каким числом он закончится? ')
        if not is_valid(numb):
            print(f'А может быть всё-таки введём целое число больше 1?')
            print()
        else:
            numb = int(numb)
            return numb

print('Добро пожаловать в числовую угадайку')

repeat = 'y'
while repeat == 'y':
    number = get_num()

    n = random.randint(1, number)

    attempts = 0
    while True:
        num = input(f'Введи целое число от 1 до {number}: ')
        if not is_valid(num):
            print(f'А может быть всё-таки введём целое число от 1 до {number}?')
        else:
            attempts += 1
            num = int(num)
            if num < n:
                print('Ваше число меньше загаданного, попробуйте еще разок')
            elif num > n:
                print('Ваше число больше загаданного, попробуйте еще разок')
            else:
                print('Вы угадали, поздравляем!')
                break
    print(f'Вы угадали число {n} за {attempts} попыток')
    print()
    repeat = input('Сыграете ещё раз? y (да) или n (нет) ')
    while repeat != 'y' and repeat != 'n':
        print('Я вас не понял. Повторите, пожалуйста')
        print()
        repeat = input('Сыграете ещё раз? y (да) или n (нет) ')
    print()

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')