print('BEEGEEK')
print()

def is_palindrome(text):
    s = ''
    for el in text:
        if el.isalnum():
            s += el.lower()
    return s == s[::-1]

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num // 2):
        if num % i == 0:
            return False
    return True

def is_even(num):
    return num % 2 == 0

def is_digit(s):
    return s.isdigit()

def is_valid_password(password):
    colon = password.split(':')
    if len(colon) == 3:
        a = password[:password.find(':')]
        if not is_digit(a):
            return False
        palindrome = is_palindrome(a)

        b = password[password.find(':') + 1:password.rfind(':')]
        if is_digit(b):
            b = int(b)
        else:
            return False
        prime = is_prime(b)

        c = password[password.rfind(':') + 1:]
        if is_digit(c):
            c = int(c)
        else:
            return False
        even = is_even(c)

        return palindrome and prime and even
    return False

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
if not is_valid_password(s):
    temp = 'не '
print(f'Пароль {s} {temp}соответствует нужным критериям')