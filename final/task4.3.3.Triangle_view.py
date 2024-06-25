print('Вид треугольника')
print()
while True:
    n1 = input('Введи первое число: ')
    if n1.isdigit() and n1 != 0:
        n1 = int(n1)
        break
    else:
        print('Нужно ввести целое число')
        print()
while True:
    n2 = input('Введи второе число: ')
    if n2.isdigit() and n2 != 0:
        n2 = int(n2)
        break
    else:
        print('Нужно ввести целое число')
        print()
while True:
    n3 = input('Введи третье число: ')
    if n3.isdigit() and n3 != 0:
        n3 = int(n3)
        break
    else:
        print('Нужно ввести целое число')
        print()
print()
if n1 == n2 == n3:
    print('Треугольник равосторонний')
elif n1 != n2 and n1 != n3 and n2 != n3:
    print('Треугольник разносторонний')
else:
    print('Треугольник равнобедренный')
