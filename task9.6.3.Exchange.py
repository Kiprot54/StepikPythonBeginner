import ifnumber
print('Курсы валют')
print()
while True:
    date = input('Введи дату в формате ДД-ММ-ГГГГ: ')
    if len(date) == 10:
        date_num = date[0:1] + date[3:4] + date[6:]
        if date_num.isdigit() and date[2] == '-' and date[5] == '-':
            break
        else:
            print('Данные введены некорректно! Нужно ввести дату в формате ДД-ММ-ГГГГ')
    else:
        print('Данные введены некорректно! Нужно ввести дату в формате ДД-ММ-ГГГГ')
        print()
while True:
    dollar = input('Введи курс доллара: ')
    if_number = ifnumber.if_number(dollar)
    if if_number == 'int' and int(dollar) > 0:
        dollar = int(dollar)
        break
    elif if_number == 'float' and float(dollar) > 0:
        dollar = float(dollar)
        break
    else:
        print('Данные введены некорректно! Нужно ввести положительное число')
        print()
while True:
    yuan = input('Введи курс юаня: ')
    if_number = ifnumber.if_number(yuan)
    if if_number == 'int' and int(yuan) > 0:
        yuan = int(yuan)
        break
    elif if_number == 'float' and float(yuan) > 0:
        yuan = float(yuan)
        break
    else:
        print('Данные введены некорректно! Нужно ввести положительное число')
        print()
print(f'Курс валют на {date}: 1$ = {dollar}₽, 1¥ = {yuan}₽')