import ifnumber

print('')
print()
while True:
    print('Введи 2 целых положительных числа. Первое число меньше второго')
    print()
    while True:
        a = input('Введи первое число: ')
        if_number = ifnumber.if_number(a)
        if if_number == 'int' and int(a) > 0:
            a = int(a)
            break
        else:
            print('Данные введены некорректно! Нужно ввести целое положительное число')
            print()
    while True:
        b = input('Введи второе число: ')
        if_number = ifnumber.if_number(b)
        if if_number == 'int' and int(b) > 0:
            b = int(b)
            break
        else:
            print('Данные введены некорректно! Нужно ввести целое положительное число')
            print()
    if a < b:
        break
    else:
        print('Первое число должно быть меньше второго')
        print()
print()
max_total = 0
c = 0
for i in range(a, b + 1):
    total = 0
    for j in range(1, i + 1):
        if i % j == 0:
            total += j
    if total > max_total:
        max_total = total
        c = i
print(f'Из отрезка [{a}, {b}] у числа {c} максимальная сумма делителей. Она равна {max_total}')



