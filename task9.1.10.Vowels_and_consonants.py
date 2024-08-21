print('Гласные и согласные')
print()
while True:
    s = input('Введи строку: ')
    if len(s.strip()) == 0:
        print('Строка не должна быть пустой')
        print()
    else:
        break
print()
vowels_symbols = 'ауоыэяюёие'
consonants_symbols = 'бвгджзйклмнпрстфхцчшщ'
counter_vowels_symbols = 0
counter_consonants_symbols = 0
for c in s.lower():
    if c in vowels_symbols:
        counter_vowels_symbols += 1
    elif c in consonants_symbols:
        counter_consonants_symbols += 1
print(f'В строке "{s}" {counter_vowels_symbols} гласных букв и {counter_consonants_symbols} согласных букв русского языка.')
