print('Windows OS')
print()

while True:
    source = input('Введи путь к файлу: ')
    if len(source.strip()) == 0:
        print('Строка не должна быть пустой')
        print()
    else:
        break
print()

strings = source.split('\\')
print(*strings, sep='\n')
