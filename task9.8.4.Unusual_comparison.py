print('Необычное сравнение')
print()

while True:
    s1 = input('Введи первую строку: ')
    if len(s1.strip()) == 0:
        print('Строка не должна быть пустой')
        print()
    else:
        break
while True:
    s2 = input('Введи вторую строку: ')
    if len(s2.strip()) == 0:
        print('Строка не должна быть пустой')
        print()
    else:
        break
print()
s1_letter = ''
s2_letter = ''
for c in s1:
    if c.isalpha():
        s1_letter += c.lower()
for c in s2:
    if c.isalpha():
        s2_letter += c.lower()
if s1_letter == s2_letter:
    temp = ''
else:
    temp = 'не '
print(f'Строки {s1} и {s2} {temp}равны')
