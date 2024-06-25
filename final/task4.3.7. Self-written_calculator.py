print('Церемония взвешивания')
print()
while True:
    n1 = input('Введи первое число: ')
    if n1.isdigit() or (n1[0] == '-' and n1[1:].isdigit()):
        n1 = int(n1)
        break
    else:
        print('Нужно ввести целое число')
        print()
while True:
    n2 = input('Введи второе число: ')
    if n2.isdigit() or (n2[0] == '-' and n2[1:].isdigit()):
        n2 = int(n2)
        break
    else:
        print('Нужно ввести целое число')
        print()
s = input('Введи математическую операцию: ')

if s == '+':
    print(n1, s, n2, '=', n1 + n2)
elif s == '-':
    print(n1, s, n2, '=', n1 - n2)
elif s == '*':
    print(n1, s, n2, '=', n1 * n2)
elif s == '/':
    if n2 == 0 :
        print('На нуль делить нельзя!')
    else:
        print(n1, s, n2, '=', n1 / n2)
else:
    print('Неверная операция')
