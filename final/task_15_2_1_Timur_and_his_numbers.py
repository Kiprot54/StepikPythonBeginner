import ifnumber

print('Тимур и его числа')
print()

def get_number(text):
    while True:
        num = input(text + ': ')
        if_number = ifnumber.if_number(num)
        if if_number == 'int' and int(num) > 0:
            num = int(num)
            return num
        else:
            print('Данные введены некорректно! Нужно ввести число')

n = get_number('Назови целое число больше 0')
left = 1
right = n
attempts = 0
while left <= right:
    attempts += 1
    middle = (left + right) // 2
    left = middle + 1
print(f'Для того, чтобы угадать число от 1 до {n}, нужно минимум {attempts} попыток')


