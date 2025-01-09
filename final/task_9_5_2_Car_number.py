print('Автомобильный номер')
print()

while True:
    s = input('Введи автомобильный номер: ')
    if len(s) == 0:
        print('Строка не должна быть пустой')
        print()
    else:
        break
print()
temp = ''
all_digits = '0123456789'
all_letters = 'АВЕКМНОРСТУХ'
if 8 <= len(s) <= 10:
    letters = s[0] + s[4:6]
    digits = s[1:4] + s[7:]
    separator = s[6]
    if len(digits) > 4 and digits.isdigit() and separator == '_':
        temp = ''
        for c in letters:
            if c not in all_letters:
                temp = 'не'
                break
    else:
        temp = 'не'
else:
    temp = 'не'
print(f'Автомобильный номер {s} {temp}корректный')
