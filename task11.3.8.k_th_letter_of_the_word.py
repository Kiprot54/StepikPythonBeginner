import ifnumber

print('k-ая буква слова')
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
    k = input('Введи номер буквы, которую нужно найти в строке: ')
    if_number = ifnumber.if_number(k)
    if if_number == 'int' and int(k) > 0:
        k = int(k)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное число')
        print()

print()

st = ''
for el in strings:
    string1 = el
    if len(string1) >= k:
        smb = string1[k - 1]
        st += smb
print(st)
