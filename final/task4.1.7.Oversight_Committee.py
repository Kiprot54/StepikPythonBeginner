print('Роскомнадзор')
print()
while True:
    year = input('Введи свой возраст: ')
    if year.isdigit():
        year = int(year)
        break
    else:
        print('Нужно ввести свой полный возраст')
        print()
print()
if year > 18:
    print('Доступ разрешен')
else:
    print('Доступ запрещён')
