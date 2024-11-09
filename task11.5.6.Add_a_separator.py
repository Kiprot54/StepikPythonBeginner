print('Добавь разделитель')
print()

while True:
    s = input('Введи строку: ')
    if len(s.strip()) == 0:
        print('Строка не должна быть пустой')
        print()
    else:
        break
print()

while True:
    separator = input('Введи строку-разделитель: ')
    if len(s.strip()) == 0:
        print('Строка не должна быть пустой')
        print()
    else:
        break
print()
separator_lst = separator.join(s)
print(separator_lst)