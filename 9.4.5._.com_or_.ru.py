print('.com or .ru')
print()

while True:
    s = input('Введи строку: ')
    if len(s.strip()) == 0:
        print('Строка не должна быть пустой')
        print()
    else:
        break
print()
if s.endswith('.com') or s.endswith('.ru'):
    temp = ''
else:
    temp = 'не '

print(f'Строка "{s}" {temp}заканчивается на .com или .ru')
