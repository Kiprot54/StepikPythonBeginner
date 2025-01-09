import ifnumber

print('Все вместе')
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
total = 0
counter = 0
mult = 1
last_digit = n % 10
while n != 0:
    m = n % 10
    total += m
    counter += 1
    mult *= m
    first_digit = n
    n //= 10
middle_ariph = total / counter

print(f'Сумма цифр числа {n1} равна {total}')
print(f'Количество цифр в числе {n1} равно {counter}')
print(f'Произведение цифр числа {n1} равно {mult}')
print(f'Среднее арифметическое цифр числа {n1} равно {middle_ariph}')
print(f'Первая цифра числа {n1} равна {first_digit}')
print(f'Сумма первой и последней цифр числа {n1} равна {first_digit + last_digit}')
