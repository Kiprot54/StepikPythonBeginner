print('Инициалы')
print()

while True:
    initials = input('Введи имя, отчество и фамилию через пробел: ')
    if len(initials.strip()) == 0:
        print('Строка не должна быть пустой')
        print()
    else:
        break
print()

initials_lst = initials.split()
first_symbols = []
for el in initials_lst:
    first_symbols.append(el[0])
print('.'.join(first_symbols) + '.')
