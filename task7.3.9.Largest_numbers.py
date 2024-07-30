import ifnumber

print('Наибольшие числа')
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
max_first_num = 0
max_second_num = 0
for i in range(n):
    while True:
        m = input('Введи целое положительное число: ')
        if_number = ifnumber.if_number(m)
        if if_number == 'int' and int(m) > 0:
            m = int(m)
            print()
            break
        else:
            print('Данные введены некорректно! Нужно ввести целое положительное число')
        print()
    if max_first_num < m:
        max_second_num = max_first_num
        max_first_num = m
    elif max_second_num < m:
        max_second_num = m
print(f'Среди введённых чисел первое максимальное - {max_first_num}')
print(f'Среди введённых чисел второе максимальное - {max_second_num}')
