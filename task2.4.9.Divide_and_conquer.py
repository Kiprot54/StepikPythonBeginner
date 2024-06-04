print('Разделяй и властвуй')
print()
while True:
    x = input('Введи целое положительное число: ')
    if x.isdigit():
        x = int(x)
        break
    else:
        print('Нужно ввести целое положительное число')
        print()

print()
print(x, x * 2, x * 3, x * 4, x * 5, sep='---')
