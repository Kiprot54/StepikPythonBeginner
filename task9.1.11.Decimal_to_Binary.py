import ifnumber

print('Decimal to Binary')
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
n1 = n
binary_number = ''
while n != 0:
    m = n % 2
    n = n // 2
    binary_number = str(m) + binary_number
print(f'Число {n1} в двоичной системе счисления равно {binary_number}')
