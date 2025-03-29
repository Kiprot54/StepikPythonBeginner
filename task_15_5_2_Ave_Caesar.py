from json.decoder import WHITESPACE

print('Аве, Цезарь')
print()

def get_text():
    while True:
        s = input('Введи текст на английском языке, который нужно зашифровать: ')
        if len(s.strip()) == 0:
            print('Строка не должна быть пустой')
            print()
        else:
            return s

def count_alpha(word):
    count = 0
    for c in word:
        if c.isalpha():
            count += 1
    return count

first = ord('a') # 97
last = ord('z') # 122
alph_len = last - first + 1 # 25
text = get_text()
words = text.split()
encrypted_words = []
for word in words:
    encrypted_word = ''
    for c in word:
        if c.isalpha():
            new_c_code = ord(c.lower()) + count_alpha(word)
            while new_c_code > last:
                new_c_code -= alph_len
            new_c = chr(new_c_code)
            if c.lower() != c:
                new_c = new_c.upper()
            encrypted_word += new_c
        else:
            encrypted_word += c
    encrypted_words.append(encrypted_word)
print(' '.join(encrypted_words))