import ifnumber

print('Сумма чисел 2')
print()

while True:
    n = input('Введи целое положительное число: ')
    if_number = ifnumber.if_number(n)
    if if_number == 'int':
        n = int(n)
        print()
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное число')
    print()
total = 0
for i in range(1, n + 1):
    last_digit = i ** 2 % 10
    if last_digit == 2 or last_digit == 5 or last_digit == 8:
        total += i
print(f'Сумма введённых чисел, квадрат которых оканчивается на 2, 5 или 8, равна {total}')
