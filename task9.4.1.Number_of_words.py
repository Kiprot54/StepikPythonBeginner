print('Нижний регистр')
print()

s = input('Введи строку: ')
print()

counter_space = s.count(' ')
if s == '':
    print('Строка пустая')
else:
    print(f'В строке "{s}" {counter_space + 1} слов')
