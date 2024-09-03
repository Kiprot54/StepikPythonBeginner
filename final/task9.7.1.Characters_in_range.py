import ifnumber

print('Символы в диапазоне')
print()

while True:
    a = input('Введи неотрицательное целое число: ')
    if_number = ifnumber.if_number(a)
    if if_number == 'int' and int(a) > -1:
        a = int(a)
        break
    else:
        print('Данные введены некорректно! Нужно ввести неотрицательное целое число')
        print()

while True:
    b = input('Введи неотрицательное целое число: ')
    if_number = ifnumber.if_number(b)
    if if_number == 'int' and int(b) > -1:
        b = int(b)
        break
    else:
        print('Данные введены некорректно! Нужно ввести неотрицательное целое число')
        print()

print()
for i in range(a, b + 1):
    print(chr(i), end=' ')
