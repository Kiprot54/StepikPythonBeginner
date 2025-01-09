import ifnumber

print('Без нулей')
print()

total = 1
for i in range(1, 11):
    while True:
        n = input(f'Введи {i}-е число: ')
        if_number = ifnumber.if_number(n)
        if if_number == 'int':
            n = int(n)
            print()
            break
        elif if_number == 'float':
            n = float(n)
            break
        else:
            print('Данные введены некорректно! Нужно ввести число')
        print()
    if n != 0:
        total *= n
print(f'Произведение введённых чисел, отличных от 0, равно {total}')
