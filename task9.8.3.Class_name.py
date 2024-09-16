import ifnumber

print('Название класса')
print()

while True:
    n = input('Введи целое положительное число: ')
    if_number = ifnumber.if_number(n)
    if if_number == 'int' and int(n) > 0:
        n = int(n)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное число')
        print()
print()
for i in range(n):
    while True:
        s = input('Введи название класса: ')
        if len(s.strip()) == 0:
            print('Название класса не может быть пустым')
            print()
        else:
            break
    
    if len(s) == 2:
        if s[0].isdigit() and s[1].isalpha():
            if 0 <= int(s[0]) <= 9 and ord('А') <= ord(s[1]) <= ord('П'):
                temp = ''
            else:
                temp = 'не'
        else:
            temp = 'не'
    else:
        temp = 'не'
    print(f'Название класса {s} {temp}правильное')
    print()
