print('Стоимость ответа')
print()

while True:
    s = input('Введи строку: ')
    if len(s.strip()) == 0:
        print('Строка не должна быть пустой')
        print()
    else:
        break
total = 0
for c in s:
    total += ord(c)
print(f"Текст сообщения: '{s}'")
print(f"Стоимость сообщения: {total * 3}🐝")
