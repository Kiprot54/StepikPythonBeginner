print('Количество артиклей')
print()

while True:
    s = input('Введи строку, содержащую английский текст: ')
    if len(s.strip()) == 0:
        print('Строка не должна быть пустой')
        print()
    else:
        break
print()

words = s.split()
counter = 0
for el in words:
    word = el.lower()
    if word == 'a' or word == 'an' or word == 'the':
        counter += 1
print(f"Общее количество артиклей 'a', 'an', 'the': {counter}")
