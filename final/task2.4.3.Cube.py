print('Куб')
print()
while True:
    a = input('Введи длину ребра куба: ')
    if a.isdigit():
        a = int(a)
        break
    else:
        print('Нужно ввести целое положительное число')
        print()

print()
print('Объём куба =', a * a * a)
print('Площадь полной поверхности куба =', 6 * a * a)
