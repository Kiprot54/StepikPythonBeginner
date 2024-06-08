print('Количество чётных чисел')
print()
counter = 0
while True:
    n1 = input('Введи целое число: ')
    if n1.isdigit() or (n1[0] == '-' and n1[1:].isdigit()):
        n1 = int(n1)
        break
    else:
        print('Нужно ввести целое число')
        print()
while True:
    n2 = input('Введи целое число: ')
    if n2.isdigit() or (n2[0] == '-' and n2[1:].isdigit()):
        n2 = int(n2)
        break
    else:
        print('Нужно ввести целое число')
        print()
while True:
    n3 = input('Введи целое число: ')
    if n3.isdigit() or (n3[0] == '-' and n3[1:].isdigit()):
        n3 = int(n3)
        break
    else:
        print('Нужно ввести целое число')
        print()
print()
if n1 % 2 == 0:
    counter += 1
if n2 % 2 == 0:
    counter += 1
if n3 % 2 == 0:
    counter += 1
print(f'Количество чётных чисел: {counter}')
