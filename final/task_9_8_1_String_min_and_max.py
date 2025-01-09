print('Строковые минимум и максимум')
print()

s_all = ''
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
    s_all += '\n' + s
    if min_s == '':
        min_s = s
        max_s = s
    else:
        min_s = min(min_s, s)
        max_s = max(max_s, s)
print()
print(f'Среди строк: {s_all}')
print(f'минимальная строка ⬇️: {min_s}')
print(f'максимальная строка ⬆️: {max_s}')
