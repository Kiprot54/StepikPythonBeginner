print('Строковые минимум и максимум')
print()

s = ''
min_s = ''
max_s = ''
while True:
    while True:
        s = input('Введи строку: ')
        if len(s.strip()) == 0:
            print('Строка не должна быть пустой')
            print()
        else:
            break

    if s == 'КОНЕЦ':
        break
    if min_s == '':
        min_s = s
        max_s = s
    else:
        min_s = min(min_s, s)
        max_s = max(max_s, s)
print()
print(f'Минимальная строка ⬇️: {min_s}')
print(f'Максимальная строка ⬆️: {max_s}')