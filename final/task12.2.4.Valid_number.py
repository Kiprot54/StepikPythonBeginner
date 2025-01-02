print('Валидный номер')
print()

while True:
    s = input('Введи строку: ').strip()
    if len(s) == 0:
        print('Строка не должна быть пустой')
        print()
    else:
        break
print()

numbers = s.split('-')

flag = True
if len(numbers) == 4:
    if numbers[0].isdigit() and numbers[0] == '7':
        del numbers[0]
    else:
        flag = False

if flag and len(numbers) == 3:
    if len(numbers[0]) != 3 or len(numbers[1]) != 3 or len(numbers[2]) != 4:
        flag = False
    else:
        if not numbers[0].isdigit() or not numbers[1].isdigit() or not numbers[2].isdigit():
            flag = False

if flag:
    print(f'Номер {s} правильный')
else:
    print('Введён неправильный номер')
