print('Минутка генетики')
print()

while True:
    s = input('Введи строку: ')
    if len(s.strip()) == 0:
        print('Строка не должна быть пустой')
        print()
    else:
        break
print()

counter_a = s.lower().count('а')
counter_g = s.lower().count('г')
counter_c = s.lower().count('ц')
counter_t = s.lower().count('т')
if len(s) - (counter_a + counter_g + counter_c + counter_t) > 0:
    print('Данные введены неверно')
else:
    print(f'В генетическом коде "{s}":')
    print(f'Аденин: {counter_a}')
    print(f'Гуанин: {counter_g}')
    print(f'Цитозин: {counter_c}')
    print(f'Тимин: {counter_t}')
