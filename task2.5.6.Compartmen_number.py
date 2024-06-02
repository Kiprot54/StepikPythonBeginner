print('Номер купе')
print()
while True:
    n = input('Введи номер места в поезде: ')
    print()
    if n.isdigit() and 1 <= int(n) <= 36:
        n = int(n)
        coupe = n // 4 + 1
        if n % 4 == 0:
            coupe -= 1
        print(f'Место {n} находится в {coupe} купе')
        break
    else:
        print('Нужно ввести целое положительное число меньше 37')
        print()