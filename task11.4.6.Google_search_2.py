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

strings = []
for i in range(1, n + 1):
    while True:
        s = input(f'Введи {i}-ю строку: ')
        if len(s.strip()) == 0:
            print('Строка не должна быть пустой')
            print()
        else:
            break
    strings.append(s)

print()
while True:
    k = input('Сколько будет поисковых запросов? ')
    if_number = ifnumber.if_number(k)
    if if_number == 'int' and int(k) > 0:
        k = int(k)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное число')
        print()
print()

searches = []
for i in range(1, k + 1):
    while True:
        search = input(f'Введи {i}-й запрос: ')
        if len(search.strip()) == 0:
            print('Строка не должна быть пустой')
            print()
        else:
            break
    searches.append(search)

print()
for el in strings:
    flag = True
    for i in range(len(searches)):
        if searches[i].lower() not in el.lower():
            flag = False
            break
    if flag:
        print(el)
