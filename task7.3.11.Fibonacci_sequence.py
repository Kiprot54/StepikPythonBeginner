import ifnumber

print('Последовательность Фибоначчи')
print()

while True:
    n = input('Введи целое положительное число: ')
    if_number = ifnumber.if_number(n)
    if if_number == 'int' and int(n) > 0:
        n = int(n)
        print()
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное число')
    print()
a = 0
b = 1

for i in range(1, n + 1):
    b = a + b
    a = b - a

    print(a, end=' ')
