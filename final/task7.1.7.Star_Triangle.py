import ifnumber

print('Звёздный треугольник')
print()

while True:
    n = input('Введи целое положительное число больше 1: ')
    if_number = ifnumber.if_number(n)
    if if_number == 'int' and int(n) >= 2:
        n = int(n)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное число больше 1')
    print()

print()
for i in range(n, 0, -1):
    print('*' * i)
