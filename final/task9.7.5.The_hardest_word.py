print('Самое тяжёлое слово')
print()

max_total = 0
max_s = ''
all_s = ''
for i in range(1, 5):
    s_total = 0
    while True:
        s = input(f'Введи {i} слово: ').strip()
        if len(s) == 0:
            print('Строка не должна быть пустой')
            print()
        elif s.count(' ') > 0:
            print('Нужно ввести одно слово')
        else:
            break
    all_s += s
    if i != 4:
        all_s += ', '
    for c in s:
        s_total += ord(c)
    if max_total < s_total:
        max_total = s_total
        max_s = s
print(f'Из 4 слов <{all_s}> самое "тяжёлое" слово "{max_s}"')
