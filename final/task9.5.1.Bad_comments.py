import ifnumber

print('Плохие комментарии')
print()

while True:
    n = input('Введи количество комментариев: ')
    if_number = ifnumber.if_number(n)
    if if_number == 'int' and int(n) > 0:
        n = int(n)
        break
    else:
        print('Данные введены некорректно! Нужно ввести положительное число')
        print()
print()
# for i in range(1, n + 1):
#     s = input(f'Введи комментарий {i}: ')
#     if len(s) == 0 or s.isspace():
#         print(f'{i}: COMMENT SHOULD BE DELETED')
#     else:
#         print(f'{i}: {s}')
lst = []
for i in range(1, n + 1):
    s = input(f'Введи комментарий {i}: ')
    lst.append(s)
print()
for i in range(len(lst)):
    if len(lst[i].strip()) == 0:
        print(f'{i + 1}: COMMENT SHOULD BE DELETED')
    else:
        print(f'{i + 1}: {lst[i]}')
