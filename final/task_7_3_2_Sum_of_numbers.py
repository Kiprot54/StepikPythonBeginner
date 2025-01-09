import ifnumber

print('Сумма чисел')
print()

while True:
    n = input('Введи целое положительное число: ')
    if_number = ifnumber.if_number(n)
    if if_number == 'int' and int(n) > 0:
        n = int(n)
        print()
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное число')
    print()
total = 0
for i in range(n):
    while True:
        m = input('Введи целое число: ')
        if_number = ifnumber.if_number(m)
        if if_number == 'int':
            m = int(m)
            break
        else:
            print('Данные введены некорректно! Нужно ввести целое число')
        print()
    total += m
print(f'Сумма введенных чисел равна {total}')
