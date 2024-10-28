import ifnumber

print('Remove outliers')
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
print(f'Введи {n} различных чисел')
for i in range(1, n + 1):
    while True:
        num = input('Введи целое положительное число: ')
        if_number = ifnumber.if_number(num)
        if if_number == 'int' and int(num) > 0:
            num = int(num)
            if not numbers.count(num):
                break
            else:
                print('Такое число ты уже вводил')
        else:
            print('Данные введены некорректно! Нужно ввести целое положительное число')
            print()
    numbers.append(num)
max_num = max(numbers)
min_num = min(numbers)
for i in range(len(numbers)):
    if numbers[i] == max_num:
        del numbers[i]
        break
for i in range(len(numbers)):
    if numbers[i] == min_num:
        del numbers[i]
        break

print(*numbers, sep='\n')
