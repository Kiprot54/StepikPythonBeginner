print('Змеиный регистр')
print()

def convert_to_python_case(text):
    snake_case = ''
    for i in range(len(text)):
        c = text[i]
        if c.isupper():
            if i != 0:
                snake_case += '_'
            snake_case += c.lower()
        else:
            snake_case += c
    return snake_case

def get_string():
    while True:
        s = input('Введи строку в «верблюжьем регистре»: ')
        if len(s.strip()) == 0:
            print('Строка не должна быть пустой')
            print()
        else:
            if s.strip().count(' ') != 0:
                print('Нужно ввести одно слово в «верблюжьем регистре»')
                print()
            else:
                return s

s = get_string()
print(convert_to_python_case(s))

# Берем каждый символ строки
# Проверяем, если это большая буква
# Если большая
#   Если это первая буква - вместо нее ставим такую же маленькую букву
#   в других случаях - вместо нее ставим "_" и такую же маленькую букву
# Если не большая - ничего не делаем