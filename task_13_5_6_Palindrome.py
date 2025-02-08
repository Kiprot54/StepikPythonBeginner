print('Палиндром')
print()

def is_palindrome(text):
    s = ''
    for el in text:
        if el.isalnum():
            s += el.lower()
    return s == s[::-1]

def get_string():
    while True:
        s = input('Введи строку: ')
        if len(s.strip()) == 0:
            print('Строка не должна быть пустой')
            print()
        else:
            return s

s = get_string()
temp = ''
if not is_palindrome(s):
    temp = 'не '
print(f'Строка "{s}" {temp}является палиндромом')