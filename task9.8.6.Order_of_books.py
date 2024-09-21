import ifnumber

print('Порядок книг')
print()

s_min = ''
flag = True
while True:
    n = input('Сколько книг в библиотеке Душнилы? ')
    if_number = ifnumber.if_number(n)
    if if_number == 'int' and int(n) > 0:
        n = int(n)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное число')
        print()
for i in range(1, n + 1):
    while True:
        s = input('Введи фамилию, инициалы автора и "название книги": ')
        if len(s.strip()) == 0:
            print('Строка не должна быть пустой')
            print()
        else:
            break
    print()
    index_first_space = s.find(' ')
    index_first_comma = s.find(',')
    author_and_book_name = s[:index_first_space] + s[index_first_comma:]
    if s_min == '':
        s_min = author_and_book_name
    else:
        if s_min > author_and_book_name:
           flag = False
           break
        s_min = author_and_book_name
if flag:
    print('YES')
else:
    print('NO')

