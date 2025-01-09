print('Цифра 1')
print()

while True:
    s = input('Введи число: ').strip()
    if len(s) == 0:
        print('Строка не должна быть пустой')
        print()
        continue
    if not s.isdigit():
        print('Нужно ввести число')
        continue
    else:
        break
print()
n = int(s)
total = 0
while n != 0:
    m = n % 10
    total += m
    n //= 10
print(f'Сумма цифр числа {s} равна {total}')
