import ifnumber

print('Очень странные дела')
print()

while True:
    n = input('Введи количество зашифрованных строк: ')
    if_number = ifnumber.if_number(n)
    if if_number == 'int' and int(n) > 0:
        n = int(n)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное число')
        print()
print()
counter = 0
for i in range(n):
    while True:
        s = input('Введи следующую строку: ')
        if len(s.strip()) == 0:
            print('Строка не должна быть пустой')
            print()
        else:
            break

    if s.count('11') > 2:
        counter += 1
print()
print(f'В зашифрованном сообщении {counter} нужных строк')
