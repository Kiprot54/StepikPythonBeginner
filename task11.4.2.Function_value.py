import ifnumber

print('Значение функции')
print()

while True:
    n = input('Сколько чисел будет введено? ')
    if_number = ifnumber.if_number(n)
    if if_number == 'int' and int(n) > 0:
        n = int(n)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное число')
        print()
print()
numbers = []
for i in range(1, n + 1):
    while True:
        num = input(f'Введи {i}-е целое число: ')
        if_number = ifnumber.if_number(num)
        if if_number == 'int':
            num = int(num)
            break
        else:
            print('Данные введены некорректно! Нужно ввести целое число')
            print()
    numbers.append(num)
print(*numbers, sep='\n')
print()
for el in numbers:
    f_x = el ** 2 + el * 2 + 1
    print(f_x)
