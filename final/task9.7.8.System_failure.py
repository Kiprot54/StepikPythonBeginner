print('Сбой в системе')
print()

while True:
    s = input('Введи строку с неправильной кодировкой: ')
    if len(s.strip()) == 0:
        print('Строка не должна быть пустой')
        print()
    else:
        break

first_index = s.find('[u-')
while not first_index == -1:
    err = s[first_index:first_index + 8]
    code = err[3:7]
    letter = chr(int(code))
    s = s.replace(err, letter)
    first_index = s.find('[u-')
print(s)
