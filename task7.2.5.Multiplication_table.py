import ifnumber

print('Таблица умножения')
print()
while True:
    n = input('Введи целое положительное число: ')
    if_number = ifnumber.if_number(n)
    if if_number == 'int' and int(n) != 0:
        n = int(n)
        print()
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное число')
    print()
for i in range(1, 10 + 1):
    print(f'{n} x {i} = {n * i}')