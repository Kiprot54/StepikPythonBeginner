print('Заглавные буквы')
print()

while True:
    s = input('Введи строку: ')
    if len(s.strip()) == 0:
        print('Строка не должна быть пустой')
        print()
    else:
        break
print()
print(f'Строка "{s}" заглавными буквами: {s.upper()}')
