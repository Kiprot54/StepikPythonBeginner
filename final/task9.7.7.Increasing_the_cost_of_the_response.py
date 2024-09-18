print('Накручиваем стоимость ответа')
print()

while True:
    s = input('Введи строку: ')
    if len(s.strip()) == 0:
        print('Строка не должна быть пустой')
        print()
    else:
        break
eng = 'eyopaxcETOPAHXCBM'
rus = 'еуорахсЕТОРАНХСВМ'
total_old = 0
total_new = 0
for c in s:
    total_old += ord(c)
total_old *= 3
for i in range(len(eng)):
    s = s.replace(eng[i], rus[i])
for c in s:
    total_new += ord(c)
total_new *= 3
print(f'Старая стоимость: {total_old}🐝')
print(f'Новая стоимость: {total_new}🐝')
