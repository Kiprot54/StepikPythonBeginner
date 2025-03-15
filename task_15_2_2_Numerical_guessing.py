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

n = random.randint(1, 100)

print('Добро пожаловать в числовую угадайку')


while True:
    num = input('Введи целое число от 1 до 100: ')
    if not is_valid(num):
        print('А может быть всё-таки введём целое число от 1 до 100?')
    else:
        num = int(num)
        if num < n:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif num > n:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print('Вы угадали, поздравляем!')
            break

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')