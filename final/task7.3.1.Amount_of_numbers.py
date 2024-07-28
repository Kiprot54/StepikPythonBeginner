import ifnumber

print('Количество чисел')
print()

while True:
    while True:
        a = input('Введи целое число - начало диапазона: ')
        if_number = ifnumber.if_number(a)
        if if_number == 'int':
            a = int(a)
            print()
            break
        else:
            print('Данные введены некорректно! Нужно ввести целое число')
        print()
    while True:
        b = input('Введи целое число - конец диапазона: ')
        if_number = ifnumber.if_number(b)
        if if_number == 'int':
            b = int(b)
            print()
            break
        else:
            print('Данные введены некорректно! Нужно ввести целое число')
        print()
    if a <= b:
        break
    else:
        print('Второе число должно быть не меньше первого')
    print()
counter = 0
for i in range(a, b + 1):
    last_number = i ** 3 % 10
    if last_number == 4 or last_number == 9:
        counter += 1
print(f'Количество чисел в диапазоне [{a}; {b}], куб которых оканчивается на 4 или 9, равно {counter}')
