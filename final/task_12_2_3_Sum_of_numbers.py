import ifnumber

print('Сумма чисел')
print()

numbers = []
while True:
    s = input('Введи строку, содержащую целые числа не меньше нуля: ').strip()
    if len(s) == 0:
        print('Строка не должна быть пустой')
        print()
    else:
        numbers = s.split()
        flag = True
        for el in numbers:
            if ifnumber.if_number(el) != 'int':
                print('Нужно ввести строку, содержащую целые числа не меньше нуля')
                flag = False
                break
            else:
                if int(el) < 0:
                    print('Нужно ввести строку, содержащую целые числа не меньше нуля')
                    flag = False
                    break
        if flag:
            break

print()
total = 0
numbers = s.split()
for el in numbers:
    total += int(el)
print(*numbers, sep='+', end='')
print('=' + str(total))
