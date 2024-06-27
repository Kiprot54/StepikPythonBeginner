print('Цвета колеса рулетки')
print()
while True:
    n = input('Введи номер рулетки: ')
    if n.isdigit():
        n = int(n)
        break
    else:
        print('Нужно ввести целое положительное число от 0 до 36')
        print()
print()
if n == 0:
    print(f'Карман рулетки зеленый')
elif 1 <= n <= 10:
    if n % 2 != 0:
        print(f'Карман рулетки красный')
    else:
        print(f'Карман рулетки черный')
elif 11 <= n <= 18:
    if n % 2 != 0:
        print(f'Карман рулетки черный')
    else:
        print(f'Карман рулетки красный')
elif 19 <= n <= 28:
    if n % 2 != 0:
        print(f'Карман рулетки красный')
    else:
        print(f'Карман рулетки черный')
elif 29 <= n <= 36:
    if n % 2 != 0:
        print(f'Карман рулетки черный')
    else:
        print(f'Карман рулетки красный')
else:
    print('На рулетке нет такого числа')
