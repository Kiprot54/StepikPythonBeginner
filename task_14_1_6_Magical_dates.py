print('Магические даты')
print()

def is_magic(date):
    numbers = date.split('.')
    num = int(numbers[0])
    month = int(numbers[1])
    year = int(numbers[2])
    return num * month == year % 100

def get_date():
    while True:
        s = input('Введи дату в формате dd.mm.yyyy: ')
        if len(s.strip()) == 0:
            print('Строка не должна быть пустой')
            print()
        else:
            lst = s.split('.')
            if lst[0].isdigit() or lst[1].isdigit() or lst[2].isdigit():
                print('Нужно ввести строковое представление корректной даты')
                print()
            else:
                return s

s = get_date()

print(is_magic(s))

# Неправильная проверка