print('Переворот')
print()

while True:
    s = input('Введи строку, в которой минимум две буквы "h": ')
    if len(s.strip()) == 0:
        print('Строка не должна быть пустой')
        print()
    elif s.count('h') < 2:
        print('В строке должно быть минимум две буквы "h"')
    else:
        break
print()

first_index = s.find('h')
last_index = s.rfind('h')
substring_h = s[first_index:last_index + 1]
reverse_h = substring_h[::-1]
first_s = s[:first_index]
last_s = s[last_index + 1:]
s = first_s + reverse_h + last_s
print(s)
