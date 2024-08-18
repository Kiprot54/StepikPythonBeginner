print('ФИО')
print()
while True:
    name = input('Введи своё имя: ').strip()
    if len(name) == 0:
        print('Строка не должна быть пустой')
        print()
    else:
        break
while True:
    surname = input('Введи свою фамилию: ').strip()
    if len(surname) == 0:
        print('Строка не должна быть пустой')
        print()
    else:
        break
while True:
    patronim = input('Введи своё отчество: ').strip()
    if len(patronim) == 0:
        print('Строка не должна быть пустой')
        print()
    else:
        break
print()
print(surname[0], name[0], patronim[0], sep='')
