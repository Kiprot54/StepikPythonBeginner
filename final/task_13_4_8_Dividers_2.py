import ifnumber

print('Делители 2')
print()

def get_factors(num):
    dividers = []
    for i in range(1, num + 1):
        if num % i == 0:
            dividers.append(i)
    return dividers

def get_number():
    while True:
        num = input('Введи целое положительное число: ')
        if_number = ifnumber.if_number(num)
        if if_number == 'int' and int(num) > 0:
            num = int(num)
            return num
        else:
            print('Данные введены некорректно! Нужно ввести целое положительное число')
            print()

def number_of_factors(num):
    dividers = get_factors(num)
    counter_dividers = len(dividers)
    return counter_dividers

number = get_number()

print(number_of_factors(number))
