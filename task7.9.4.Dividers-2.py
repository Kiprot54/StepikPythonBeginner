import ifnumber

print('Делители-1')
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
print()
for i in range(1, n + 1):
    print(i, end='')
    for j in range(1, i + 1):
        if i % j == 0:
            print('+', end='')
    print()
