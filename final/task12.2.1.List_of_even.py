import ifnumber

print('Список чётных')
print()

while True:
    num = input('Введи чётное число, не меньше 2: ')
    if_number = ifnumber.if_number(num)
    if if_number == 'int' and int(num) >= 2:
        num = int(num)
        break
    else:
        print('Данные введены некорректно! Нужно ввести чётное число, не меньше 2')
        print()
print()

print([i for i in range(2, num + 1) if i % 2 == 0])