print('Панграммы')
print()

def is_pangram(text, language):
    alph_ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    alph_en = 'abcdefghijklmnopqrstuvwxyz'
    text = text.lower()
    if language == 'ru':
        for c in alph_ru:
            if c in text:
                return True
            else:
                return False
    else:
        for c in alph_en:
            if c in text:
                return True
            else:
                return False

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
        s = input('Выбери язык: русский (ru) или английский (en): ')
        if s != 'ru' and s != 'en':
            print('Нужно выбрать ru или en')
        else:
            return s


language = get_language()
text = get_text()

print(is_pangram(text, language))
