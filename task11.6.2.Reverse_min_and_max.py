print('Переставить min и max')
print()

while True:
    s = input('Введи числа через пробел: ')
    if len(s.strip()) == 0:
        print('Строка не должна быть пустой')
        print()
    else:
        break
print()

numbers = s.split()

flag = True
for i in range(len(numbers)):
    if not numbers[i].isdigit():
        flag = False
        break
    numbers[i] = float(numbers[i])

if not flag:
    print('Данные введены неверно')
else:
    print(numbers)
    numbers_max = max(numbers)
    numbers_min = min(numbers)
    numbers_index_max = numbers.index(numbers_max)
    numbers_index_min = numbers.index(numbers_min)
    numbers[numbers_index_max] = numbers_min
    numbers[numbers_index_min] = numbers_max
    print(*numbers)
