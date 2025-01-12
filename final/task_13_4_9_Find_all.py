print('Найти всех')
print()

def find_all(target, symbol):
    indexes = []
    for i in range(len(target)):
        if target[i] == symbol:
            indexes.append(i)
    return indexes

def get_string(arg):
    while True:
        s = input(f'Введи {arg}: ')
        if len(s.strip()) == 0:
            print('Строка не должна быть пустой')
            print()
        else:
            return s

def get_symbol():
    while True:
        s = get_string('любой символ')
        if len(s) == 1:
            return s
        else:
            print('Нужно ввести один символ')
            print()

s = get_string('строку')
symbol = get_symbol()
indexes = find_all(s, symbol)
print(indexes)