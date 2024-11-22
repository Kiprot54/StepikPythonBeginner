import ifnumber

print('Сортировка чисел')
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
            if not el.isdigit() and ifnumber.if_number(el) != 'int':
                print('Нужно ввести строку, содержащую целые числа')
                print()
                flag = False
                break
        if flag:
            break
numbers = s.split()
lst = []
for i in range(len(numbers)):
    lst.append(int(numbers[i]))
lst.sort()
print(*lst)
lst.sort(reverse=True)
print(*lst)
