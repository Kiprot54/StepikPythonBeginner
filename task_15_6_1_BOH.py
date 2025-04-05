import ifnumber

print('BOH')
print()

def get_num():
    while True:
        num = input('Введи натуральное число в десятичной системе счисления: ')
        if_number = ifnumber.if_number(num)
        if if_number == 'int' and int(num) > 0:
            num = int(num)
            return num
        else:
            print('Данные введены некорректно! Нужно ввести число')
            print()

n = get_num()
binary = bin(n)[2:]
octal = oct(n)[2:]
hex = hex(n)[2:].upper()

print(f'Binary: {binary}')
print(f'Octal: {octal}')
print(f'Hex: {hex}')
