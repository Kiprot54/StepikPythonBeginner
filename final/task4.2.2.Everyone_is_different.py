print('Все разные')
print()
while True:
    abc = input('Введи натуральное трёзначное число: ')
    if abc.isdigit() and 100 <= int(abc) <= 999:
        break
    else:
        print('Нужно ввести натуральное трёзначное число')
        print()
print()
a = abc[0]
b = abc[1]
c = abc[2]
if not a == b and not a == c and not b == c:
    print(f'В числе {abc} все цифры разные')
else:
    print(f'В числе {abc} есть одинаковые цифры')
