print('Сколько раз?')
print()

while True:
    s = input('Введи строку: ')
    if len(s.strip()) == 0:
        print('Строка не должна быть пустой')
        print()
    else:
        break
print()
counter_plus = 0
counter_mult = 0
for i in range(len(s)):
    if s[i] == '+':
        counter_plus += 1
    elif s[i] == '*':
        counter_mult += 1
print(f'В строке "{s}":')
print(f'символ "+" встречается {counter_plus} раз;')
print(f'символ "*" встречается {counter_mult} раз.')
