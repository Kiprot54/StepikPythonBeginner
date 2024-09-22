print('Каждый третий')
print()

while True:
    s = input('Введи строку: ')
    if len(s.strip()) == 0:
        print('Строка не должна быть пустой')
        print()
    else:
        break
print()
s1 = ''
for i in range(len(s)):
    if i % 3 != 0:
        s1 += s[i]
print(s1)