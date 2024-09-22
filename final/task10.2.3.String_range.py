print('Строковый диапазон')
print()

while True:
    s = input('Введи строку: ')
    if len(s.strip()) == 0:
        print('Строка не должна быть пустой')
        print()
    else:
        break
print()
print(f'Символы со 2 по 5 строки "{s}": {s[1:5]}')
