import ifnumber

print('Вторая цифра')
print()

while True:
    n = input('Введи целое положительное число больше 9: ')
    if_number = ifnumber.if_number(n)
    if if_number == 'int' and int(n) > 9:
        n = int(n)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное число больше 9')
        print()

print()
n1 = n
while n > 9:
    m = n % 10
    n //= 10
print(f'Вторая цифра числа {n1} равна {m}')
