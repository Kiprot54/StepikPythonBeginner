print('Какая следующая буква?')
print()
while True:
    s = input('Введи букву русского алфавита в верхнем регистре: ')
    s1 = s.strip()
    if len(s1) == 0:
        print('Строка не должна быть пустой')
    elif len(s1) > 1:
        print('Нужно ввести одну букву')
    elif not s1.isupper():
        print('Нужно ввести букву в верхнем регистре')
    elif not ord('А') <= ord(s) <= ord('Я'):
        print('Нужно ввести букву русского алфавита')
    else:
        break
    print()
if s == 'Ё':
    s = 'Е'
if s == 'Я':
    print('Дальше букв нет')
else:
    print(f'После буквы {s} идёт буква {chr(ord(s) + 1)}')