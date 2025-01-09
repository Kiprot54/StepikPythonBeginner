import ifnumber

print('Negatives, Zeros and Positives')
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
positive_numbers = []
negative_numbers = []
zero_numbers = []
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
    if num > 0:
        positive_numbers.append(num)
    elif num < 0:
        negative_numbers.append(num)
    else:
        zero_numbers.append(num)

print()
print(f'Среди введённых чисел', *numbers)
print()
print('отрицательные числа:')
print(*negative_numbers, sep='\n')
print('нули:')
print(*zero_numbers, sep='\n')
print(f'положительные числа:')
print(*positive_numbers, sep='\n')
