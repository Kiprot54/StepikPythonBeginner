print('Трёхзначное число 2')
print()
while True:
    abc = input('Введи трёхзначное число: ')
    if abc.isdigit() and 100 <= int(abc) <= 999:
        abc = int(abc)
        break
    else:
        print('Нужно ввести положительное трёхзначное число')
        print()
print()
a = abc // 100
b = abc // 10 % 10
c = abc % 10
print(f'Сумма цифр числа {abc} равна {a + b + c}')
print()
print(f'Произведение цифр числа {abc} равно {a * b * c}')
