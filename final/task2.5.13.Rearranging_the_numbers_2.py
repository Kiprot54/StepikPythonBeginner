print('Перестановка цифр')
print()
while True:
    abc = input('Введи целое положительное трехзначное число: ')
    if abc.isdigit() and 100 <= int(abc) <= 999:
        break
    else:
        print('Нужно ввести целое положительное трехзначное число')
        print()
print()
a = abc[0]
b = abc[1]
c = abc[2]
print(f'{abc}')
print(f'{a}{c}{b}')
print(f'{b}{a}{c}')
print(f'{b}{c}{a}')
print(f'{c}{b}{a}')
print(f'{c}{a}{b}')