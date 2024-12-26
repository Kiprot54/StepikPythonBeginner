print('В одну строку 2')
print()

while True:
    s = input('Введи строку: ')
    if len(s.strip()) == 0:
        print('Строка не должна быть пустой')
        print()
    else:
        break
print()

print(*[s[i] for i in range(len(s)) if s[i] in '1234567890'], sep='')