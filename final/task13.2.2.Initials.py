print('ФИО')
print()

def print_fio(name, surname, patronymic):
    print(surname[0].upper() + name[0].upper() + patronymic[0].upper())

while True:
    name = input('Введи имя: ')
    if len(name.strip()) == 0:
        print('Имя не должно быть пустой')
        print()
    else:
        break
print()
while True:
    surname = input('Введи фамилию: ')
    if len(surname.strip()) == 0:
        print('Фамилия не должна быть пустой')
        print()
    else:
        break
print()
while True:
    patronymic = input('Введи отчество: ')
    if len(patronymic.strip()) == 0:
        print('Отчество не должно быть пустой')
        print()
    else:
        break
print()

print_fio(name, surname, patronymic)