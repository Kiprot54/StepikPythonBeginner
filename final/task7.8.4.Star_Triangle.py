import ifnumber

print('Звёздный треугольник')
print()

while True:
    n = input('Введи целое положительное нечётное число: ')
    if_number = ifnumber.if_number(n)
    if if_number == 'int' and int(n) > 0 != int(n) % 2:
        n = int(n)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное нечётное число')
        print()
print()
for i in range(1, n // 2 + 2):
    for j in range(i):
        print('*', end='')
    print()
for i in range(n // 2, -1, -1):
    for j in range(i):
        print('*', end='')
    print()
