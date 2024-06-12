print('Принадлежность 3')
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
if -30 < x <= -2 or 7 < x <= 25:
    print(f'Число {x} принадлежит промежуткам (-30, -2] или (7, 25]')
else:
    print(f'Число {x} не принадлежит промежуткам (-30, -2] или (7, 25]')
