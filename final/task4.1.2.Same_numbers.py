print('Одинаковые цифры')
print()
while True:
    ab = input('Введи двузначное положительное число: ')
    if ab.isdigit() and 10 <= int(ab) <= 99:
        break
    else:
        print('Нужно ввести двузначное положительное число')
        print()
print()
a = ab[0]
b = ab[1]
if a == b:
    print(f'Число {ab} состоит из одинаковых цифр')
else:
    print(f'Число {ab} состоит из не одинаковых цифр')