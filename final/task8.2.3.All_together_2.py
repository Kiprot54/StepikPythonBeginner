import ifnumber

print('Все вместе 2')
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
last_digit = n % 10
counter_3 = 0
counter_last_digit = 0
counter_even_digit = 0
counter_05 = 0
total = 0
mult = 1
while n != 0:
    m = n % 10
    if m == 3:
        counter_3 += 1
    if m == last_digit:
        counter_last_digit += 1
    if m % 2 == 0:
        counter_even_digit += 1
    if m > 5:
        total += m
    if m > 7:
        mult *= m
    if m == 0 or m == 5:
        counter_05 += 1
    n //= 10
print(f'В числе {n1}:')
print(f'<{counter_3}> цифр 3;')
print(f'последняя цифра {last_digit} встречается <{counter_last_digit}> раз;')
print(f'количество чётных цифр - <{counter_even_digit}>;')
print(f'сумма его цифр, больших 5, равна <{total}>;')
if mult == 1:
    print('цифр больше 7 нет')
else:
    print(f'произведение цифр, больших 7, равно <{mult}>;')
print(f'<{counter_05}> цифр 0 и 5.')
