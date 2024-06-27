print('Римские цифры')
print()
while True:
    n = input('Введи целое число: ')
    if n.isdigit():
        n = int(n)
        break
    else:
        print('Нужно ввести целое число')
        print()
print()
if n % 2 != 0:
    print('YES')
else:
    if 2 <= n <= 5 or 20 < n:
        print('NO')
    elif 6 <= n <= 20:
        print('YES')