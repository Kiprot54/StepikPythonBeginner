import ifnumber

print('Взлом Братства Стали')
print()

while True:
    s = input('Введи # и количество строк в программе: ')
    if len(s.strip()) == 0:
        print('Строка не должна быть пустой')
        print()
    elif not (s[0] == '#' and s[1:].isdigit() and (ifnumber.if_number(s[1:]) == 'int' and 0 <= int(s[1:]))):
        print('Нужно ввести # и целое положительное число')
    else:
        break
print()
lines = []
n = int(s[1:])
for i in range(n):
    while True:
        line = input('Введи строку кода: ')
        if len(line.strip()) == 0:
            print('Строка не должна быть пустой')
            print()
        else:
            break
    print()
    if '#' in line:
        line_index = line.index('#')
        line = line[:line_index].rstrip()
    lines.append(line)
print(*lines, sep='\n')
