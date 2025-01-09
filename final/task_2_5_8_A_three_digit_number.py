print('Трёхзначное число')
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
print(abc // 100, abc // 10 % 10, abc % 10, sep=', ')
