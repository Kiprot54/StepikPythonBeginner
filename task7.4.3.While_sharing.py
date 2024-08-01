import ifnumber

print('Пока делимся')
print()

while True:
    while True:
        n = input('Введи число: ')
        if_number = ifnumber.if_number(n)
        if if_number == 'int':
            n = int(n)
            break
        else:
            print('Данные введены некорректно! Нужно ввести число')
        print()
    if n % 7 == 0:
        print(n)
    else:
        break

