import ifnumber

print('Is the Number Prime?')
print()

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
temp = ''
if not is_prime(number):
    temp = 'не '
print(f'Число {number} {temp}является простым')
