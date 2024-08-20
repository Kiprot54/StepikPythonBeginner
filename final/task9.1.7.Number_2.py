print('Цифра 2')
print()

while True:
    s = input('Введи строку: ')
    if len(s.strip()) == 0:
        print('Строка не должна быть пустой')
        print()
    else:
        break
print()
flag = True
s_digit = '1234567890'
for i in range(len(s)):
    if s[i] in s_digit:
        flag = False
        break
if not flag:
    ins = 'цифра есть'
else:
    ins = 'цифр нет'
print(f'В строке "{s}" {ins}')
