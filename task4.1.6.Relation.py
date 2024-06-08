print('Соотношение')
print()
while True:
    abcd = input('Введи четырехзначное число: ')
    if abcd.isdigit() and 1000 <= int(abcd) <= 9999:
        break
    else:
        print('Нужно ввести целое четырехзначное число')
        print()
print()
a = abcd[0]
b = abcd[1]
c = abcd[2]
d = abcd[3]
if int(a) + int(d) == int(b) - int(c):
    print(f'{a} + {d} = {b} - {c}')
else:
    print(f'{a} + {d} != {b} - {c}')
