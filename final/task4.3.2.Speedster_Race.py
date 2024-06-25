print('Гонка спидстеров')
print()
while True:
    n = input('Введи скорость Зума: ')
    if n.isdigit():
        n = int(n)
        break
    else:
        print('Нужно ввести целое положительное число')
        print()
while True:
    k = input('Введи скорость Флэша: ')
    if k.isdigit():
        k = int(k)
        break
    else:
        print('Нужно ввести целое положительное число')
        print()
print()
if k == n:
    print('Не знаю')
elif n < k:
    print('Можно принимать вызов Зума')
else:
    print('Лучше не рисковать')
