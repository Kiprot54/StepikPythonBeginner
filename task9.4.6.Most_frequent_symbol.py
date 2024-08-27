print('Самый частотный символ')
print()

while True:
    s = input('Введи строку: ')
    if len(s.strip()) == 0:
        print('Строка не должна быть пустой')
        print()
    else:
        break
print()
counter = 0
latter = ''
for c in s:
    c_count = s.count(c)
    if c_count >= counter:
        counter = c_count
        latter = c
print(f'В строке "{s}" наиболее часто появляется символ "{latter}" - {counter} раз')