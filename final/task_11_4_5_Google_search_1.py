import ifnumber

print('Google search 1')
print()

while True:
    n = input('Сколько строк будет введено? ')
    if_number = ifnumber.if_number(n)
    if if_number == 'int' and int(n) > 0:
        n = int(n)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное число')
        print()
print()
lst = []
for i in range(1, n + 1):
    while True:
        s = input(f'Введи {i}-ю строку: ')
        if len(s.strip()) == 0:
            print('Строка не должна быть пустой')
            print()
        else:
            break
    print()
    lst.append(s)
while True:
    search = input('Что будем искать? ')
    if len(search.strip()) == 0:
        print('Строка не должна быть пустой')
        print()
    else:
        break
print()
for el in lst:
    if search.lower() in el.lower():
        print(el)
