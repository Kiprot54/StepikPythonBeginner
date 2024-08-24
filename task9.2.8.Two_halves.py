print('Две половинки')
print()

while True:
    s = input('Введи строку: ')
    if len(s.strip()) == 0:
        print('Строка не должна быть пустой')
        print()
    else:
        break
print()
s_len = len(s)
s_middle_len = s_len // 2
if s_len % 2 == 1:
    s_first = s[:s_middle_len + 1]
    s_last = s[s_middle_len + 1:s_len]
else:
    s_first = s[:s_middle_len]
    s_last = s[s_middle_len:s_len]

print(s_last + s_first)