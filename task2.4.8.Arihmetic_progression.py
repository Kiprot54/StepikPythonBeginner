print('Арифметическая прогрессия')
print()
while True:
    a1 = input('Введи первый член арифметической прогрессии: ')
    if a1.isdigit() or (a1[0] == '-' and a1[1:].isdigit()):
        a1 = int(a1)
        break
    else:
        print('Нужно ввести целое число')
        print()
while True:
    d = input('Введи разность арифметической прогрессии: ')
    if d.isdigit() or (d[0] == '-' and d[1:].isdigit()):
        d = int(d)
        break
    else:
        print('Нужно ввести целое число')
        print()
while True:
    n = input('Какой член арифметической прогрессии нужно найти? ')
    if n.isdigit() and int(n) > 1:
        print(f'{n}-й член арифметической прогрессии:', a1 + d * (int(n) - 1))
        break
    else:
        print('Нужно ввести целое число, большее 1')
        print()
