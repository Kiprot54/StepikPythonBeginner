import ifnumber

print('Суммы двух')
print()

while True:
    num = input('Введи целое число больше 1: ')
    if_number = ifnumber.if_number(num)
    if if_number == 'int' and int(num) >= 2:
        num = int(num)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое число больше 1')
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

lst_sum = []
for i in range(len(lst) - 1):
    n_sum = lst[i] + lst[i + 1]
    lst_sum.append(n_sum)
print(lst_sum)
