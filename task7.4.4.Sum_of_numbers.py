import ifnumber

print('Сумма чисел')
print()
total = 0
while True:
    while True:
        n = input('Введи число: ')
        if_number = ifnumber.if_number(n)
        if if_number == 'int':
            n = int(n)
            break
        else:
            print('Данные введены некорректно! Нужно ввести число')
        print()
    if n > 0:
        total += n
    else:
        break
print(total)