print('Панграммы')
print()

def is_pangram(text, language):
    alph_ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    alph_en = 'abcdefghijklmnopqrstuvwxyz'
    txt = text.lower()
    if language == 'ru':
        return is_symbol_in_string(alph_ru, txt)
    else:
        return is_symbol_in_string(alph_en, txt)

def is_symbol_in_string(alphabet, txt):
    for c in alphabet:
        if c not in txt:
            return False
    return True

def get_text():
    while True:
        s = input('Введи строку: ')
        if len(s.strip()) == 0:
            print('Строка не должна быть пустой')
            print()
        else:
            return s

def get_language():
    while True:
        lang = input('Выбери язык: русский (ru) или английский (en): ')
        if lang != 'ru' and lang != 'en':
            print('Нужно выбрать ru или en')
            print()
        else:
            return lang

text = get_text()
language = get_language()

s = ''
if not is_pangram(text, language):
    s = 'не '

print(f'Строка "{text}" {s}является панграммой')