import ifnumber

print('Сумма цифр')
print()


def print_digit_sum(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    print(total)


while True:
    num = input('Введи целое положительное число: ')
    if_number = ifnumber.if_number(num)
    if if_number == 'int' and int(num) > 0:
        num = int(num)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное число')
        print()

print_digit_sum(num)
