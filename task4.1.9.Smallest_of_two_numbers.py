print('')
print()
while True:
    n1 = input('Введи число: ')
    if n1.isdigit() or (n1[0] == '-' and n1[1:].isdigit()):
        n1 = int(n1)
        break
    else:
        print('Нужно ввести целое положительное число')
        print()
while True:
    n2 = input('Введи число: ')
    if n2.isdigit() or (n2[0] == '-' and n2[1:].isdigit()):
        n2 = int(n2)
        break
    else:
        print('Нужно ввести целое положительное число')
        print()
print()
if n1 < n2:
    print(f'Наименьшее из чисел {n1} и {n2} - {n1}')
else:
    print(f'Наименьшее из чисел {n1} и {n2} - {n2}')
