print('Мандарины')
print()
n, k = 0, 0
while True:
    n = input('Введи количество школьников: ')
    if n.isdigit() and int(n) != 0:
        print()
        break
    else:
        print('Нужно ввести целое положительное число')
        print()
while True:
    k = input('Введи количество мандаринов: ')
    if k.isdigit():
        print()
        break
    else:
        print('Нужно ввести целое положительное число')
        print()

mandarins_in_schoolboy = int(k) // int(n)
mandarins_in_pottle = int(k) % int(n)
print(f'Мандаринов у каждого школьника: {mandarins_in_schoolboy}')
print(f'Осталось мандаринов в корзине: {mandarins_in_pottle}')
