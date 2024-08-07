import ifnumber

print('Таблица-2')
print()

while True:
    n = input('Введи целое положительное число меньше 10: ')
    if_number = ifnumber.if_number(n)
    if if_number == 'int' and 0 < int(n) < 10:
        n = int(n)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное число меньше 10')
        print()
print()
for i in range(1, n + 1):
    for j in range(1, 10):
        print(i, '+', j, '=', i + j)
    print()
