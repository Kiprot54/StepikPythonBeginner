print('Римские цифры')
print()
while True:
    n = input('Введи целое число от 1 до 10: ')
    if n.isdigit() and 1 <= int(n) <= 10:
        n = int(n)
        break
    else:
        print('Нужно ввести целое число от 1 до 10')
        print()
print()
if n == 1 or n == 2 or n == 3:
    print('I' * n)
elif n == 4:
    print('I' + 'V')
elif 5 <= n <= 8:
    print('V' + 'I' * (n - 5))
elif 9 <= n <= 10:
    print('I' * (10 - n) + 'X')
