print('Принадлежность 2')
print()
while True:
    x = input('Введи целое число: ')
    if x.isdigit() or (x[0] == '-' and x[1:].isdigit()):
        x = int(x)
        break
    else:
        print('Нужно ввести целое число')
        print()
print()
# if x <= -3 or x >= 7:
if not -3 < x < 7:
    print(f'Число {x} или меньше -3 включительно, или больше 7 включительно')
else:
    print(f'Число {x} не меньше -3 включительно и не больше 7 включительно')
