print('Необычное сравнение')
print()

while True:
    s1 = input('Введи строку: ')
    if len(s1.strip()) == 0:
        print('Строка не должна быть пустой')
        print()
    else:
        break
while True:
    s2 = input('Введи строку: ')
    if len(s2.strip()) == 0:
        print('Строка не должна быть пустой')
        print()
    else:
        break
print()
s1_lst = []
s2_lst = []
for c in s1:
    if c.isalpha():
        s1_lst.append(c.lower())
for c in s2:
    if c.isalpha():
        s2_lst.append(c.lower())
if s1_lst == s2_lst:
    temp = ''
else:
    temp = 'не '
print(f'Строка {s1} и {s2} {temp}равны')