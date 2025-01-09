print('Двузначное число')
print()

while True:
    n = input('Введи целое двузначное число: ')
    if n.isdigit() and 10 <= int(n) <= 99:
        n = int(n)
        break
    else:
        print('Нужно ввести целое двузначное число')
        print()
print()
print(f'Число: {n}')
print(f'Единицы: {n % 10}')
print(f'Десятки: {n // 10}')
