print('Удаление фрагмента')
print()

while True:
    s = input('Введи строку: ')
    if len(s) == 0:
        print('Строка не должна быть пустой')
        print()
    else:
        break
print()
h_first_index = s.find('h')
h_last_index = s.rfind('h')
h_counter = s.count('h')
h_delete = s[h_first_index:h_last_index + 1]
if h_counter <= 1:
    print(f'В строке "{s}" {h_counter} букв "h"')
else:
    print(s[:h_first_index] + s[h_last_index + 1:])
