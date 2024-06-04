print('Следующее и предыдущее')
print()
while True:
    n = input('Введи целое число: ')
    if n.isdigit() or (n[0] == '-' and n[1:].isdigit()):
        n = int(n)
        break
    else:
        print('Нужно ввести целое число')
        print()
print()
print(f'Следующее за числом {n} число: {n + 1}')
print(f'Для числа {n} предыдущее число: {n - 1}')
