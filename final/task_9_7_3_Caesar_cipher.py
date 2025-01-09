import ifnumber

print('Шифр Цезаря')
print()

while True:
    n = input('Введи целое число от 1 до 25: ')
    if_number = ifnumber.if_number(n)
    if if_number == 'int' and 1 <= int(n) <= 25:
        n = int(n)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое число от 1 до 25')
        print()
while True:
    s = input('Введи строку: ')
    if len(s.strip()) == 0:
        print('Строка не должна быть пустой')
        print()
    else:
        break
print()
for c in s:
    c_ord = ord(c) - n
    if c_ord < 97:
        c_ord += 26
    print(chr(c_ord), end='')
