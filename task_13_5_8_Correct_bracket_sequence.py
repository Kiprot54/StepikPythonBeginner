print('Правильная скобочная последовательность')
print()

def is_correct_bracket(text):
    brackets_count = 0
    for el in text:
        if el == '(':
            brackets_count += 1
        else:
            brackets_count -= 1
        if brackets_count < 0:
            return False
    return brackets_count == 0

def get_string():
    while True:
        s = input('Введи строку только со скобками: ')
        if len(s.strip()) == 0:
            print('Строка не должна быть пустой')
            print()
        else:
            if s.count('(') + s.count(')') == len(s):
                return s
            else:
                print('Нужно ввести только скобки')
                print()

s = get_string()
temp = ''
if not is_correct_bracket(s):
    temp = 'не '

print(f'Строка "{s}" {temp}является правильной скобочной последовательностью')
