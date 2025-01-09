import ifnumber

print('Сумма делителей')
print()

while True:
    n = input('Введи целое положительное число: ')
    if_number = ifnumber.if_number(n)
    if if_number == 'int' and int(n) > 0:
        n = int(n)
        print()
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное число')
    print()
total = 0
for i in range(1, n + 1):
    if n % i == 0:
        total += i
print(f'Сумма всех делителей числа {n} равна {total}')
