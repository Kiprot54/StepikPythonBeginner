print('Три последовательных числа')
print()
while True:
    n = input('Введи целое число: ')

    if n.isdigit() or (n[0] == '-' and n[1:].isdigit()):
        n = int(n)
        break
    else:
        print('Нужно ввести целое число')
        print()

print(n)
print(n + 1)
print(n + 2)
