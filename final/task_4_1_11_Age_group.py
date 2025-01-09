print('Возрастная группа')
print()
while True:
    age = input('Введи свой возраст: ')
    if age.isdigit():
        age = int(age)
        break
    else:
        print('Нужно ввести целое положительное число')
        print()
print()
if age <= 13:
    print('Ты ещё ребёнок')
elif 14 <= age <= 24:
    print('Ты молодой человек')
elif 25 <= age <= 59:
    print('Ты зрелый человек')
else:
    print('Ты старик')
