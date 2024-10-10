import ifnumber

print('Список делителей')
print()

while True:
    n = input('Введи целое положительное число: ')
    if_number = ifnumber.if_number(n)
    if if_number == 'int':
        n = int(n)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное число')
        print()

print()
lst = []
for i in range(1, n + 1):
    if n % i == 0:
        lst.append(i)
print(lst)
