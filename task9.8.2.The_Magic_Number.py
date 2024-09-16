print('Волшебное число')
print()

min_s = ''
max_s = ''
mult = 0
for i in range(1, 5):
    while True:
        s = input(f'Введи {i}-ю строку: ')
        if len(s.strip()) == 0:
            print('Строка не должна быть пустой')
            print()
        else:
            break
    if i == 1:
        min_s = s
        max_s = s
    else:
        min_s = min(min_s, s)
        max_s = max(max_s, s)
mult = ord(min_s[-1]) * ord(max_s[-1])
print(mult ** 2)