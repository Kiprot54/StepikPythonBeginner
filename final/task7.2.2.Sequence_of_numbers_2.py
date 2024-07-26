import ifnumber

print('Последовательность чисел 2')
print()
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

if m < n:
    for i in range(m, n + 1):
        print(i)
else:
    for i in range(m, n - 1, -1):
        print(i)
