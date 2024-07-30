import ifnumber

print('Only even numbers')
print()
counter = 0
for i in range(10):
    while True:
        n = input('Введи число: ')
        if_number = ifnumber.if_number(n)
        if if_number == 'int':
            n = int(n)
            break
        elif if_number == 'float':
            n = float(n)
            break
        else:
            print('Данные введены некорректно! Нужно ввести число')
        print()
    if n % 2 == 0:
        counter += 1
    print()
if counter == 10:
    print('Все числа чётные')
else:
    print('Не все числа являются чётными')
