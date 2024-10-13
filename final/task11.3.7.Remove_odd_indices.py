import ifnumber

print('Удалите нечётные индексы')
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
    lst.append(n)
lst_del = []
for i in range(len(lst)):
    if i % 2 == 0:
        n1 = lst[i]
        lst_del.append(n1)
print(lst_del)
