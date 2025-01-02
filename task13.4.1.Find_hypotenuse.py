from math import sqrt
import ifnumber


print('Найти гипотенузу')
print()

def compute_hypotenuse(a, b):
    c = sqrt(a ** 2 + b ** 2)
    return c

def get_catet():
    while True:
        n = input('Введи длину катета (целое число): ')
        if_number = ifnumber.if_number(n)
        if if_number == 'int':
            n = int(n)
            return n
        else:
            print('Данные введены некорректно! Нужно ввести число')
            print()

catets = []
for _ in range(2):
    catets.append(get_catet())

print(compute_hypotenuse(catets[0], catets[1]))
