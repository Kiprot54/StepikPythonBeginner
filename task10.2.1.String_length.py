print('Длина строки')
print()

while True:
    s = input('Введи строку: ')
    if len(s.strip()) == 0:
        print('Строка не должна быть пустой')
        print()
    else:
        break
print()
print(f'Длина строки "{s}": {len(s)}')
