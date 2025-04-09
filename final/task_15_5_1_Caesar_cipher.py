print('Шифр Цезаря')
print()

def get_direction():
    while True:
        direction = input('Будем шифровать или дешифровать? ш / д ').lower()
        if direction == 'ш' or direction == 'i':
            return True
        elif direction == 'д' or direction == 'l':
            return False
        else:
            print('Я тебя не понял. Повтори ещё раз.')

def get_lang():
    while True:
        lang = input('Выбери язык алфавита ru (русский) или eng (английский): ')
        if lang == 'ru' or lang == 'eng':
            return lang
        else:
            print('Язык введён неверно. Повтори ещё раз.')


def get_step():
    while True:
        step = input('Введи шаг сдвига: ')
        if step.isdigit() and int(step) > 0:
            return int(step)
        else:
            print('Значение введено неверно. Повтори ещё раз.')

def get_text(direction):
    temp = ''
    if not direction:
        temp = 'де'
    while True:
        s = input(f'Введи текст, который нужно {temp}шифровать: ')
        if len(s.strip()) == 0:
            print('Строка не должна быть пустой')
            print()
        else:
            return s

def crypt_string(direction, lang, step, text):
    if lang == 'ru':
        alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    else:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
    s = ''
    alph_len = len(alphabet)
    for c in text:

        c_lower = c.lower()
        if c_lower in alphabet:
            if direction:
                index = alphabet.find(c_lower) + step
                while index > alph_len:
                    index -= alph_len
            else:
                index = alphabet.find(c_lower) - step
                while index < 0:
                    index += alph_len
            if c == c_lower:
                s += alphabet[index]
            else:
                s += alphabet[index].upper()
        else:
            s += c
    return s

direction = get_direction()
print(crypt_string(direction, get_lang(), get_step(), get_text(direction)))
