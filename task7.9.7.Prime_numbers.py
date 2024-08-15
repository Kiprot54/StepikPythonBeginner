import ifnumber

print('Сумма факториалов')
print()

while True:
    while True:
        a = input('Введи первое целое положительное число: ')
        if_number = ifnumber.if_number(a)
        if if_number == 'int' and a != 0:
            a = int(a)
            break
        else:
            print('Данные введены некорректно! Нужно ввести целое положительное число')
            print()
    while True:
        b = input('Введи второе целое положительное число: ')
        if_number = ifnumber.if_number(b)
        if if_number == 'int' and b != 0:
            b = int(b)
            break
        else:
            print('Данные введены некорректно! Нужно ввести целое положительное число')
            print()
    if a < b:
        break
    else:
        print('Первое число должно быть меньше второго')
for i in range(a, b + 1):
    counter = 0
    for j in range(1, i + 1):
        if i % j == 0:
            counter += 1
    if counter == 2:
        print(i)
