import ifnumber

print('Делители 1')
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
number = get_number()
print(get_factors(number))
