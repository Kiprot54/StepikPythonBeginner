print('Good password')
print()

def is_password_good(password):
    if len(password) >= 8:
        up = False
        low = False
        dig = False
        for c in password:
            if c.isupper():
                up = True
            if c.islower():
                low = True
            if c.isdigit():
                dig = True
        return up and low and dig
    return False

def get_string():
    while True:
        s = input('Введи пароль: ')
        if len(s.strip()) == 0:
            print('Пароль не должен быть пустым')
            print()
        else:
            return s


def start():
    str = get_string()
    temp = ''
    if not is_password_good(str):
        temp = 'не'

    return f'Пароль {str} {temp}надёжный'
print(start())
