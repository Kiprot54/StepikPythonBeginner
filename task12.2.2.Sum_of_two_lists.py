import ifnumber

print('Сумма двух списков')
print()

s1, s2 = '', ''
for i in range(1, 3):
    while True:
        s = input(f'Введи {i}-ю строку: ')
        if len(s.strip()) == 0:
            print('Строка не должна быть пустой')
            print()
        flag = False
        for el in s.split():
            if ifnumber.if_number(el) != 'int':
                flag = True
                break
        if flag:
            print('Нужно ввести строку, содержащую целые числа')
        else:
            if i == 1:
                s1 = s
            else:
                s2 = s
            if len(s1) != 0 and len(s2) != 0:
                if s1.count(' ') != s2.count(' '):
                    print('Количество чисел в обеих строках должно быть одинаковое')
                else:
                    break
            else:
                break
print()

L = s1.split()
M = s2.split()

suma = 0
lst = []
for i in range(len(L)):
    suma = int(L[i]) + int(M[i])
    lst.append(suma)
print(*lst)