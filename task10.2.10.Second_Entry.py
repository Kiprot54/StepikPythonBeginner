print('Второе вхождение')
print()

while True:
    s = input('Введи строку: ')
    if len(s.strip()) == 0:
        print('Строка не должна быть пустой')
        print()
    else:
        break
print()

counter_f = s.count('f')
if counter_f == 1:
    print(f'Буква "f" в строке "{s}" встречается {counter_f} раз')
elif counter_f == 0:
    print(f'Буква "f" в строке "{s}" не встречается')
else:
    s1 = s
    s1 = s1.replace('f', '.', 1)
    s1_find_f = s1.find('f')
    print(f'У второй буквы "f" в строке "{s}" индекс {s1_find_f}')