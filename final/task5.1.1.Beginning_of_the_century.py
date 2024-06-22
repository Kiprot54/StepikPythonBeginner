print('Начало столетия')
print()
while True:
    year = input('Введи год: ')  # 2024 2000
    if year.isdigit():
        year = int(year)
        break
    else:
        print('Нужно ввести целое положительное число')
        print()
print()
# if year[-2:] == '00':
if year % 100 == 0:
    print(f'{year} год является началом столетия')
else:
    print(f'{year} год не является началом столетия')