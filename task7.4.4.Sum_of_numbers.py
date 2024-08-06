import ifnumber

print('Сумма чисел')
print()

total = 0
while True:
    while True:
        n = input('Введи целое число: ')
        if_number = ifnumber.if_number(n)
        if if_number == 'int':
            n = int(n)
            break
        else:
            print('Данные введены некорректно! Нужно ввести целое число')
        print()
    if n > 0:
        total += n
    else:
        break
print(f'Сумма введённых чисел равна {total}')

# какое число?