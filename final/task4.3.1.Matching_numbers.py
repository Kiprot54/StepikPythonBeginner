print('Совпадающие числа')
print()
while True:
    n1 = input('Введи первое число: ')
    if n1.isdigit():
        n1 = int(n1)
        break
    else:
        print('Нужно ввести целое число')
        print()
while True:
    n2 = input('Введи второе число: ')
    if n2.isdigit():
        n2 = int(n2)
        break
    else:
        print('Нужно ввести целое число')
        print()
while True:
    n3 = input('Введи третье число: ')
    if n3.isdigit():
        n3 = int(n3)
        break
    else:
        print('Нужно ввести целое число')
        print()
print()
counter = 0
if n1 == n2:
    counter += 1
if n1 == n3:
    counter += 1
if n2 == n3:
    counter += 1
if counter == 1:
    counter += 1
print(f'Из чисел {n1}, {n2} и {n3} совпадающих - {counter}')
