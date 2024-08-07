import ifnumber

print('Обратный порядок 2')
print()

while True:
    n = input('Введи целое положительное число: ')
    if_number = ifnumber.if_number(n)
    if if_number == 'int' and int(n) > 0:
        n = int(n)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное число')
    print()

print()
while n != 0:
    m = n % 10
    n //= 10
    print(m, end='')
