print('Двузначное число 2')
print()

while True:
    n = input('Введи целое положительное двузначное число: ')
    if n.isdigit() and 10 <= int(n) <= 99:
        n = int(n)
        break
    else:
        print('Нужно ввести целое положительное двузначное число')
        print()
print()
first_digit = n % 10
last_digit = n // 10
print(f'Сумма цифр числа {n} равна {first_digit + last_digit}')
