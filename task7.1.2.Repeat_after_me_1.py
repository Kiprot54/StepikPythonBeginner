import ifnumber
print('Повторяй за мной 1')
print()
s = input('Введи строку: ')
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
for _ in range(num):
    print(s)
