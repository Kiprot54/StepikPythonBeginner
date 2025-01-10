print('Количество дней')
print()

def get_days(month):
    month31 = [1, 3, 5, 7, 8, 10, 12]
    month30 = [4, 6, 9, 11]
    month28 = [2]
    if month.isdigit():
        month = int(month)
        if month in month31:
            return 31
        elif month in month30:
            return 30
        elif month in month28:
            return 28
        else:
            return 'Номер месяца введён некорректно'
    else:
        return 'Номер месяца введён некорректно'

def get_month():
    num = input('Введи номер месяца: ')
    return num

month = get_month()
print(get_days(month))
