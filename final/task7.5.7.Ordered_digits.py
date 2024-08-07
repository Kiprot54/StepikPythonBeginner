import ifnumber

print('Упорядоченные цифры')
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
flag = True
n1 = n
while n > 9:
    m = n % 10
    k = n % 100 // 10
    if m > k:
        flag = False
        break
    n //= 10

if flag:
    print(f'Цифры в числе {n1} упорядочены по неубыванию')
else:
    print(f'Цифры в числе {n1} не упорядочены по неубыванию')
