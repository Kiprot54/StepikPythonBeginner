print('Геометрическая прогрессия')
print()
while True:
    b1 = input('Введи первый член геометрической прогрессии: ')
    if b1.isdigit() or (b1[0] == '-' and b1[1:].isdigit()):
        b1 = int(b1)
        break
    else:
        print('Нужно ввести целое число')
        print()

while True:
    q = input('Введи знаменатель геометрической прогрессии: ')
    if (q.isdigit() or (q[0] == '-' and q[1:].isdigit())) and int(q) != 0:
        q = int(q)
        break
    else:
        print('Нужно ввести целое число, не равное нулю')
        print()

while True:
    n = input('Какой член геометрической прогрессии нужно найти? ')
    if n.isdigit() and int(n) > 1:
        print(f'{n}-й член геометрической прогрессии:', b1 * q ** (int(n) - 1))
        break
    else:
        print('Нужно ввести целое положительное число')
        print()
