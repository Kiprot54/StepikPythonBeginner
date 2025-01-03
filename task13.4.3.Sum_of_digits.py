import ifnumber

print('Сумма цифр')
print()

def sum_digits(n):
    total = 0
    for i in range(len(n)):
        total += int(n[i])
    return total

def get_number():
    while True:
        num = input('Введи целое положительное число: ')
        if_number = ifnumber.if_number(num)
        if if_number == 'int' and int(num) > 0:
            return num
        else:
            print('Данные введены некорректно! Нужно ввести целое положительное число')
            print()

number = get_number()

print(sum_digits(number))
