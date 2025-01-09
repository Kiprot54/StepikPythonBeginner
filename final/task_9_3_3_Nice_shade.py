print('Хороший оттенок')
print()

while True:
    s = input('Введи строку: ')
    if len(s) == 0:
        print('Строка не должна быть пустой')
        print()
    else:
        break
print()
if 'хорош' in s.lower():
    temp = 'есть подстрока'
else:
    temp = 'нет подстроки'
print(f'В строке "{s}" {temp} "хорош"')
