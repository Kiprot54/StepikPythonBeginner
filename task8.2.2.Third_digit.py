import ifnumber

print('Третья цифра')
print()

while True:
    n = input('Введи целое положительное число больше 99: ')
    if_number = ifnumber.if_number(n)
    if if_number == 'int' and int(n) > 99:
        n = int(n)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное число больше 99')
        print()
print()
n1 = n
while n > 999:
    n //= 10
m = n % 10
print(f'Третья цифра числа {n1} равна {m}')
