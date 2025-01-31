import ifnumber

print('Next Prime')
print()

def get_next_prime(num):
    num += 1
    while not is_prime(num):
        num += 1
    return num


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def get_number():
    while True:
        num = input(f'Введи целое положительное число: ')
        if_number = ifnumber.if_number(num)
        if if_number == 'int' and int(num) > 0:
            num = int(num)
            return num
        else:
            print('Данные введены некорректно! Нужно ввести целое положительное число')
            print()

number = get_number()
print(f'Первое простое число после числа {number} равно {get_next_prime(number)}')
