import ifnumber

print('Цифровой корень')
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
while n > 9:
    total = 0
    while n != 0:
        m = n % 10
        total += m
        n //= 10
    n = total
print(f'Цифровой корень числа {n1} равен {n}')
