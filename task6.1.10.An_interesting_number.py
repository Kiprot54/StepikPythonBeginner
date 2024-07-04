print('Интересное число')
print()
while True:
    abc = input('Введи трёхзначное положительное число: ')
    if abc.isdigit() and 100 <= int(abc) <= 999:
        abc = int(abc)
        break
    else:
        print('Нужно ввести целое трёхзначное положительное число')
        print()
print()
a = abc // 100
b = abc // 10 % 10
c = abc % 10
if a > c:
    max_number = a
    min_number = c
else:
    max_number = c
    min_number = a
if b > max_number:
    middle_number, max_number = max_number, b
elif b < min_number:
    middle_number, min_number = min_number, b
else:
    middle_number = b
if max_number - min_number == middle_number:
    print(f'Разность максимальной и минимальной цифры числа {abc} равна средней цифре этого числа')
else:
    print(f'Разность максимальной и минимальной цифры числа {abc} не равна средней цифре этого числа')
