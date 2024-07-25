import ifnumber

print('Звёздный треугольник')
print()

while True:
    m = input('Введи стартовое количество организмов: ')
    if_number = ifnumber.if_number(m)
    if if_number == 'int':
        m = int(m)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное число')
    print()
while True:
    p = input('Введи среднесуточное увеличение организмов: ')
    if_number = ifnumber.if_number(p)
    if if_number == 'int':
        p = int(p)
        break
    elif if_number == 'float':
        p = float(p)
        break
    else:
        print('Данные введены некорректно! Нужно ввести положительное число')
    print()
while True:
    n = input('Введи количество дней наблюдения: ')
    if_number = ifnumber.if_number(n)
    if if_number == 'int' and int(n) != 0:
        n = int(n)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное число')
    print()
print()

for i in range(1, n + 1):
    print(f'В {i}-ый день будет {m * (1 + p / 100) ** (i - 1)} организмов')

