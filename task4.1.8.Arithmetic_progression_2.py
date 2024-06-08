print('Арифметическая прогрессия 2')
print()
while True:
    a1 = input('Введи число: ')
    if a1.isdigit() or (a1[0] == '-' and a1[1:].isdigit()):
        a1 = int(a1)
        break
    else:
        print('Нужно ввести целое положительное число')
        print()
while True:
    a2 = input('Введи число: ')
    if a2.isdigit() or (a2[0] == '-' and a2[1:].isdigit()):
        a2 = int(a2)
        break
    else:
        print('Нужно ввести целое положительное число')
        print()
while True:
    a3 = input('Введи число: ')
    if a3.isdigit() or (a3[0] == '-' and a3[1:].isdigit()):
        a3 = int(a3)
        break
    else:
        print('Нужно ввести целое положительное число')
        print()
print()
if a2 - a1 == a3 - a2:
    print(f'{a1}, {a2}, {a3} - члены арифметической прогрессии')
else:
    print(f'{a1}, {a2}, {a3} - не являются членами арифметической прогрессии')