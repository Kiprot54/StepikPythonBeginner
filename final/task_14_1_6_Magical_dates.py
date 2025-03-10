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
            if len(lst) == 3 and lst[0].isdigit() and lst[1].isdigit() and lst[2].isdigit():
                if len(lst[0]) == 2 and len(lst[1]) == 2 and len(lst[2]) == 4:
                    return s
                else:
                    print('Нужно ввести дату в формате dd.mm.yyyy')
                    print()
            else:
                print('Нужно ввести дату в формате dd.mm.yyyy')
                print()

date = get_date()

print(is_magic(date))

