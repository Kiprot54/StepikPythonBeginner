print('Пароль')
print()
password = input('Введи пароль: ')
repassword = input('Подтверди пароль: ')
print()
if repassword == password:
    print('Пароль принят')
else:
    print('Пароль не принят')
