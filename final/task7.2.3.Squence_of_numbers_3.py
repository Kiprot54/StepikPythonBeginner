import ifnumber

print('Последовательность чисел 3')
print()
while True:
    while True:
        m = input('Введи первое целое число: ')
        if_number = ifnumber.if_number(m)
        if if_number == 'int':
            m = int(m)
            print()
            break
        else:
            print('Данные введены некорректно! Нужно ввести целое число')
        print()
    while True:
        n = input('Введи второе целое число: ')
        if_number = ifnumber.if_number(n)
        if if_number == 'int':
            n = int(n)
            print()
            break
        else:
            print('Данные введены некорректно! Нужно ввести целое число')
        print()
    if m > n:
        break
    else:
        print('Первое число должно быть больше второго')

for i in range(m, n - 1, -1):
    if i % 2 != 0:
        print(i)
