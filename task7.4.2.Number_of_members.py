print('Количество членов')
print()
counter = 0
while True:
    s = input('Введи строку: ')
    s = s.lower()
    if s != 'стоп' and s != 'хватит' and s != 'достаточно':
        counter += 1
    else:
        break
print(counter)
