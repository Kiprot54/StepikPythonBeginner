import ifnumber

print('Квадрат числа')
print()

while True:
    num = input('Введи целое положительное число: ')
    if_number = ifnumber.if_number(num)
    if if_number == 'int' and int(num) > 0:
        num = int(num)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное число')
    print()

print()
for i in range(num + 1):
    print(f'Квадрат числа {i} равен {i ** 2}')
