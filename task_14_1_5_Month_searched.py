import ifnumber

print('Искомый месяц')
print()

def get_month(language, number):
    ru_months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    en_months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    if language == 'ru':
        return ru_months[number - 1]
    else:
        return en_months[number - 1]

def get_language():
    while True:
        s = input('Выбери язык: русский (ru) или английский (en): ')
        if s != 'ru' and s != 'en':
            print('Нужно выбрать ru или en')
        else:
            return s

def get_num():
    while True:
        num = input('Введи номер месяца: ')
        if_number = ifnumber.if_number(num)
        if if_number == 'int' and 1 <= int(num) <= 12:
            num = int(num)
            return num
        else:
            print('Введён неправильный номер месяца.')
            print()

language = get_language()
number = get_num()

print(get_month(language, number))

# 1 месяц года на английском языке - january
