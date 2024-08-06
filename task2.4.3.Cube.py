import ifnumber

print('Куб')
print()

while True:
    a = input('Введи длину ребра куба: ')
    if_number = ifnumber.if_number(a)
    if if_number == 'int' and int(a) > 0:
        a = int(a)
        print()
        break
    elif if_number == 'float' and float(a) > 0:
        a = float(a)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное число')
    print()

print()
print('Объём куба =', a * a * a)
print('Площадь полной поверхности куба =', 6 * a * a)
