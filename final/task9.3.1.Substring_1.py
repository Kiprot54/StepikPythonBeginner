print('Заглавные буквы')
print()

while True:
    s = input('Введи имя и фамилию в одной строке: ').strip()
    if s.count(' ') != 1:
        print('Нужно ввести 2 слова: имя и фамилию')
        print()
    else:
        break
print()
if s == s.title():
    temp = 'правильно: оба слова с большой'
else:
    temp = 'неправильно: хотя бы одно слово с маленькой'
print(f'Имя и фамилия "{s}" введены {temp} буквы')
