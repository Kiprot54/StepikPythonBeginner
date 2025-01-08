import ifnumber

print('Конвертер километров')
print()

def convert_to_miles(km):
    miles = km * 0.6214
    return miles

def get_distance_kilometers():
    while True:
        num = input('Введи расстояние в километрах: ')
        if_number = ifnumber.if_number(num)
        if if_number == 'int' and int(num) > 0:
            num = int(num)
            return num
        elif if_number == 'float' and float(num) > 0:
            num = float(num)
            return num
        else:
            print('Данные введены некорректно! Нужно ввести положительное число')
            print()

km = get_distance_kilometers()
print(convert_to_miles(km))