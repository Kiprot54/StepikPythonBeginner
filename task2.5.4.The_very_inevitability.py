print('Сама неотвратимость')
print()
while True:
    n = input('Сколько населения во Вселенной? ')
    print()
    if n.isdigit():
        k = int(n)
        m = k // 2
        if k % 2 != 0:
            m += 1
        print(f'Останется выжившим населения: {m}')
        break
    else:
        print('Нужно ввести положительное целое число')
