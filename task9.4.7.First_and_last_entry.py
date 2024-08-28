print('Самый частотный символ')
print()

while True:
    s = input('Введи строку: ')
    if len(s) == 0:
        print('Строка не должна быть пустой')
        print()
    else:
        break
print()
f_count = s.count('f')
if f_count == 1:
    print(f'В строке "{s}" буква "f" встречается {f_count} раз. Её индекс - {s.find('f')}')
elif f_count == 0:
    print(f'В строке "{s}" буква "f" не встречается')
else:
    f_first_index = s.find('f')
    f_last_index = s.rfind('f')
    print(f'В строке "{s}" буква "f" встречается {f_count} раз. Индекс её первого вхождения - {f_first_index}, индекс её последнего вхождения - {f_last_index}')
