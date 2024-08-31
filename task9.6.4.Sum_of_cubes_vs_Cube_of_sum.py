import ifnumber

print('Сумма кубов vs Куб суммы')
print()

while True:
    a = input('Введи первое целое число: ')
    if_number = ifnumber.if_number(a)
    if if_number == 'int':
        a = int(a)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое число')
        print()
while True:
    b = input('Введи второе целое число: ')
    if_number = ifnumber.if_number(b)
    if if_number == 'int':
        b = int(b)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое число')
        print()
print()
sum_cube = a ** 3 + b ** 3
cube_sum = (a + b) ** 3
print(f'Для чисел {a} и {b}:')
print(f'  Сумма кубов: {a}**3 + {b}**3 = {sum_cube}')
print(f'  Куб суммы: ({a} + {b})**3 = {cube_sum}')
