import ifnumber

print('Численный треугольник 2')
print()

while True:
    n = input('Введи целое положительное число: ')
    if_number = ifnumber.if_number(n)
    if if_number == 'int' and int(n) > 0:
        n = int(n)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное число')
        print()
counter = 1
print()
for i in range(1, n + 1):
    for j in range(i):
        print(counter, end=' ')
        counter += 1
    print()
