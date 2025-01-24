import ifnumber

print('Is the Triangle Valid?')
print()


def is_valid_triangle(side1, side2, side3):
    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        return True
    return False


def get_number(s):
    while True:
        num = input(f'Введи {s} целое положительное число: ')
        if_number = ifnumber.if_number(num)
        if if_number == 'int' and int(num) > 0:
            num = int(num)
            return num
        else:
            print('Данные введены некорректно! Нужно ввести целое положительное число')
            print()


def get_numbers():
    numbers = [get_number(f'{i}-е') for i in range(1, 4)]
    return numbers


numbers = get_numbers()
is_valid = is_valid_triangle(numbers[0], numbers[1], numbers[2])

temp = ''
if is_valid:
    temp = 'не'

print(f'Треугольник со сторонами {numbers[0]}, {numbers[1]}, {numbers[2]} {temp}вырожденный')
