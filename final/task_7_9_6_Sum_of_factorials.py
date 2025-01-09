import ifnumber

print('Сумма факториалов')
print()

while True:
    n = input('Введи целое положительное число: ')
    if_number = ifnumber.if_number(n)
    if if_number == 'int' and n != 0:
        n = int(n)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное число')
        print()
print()
total = 0
mult = 1
for i in range(1, n + 1):
    mult *= i
    total += mult
print(f'Сумма факториалов до числа {n} равна {total}')
