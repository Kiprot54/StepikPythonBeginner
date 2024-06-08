print('Чётное или нечётное?')
print()
while True:
    n = input('Введи число: ')
    if n.isdigit() or (n[0] == '-' and n[1:].isdigit()):
        n = int(n)
        break
    else:
        print('Нужно ввести целое положительное число')
        print()
print()
if n % 2 == 0:
    print(f'Число {n} чётное')
else:
    print(f'Число {n} нечётное')