import ifnumber

print('Одинаковые цифры')
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

print()
n1 = n
last_digit = n % 10
n //= 10
flag = True
while n != 0:
    m = n % 10
    if m != last_digit:
        flag = False
        break
    n //= 10
if flag:
    print(f'В числе {n1} все цифры одинаковые')
else:
    print(f'В числе {n1} не все цифры одинаковые')
