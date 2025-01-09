print('Girls only')
print()
while True:
    age = input('Введи свой возраст: ')  # 14
    if age.isdigit() and int(age) != 0:
        age = int(age)
        break
    else:
        print('Нужно ввести целое положительное число')
        print()
while True:
    gender = input('Введи свой пол: ')  # m
    gender = gender.lower()
    if gender == 'm' or gender == 'f':
        break
    else:
        print('Надо ввести f (девочка) или m (мальчик)')
print()
if 10 <= age <= 15 and gender == 'f':
    print('Ты нам подходишь')
else:
    print('Ты нам не подходишь')