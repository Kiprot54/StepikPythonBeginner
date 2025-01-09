import ifnumber

print('max и min')
print()

while True:
    n = input('Введи целое положительное число не меньше 10: ')
    if_number = ifnumber.if_number(n)
    if if_number == 'int' and int(n) >= 10:
        n = int(n)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное число не меньше 10')
        print()

print()
n1 = n
m = n % 10
max_n = m
min_n = m
while n != 0:
    m = n % 10
    if m > max_n:
        max_n = m
    elif m < min_n:
        min_n = m
    n //= 10
print(f'Максимальная цифра числа {n1} равна {max_n}')
print(f'Минимальная цифра числа {n1} равна {min_n}')