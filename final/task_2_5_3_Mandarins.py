print('Мандарины')
print()

while True:
    n = input('Введи количество школьников: ')
    if n.isdigit() and int(n) != 0:
        break
    else:
        print('Нужно ввести целое положительное число')
        print()
while True:
    k = input('Введи количество мандаринов: ')
    if k.isdigit():
        break
    else:
        print('Нужно ввести целое положительное число')
        print()

mandarins_in_schoolboy = int(k) // int(n)
mandarins_in_pottle = int(k) % int(n)
print()
print(f'Мандаринов у каждого школьника: {mandarins_in_schoolboy}')
print(f'Осталось мандаринов в корзине: {mandarins_in_pottle}')
