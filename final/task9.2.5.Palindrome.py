print('Палиндром')
print()

while True:
    s = input('Введи слово: ').strip()
    if len(s) == 0:
        print('Строка не должна быть пустой')
        print()
    elif s.find(' ') != -1:
        print('Нужно вести слово')
        print()
    else:
        break
print()
s_small = s.lower()
s_revert = s_small[::-1]
if s_revert == s_small:
    temp = ''
else:
    temp = 'не '
print(f'Слово {s} {temp}является палиндромом')
