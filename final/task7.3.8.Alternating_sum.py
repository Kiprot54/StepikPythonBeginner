import ifnumber

print('Знакочередующаяся сумма')
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
# for i in range(1, n + 1):
    # if i % 2 != 0:
    #     total += i
    # else:
    #     total -= i
if n % 2 != 0:
    total = n // 2 + 1
else:
    total = n // (-2)
print(f'Знакочередующуюся сумма от 1 до {n} равна {total}')
