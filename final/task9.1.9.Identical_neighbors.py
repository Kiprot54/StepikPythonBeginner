print('Одинаковые соседи')
print()

while True:
    s = input('Введи строку: ')
    if len(s.strip()) == 0:
        print('Строка не должна быть пустой')
        print()
    else:
        break
print()
counter = 0
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        counter += 1
print(f'В строке "{s}" {counter} одинаковых соседних символов')
