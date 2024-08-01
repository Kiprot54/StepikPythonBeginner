import ifnumber

print('Ведьмаку заплатите чеканной монетой')
print()


while True:
    n = input('Введи, сколько нужно заплатить ведьмаку: ')
    if_number = ifnumber.if_number(n)
    if if_number == 'int' and int(n) > 0:
        n = int(n)
        print()
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное число')
    print()
counter = 0
while n != 0:
    if n >= 25:
        n -= 25
        counter += 1
    elif n >= 10:
        n -= 10
        counter += 1
    elif n >= 5:
        n -= 5
        counter += 1
    elif n >= 1:
        n -= 1
        counter += 1
print(f'Нужно отдать ведьмаку минимум {counter} чеканных монет')


