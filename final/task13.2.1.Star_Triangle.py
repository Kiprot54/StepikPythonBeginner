import ifnumber

print('Звёздный треугольник')
print()

def draw_triangle(fill, base):
    for i in range(1, base // 2 + 2):
        print(fill * i)

    for i in range(base // 2, -1, -1):
        print(fill * i)
        
while True:
    symbol = input('Введи символ: ')
    if len(symbol.strip()) == 0:
        print('Строка не должна быть пустой')
        print()
    elif len(symbol.strip()) != 1:
        print('Нужно ввести один символ')
    else:
        break
print()

while True:
    num = input('Введи целое чётное число: ')
    if_number = ifnumber.if_number(num)
    if if_number == 'int' and int(num) > 0:
        num = int(num)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое чётное число')
        print()
print()

draw_triangle(symbol, num)

