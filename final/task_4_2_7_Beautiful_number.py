print('Красивое число')
print()
while True:
    n = input('Введи целое число: ')
    if n.isdigit() or (n[0] == '-' and n[1:].isdigit()):
        break
    else:
        print('Нужно ввести целое число')
        print()
print()
if len(n) == 4 or (n[0] == '-' and len(n[1:]) == 4):
    m = abs(int(n))
    if m % 7 == 0 or m % 17 == 0:
        print(f'Число {n} одновременно и четырёхзначное, и делится нацело на 7 или на 17')
    else:
        print(f'Число {n} или не четырёхзначное, или не делится нацело на 7 или на 17')
else:
    print(f'Число {n} не четырёхзначное')
