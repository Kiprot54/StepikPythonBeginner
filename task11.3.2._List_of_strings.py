import ifnumber

print('Список строк')
print()

while True:
    n = input('Введи целое положительное число: ')
    if_number = ifnumber.if_number(n)
    if if_number == 'int' and int(n) > 0:
        n = int(n)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное число')
        print()

lst = []
print()
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
print(lst)

