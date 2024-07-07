print('Корректный email')
print()
email = input('Введи емайл: ')

if ('@' in email and '.' in email) and email.count('@') == 1:
    print(f'Емайл <{email}> корректный')
else:
    print(f'Введён не корректный емайл')
