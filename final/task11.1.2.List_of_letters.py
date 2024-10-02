import ifnumber

print('Список чисел')
print()

while True:
    n = input('Введи целое положительное число от 1 до 26: ')
    if_number = ifnumber.if_number(n)
    if if_number == 'int' and 1 <= int(n) <= 26:
        n = int(n)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное число от 1 до 26')
        print()
print()

s = ''
for i in range(n):
    s += chr(ord('a') + i)
print(list(s))
