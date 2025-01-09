print('Сортировка трех')
print()
n1 = float(input('Введи первое число: '))
n2 = float(input('Введи второе число: '))
n3 = float(input('Введи третье число: '))
if n1 > n2:
    max_n = n1
    min_n = n2
else:
    max_n = n2
    min_n = n1
if n3 > max_n:
    middle_n = max_n
    max_n = n3
elif n3 < min_n:
    middle_n = min_n
    min_n = n3
else:
    middle_n = n3
print(f'{max_n}, {middle_n}, {min_n}')