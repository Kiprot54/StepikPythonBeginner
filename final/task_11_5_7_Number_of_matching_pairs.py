import ifnumber

print('Количество совпадающих пар')
print()

while True:
    s = input('Введи строку, содержащую целые числа: ')
    if len(s.strip()) == 0:
        print('Строка не должна быть пустой')
        print()
    else:
        break
print()

numbers = s.split()
flag = True
for el in numbers:
    if not el.isdigit():
        flag = False
        break
    else:
        if_number = ifnumber.if_number(el)
        if if_number != 'int':
            flag = False
            break
if flag:
    counter = 0
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                counter += 1
    print(counter)
else:
    print('Ошибка! Строка содержит не только целые числа')
