print('Четырёхзначное число')
print()
while True:
    abcd = input('Введи положительное четырёхзначное число: ')
    if abcd.isdigit() and 1000 <= int(abcd) <= 9999:
        abcd = int(abcd)
        break
    else:
        print('Нужно ввести положительное четырёхзначное число')
        print()
print()
a = abcd // 1000
b = abcd // 100 % 10
c = abcd // 10 % 10
d = abcd % 10
print(f'Цифра в позиции тысяч равна {a}')
print(f'Цифра в позиции сотен равна {b}')
print(f'Цифра в позиции десятков равна {c}')
print(f'Цифра в позиции единиц равна {d}')
