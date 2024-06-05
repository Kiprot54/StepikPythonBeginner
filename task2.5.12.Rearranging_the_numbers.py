print('Перестановка цифр')
print()
while True:
    n = input('Введи целое положительное двузначное число: ')
    if n.isdigit() and 10 <= int(n) <= 99:
        break
    else:
        print('Нужно ввести целое положительное двузначное число')
        print()
print()
first_digit = n[0]
last_digit = n[1]
print(f'{n} => {last_digit}{first_digit}')