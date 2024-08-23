print('Делаем срезы 1')
print()

while True:
    s = input('Введи строку длиной больше 3-х символов: ')
    if len(s) <= 3:
        print('Строка должна быть длиной больше 3-х символов')
        print()
    else:
        break
print()
s_len = len(s)
s_triple = s * 3
s_first = s[0]
s_first_3 = s[:3]
s_last_3 = s[-3:]
s_revert = s[::-1]
s_delete = s[1:len(s) - 1]
print(f'Общее количество символов в строке "{s}" равно {s_len}')
print(f'Строка "{s}", повторенная 3 раза: "{s_triple}"')
print(f'Первый символ строки "{s}": "{s_first}"')
print(f'Первые три символа строки "{s}": "{s_first_3}"')
print(f'Последние три символа строки "{s}": "{s_last_3}"')
print(f'Строка "{s}" в обратном порядке: "{s_revert}"')
print(f'Строка "{s}" с удалённым первым и последним символами: "{s_delete}"')
