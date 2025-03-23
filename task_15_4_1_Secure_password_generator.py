import random

print('Генератор безопасных паролей')
print()

def generate_password(length, chars):
    password = ''
    for i in range(length):
        s = random.randint(0, len(chars) - 1)
        password += chars[s]
    return password

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ambiguous_chars = 'il1Lo0O'
punctuation = '!#$%&*+-=?@^_.'

quantity_password = int(input('Сколько паролей сгенерировать? '))
len_password = int(input('Длину одного пароля? '))

num_password = input(f'Включать ли цифры {digits}? y(да) или n(нет) ')
uppercase_letters_password = input(f'Включать ли прописные буквы {uppercase_letters}? y(да) или n(нет) ')
lowercase_letters_password = input(f'Включать ли строчные буквы {lowercase_letters}? y(да) или n(нет) ')
symbol_password = input(f'Включать ли символы {punctuation}? y(да) или n(нет) ')
ambiguous_chars_password = input(f'Исключать ли неоднозначные символы {ambiguous_chars}? y(да) или n(нет) ')

chars = ''
answer = 'y'
if num_password == answer:
    chars += digits
if uppercase_letters_password == answer:
    chars += uppercase_letters
if num_password == answer:
    chars += lowercase_letters
if num_password == answer:
    chars += punctuation
if ambiguous_chars_password == answer:
    chars_without_ambiguous = ''
    for el in chars:
        if el not in ambiguous_chars:
            chars_without_ambiguous += el
    chars = chars_without_ambiguous

for i in range(quantity_password):
    print(generate_password(len_password, chars))