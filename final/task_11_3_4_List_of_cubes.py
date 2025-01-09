import ifnumber

print('Список кубов')
print()

while True:
    num = input('Сколько чисел будет введено? ')
    if_number = ifnumber.if_number(num)
    if if_number == 'int' and int(num) > 0:
        num = int(num)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное число')
        print()

print()
lst = []
for i in range(1, num + 1):
    while True:
        n = input(f'Введи {i}-е целое число: ')
        if_number = ifnumber.if_number(n)
        if if_number == 'int':
            n = int(n)
            break
        else:
            print('Данные введены некорректно! Нужно ввести целое число')
            print()
    lst.append(n ** 3)
print(lst)
