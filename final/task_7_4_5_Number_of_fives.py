import ifnumber

print('Количество пятерок')
print()

counter = 0
while True:
    while True:
        n = input('Введи целое число: ')
        if_number = ifnumber.if_number(n)
        if if_number == 'int':
            n = int(n)
            print()
            break
        else:
            print('Данные введены некорректно! Нужно ввести целое число')
        print()
    if 1 <= n <= 5:
        if n == 5:
            counter += 1
    else:
        break
print(f'Среди введённых чисел {counter} пятёрок')
