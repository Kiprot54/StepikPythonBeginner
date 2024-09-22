print('Сортируем слова')
print()

min_s = ''
max_s = ''
middle_s = ''
s_sum = ''
s_all = ''
for i in range(1, 4):
    while True:
        s = input(f'Введи {i}-е слово: ')
        if len(s.strip()) == 0:
            print('Строка не должна быть пустой')
            print()
        elif s.count(' ') > 0:
            print('Нужно ввести слово')
            print()
        else:
            break

    s_sum += s
    if min_s == '':
        min_s = s
        max_s = s
        s_all = s
    else:
        min_s = min(min_s, s)
        max_s = max(max_s, s)
        s_all += ', ' + s
middle_s = s_sum.replace(max_s, '').replace(min_s, '')
print(f'Слова "{s_all}", отсортированные по возрастанию:\n {min_s} {middle_s} {max_s}')
