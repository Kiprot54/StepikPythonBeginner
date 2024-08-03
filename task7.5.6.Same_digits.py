import ifnumber

print('Одинаковые цифры')
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
    print('Все цифры одинаковые')
else:
    print('Не все цифры одинаковые')
