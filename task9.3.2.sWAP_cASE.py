print('sWAP cASE')
print()

while True:
    s = input('Введи строку: ')
    if len(s) == 0:
        print('Строка не должна быть пустой')
        print()
    else:
        break
print()
print(s.swapcase())
