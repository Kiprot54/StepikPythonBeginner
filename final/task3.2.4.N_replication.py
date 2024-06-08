print('Размножение n-ок')
print()
while True:
    n = input('Введи число от 1 до 9: ')
    if n.isdigit() and 1 <= int(n) <= 9:
        n = int(n)
        break
    else:
        print('Нужно ввести число от 1 до 9')
        print()
nn = n * 11
nnn = n * 111
print(f'{n} + {nn} + {nnn} = {n + nn + nnn}')