print('Високосный год')
print()
while True:
    year = input('Введи год: ')
    if year.isdigit():
        year = int(year)
        break
    else:
        print('Нужно ввести целое положительное число')
        print()
print()
if (year % 4 == 0 and not year % 100 == 0) or (year % 400 == 0):
    print(f'Год {year} является високосным')
else:
    print(f'Год {year} не является високосным')