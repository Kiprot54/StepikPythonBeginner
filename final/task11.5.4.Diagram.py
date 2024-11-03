print('Диаграмма')
print()

while True:
    s = input('Введи положительное целые числа через пробел: ')
    if len(s.strip()) == 0:
        print('Строка не должна быть пустой')
        print()
    else:
        break
print()

s_lst = s.split()
for el in s_lst:
    if el.isdigit():
        print('+' * int(el))
    else:
        print()
