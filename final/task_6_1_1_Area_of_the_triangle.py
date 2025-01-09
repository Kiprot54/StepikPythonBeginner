print('Площадь треугольника')
print()
while True:
    a = input('Введи первый катет прямоугольного треугольника: ')
    if a.isdigit():
        a = int(a)
        break
    else:
        print('Нужно ввести целое число')
        print()
while True:
    b = input('Введи второй катет прямоугольного треугольника: ')
    if b.isdigit():
        b = int(b)
        break
    else:
        print('Нужно ввести целое число')
        print()
print()
print(f'Площадь прямоугольного треугольника с катетами {a} и {b} равна {1 / 2 * a * b}')
