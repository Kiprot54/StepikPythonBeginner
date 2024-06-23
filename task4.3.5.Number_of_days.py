print('Количество дней')
print()
while True:
    n = input('Введи номер месяца: ')
    if n.isdigit() and 1 <= int(n) <= 12:
        n = int(n)
        break
    else:
        print('Нужно ввести целое число от 1 до 12')
        print()
print() # 31 * 8, 30 * 4
if n == 1 or n == 3 or n == 5 or n == 7 or n == 8 or n == 10 or n == 12:
    print(f'В месяце под номером {n} - {31} дней')
elif n == 2:
    print(f'В месяце под номером {n} - {28} дней')
else:
    print(f'В месяце под номером {n} - {30} дней')



