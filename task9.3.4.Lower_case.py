print('Нижний регистр')
print()

while True:
    s = input('Введи строку: ')
    if len(s) == 0:
        print('Строка не должна быть пустой')
        print()
    else:
        break
print()
counter = 0
for c in s:
    if c.islower():
        counter += 1
print(f'В строке "{s}" {counter} буквенных символов в нижнем регистре')
