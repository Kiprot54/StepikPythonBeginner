print('Двузначное число')
print()

while True:
    n = input('Введи число: ') # 10
    if n.isdigit() and 10 <= int(n) <= 99:
        n = int(n)
        break
    else:
        print('Нужно ввести целое число, большее 9 и меньшее 100')
        print()
print()
print(f'Единицы: {n % 10}')
print(f'Десятки: {n // 10}')
