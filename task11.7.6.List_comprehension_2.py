import ifnumber

print('Списочное выражение 2')
print()


while True:
    s = input('Введи строку, содержащую целые числа: ')
    if len(s.strip()) == 0:
        print('Строка не должна быть пустой')
        print()
    else:
        numbers = s.split()
        flag = True
        for el in numbers:
            if not (el.isdigit() or ifnumber.if_number(el) == 'int'):
                flag = False
                break
        if flag:
            break
        else:
            print('Нужно ввести строку, содержащую целые числа')
print()
numbers = s.split()
print(*[int(el) ** 3 for el in numbers])
