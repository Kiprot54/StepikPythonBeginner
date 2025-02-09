print('Ровно в одном')
print()

def is_one_away(word1, word2):
    if len(word1) == len(word2):
        n = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                n += 1
                if n > 1:
                    return False
        if n == 0:
            return False
        return True
    return False

def get_string():
    while True:
        s = input('Введи строку: ')
        if len(s.strip()) == 0:
            print('Строка не должна быть пустой')
            print()
        else:
            return s

def start():
    s1 = get_string()
    s2 = get_string()
    ins1 = ''
    ins2 = ''
    if is_one_away(s1, s2):
        print(f'Длина слов {s1} и {s2} равна и они отличаются на одну букву')
    else:
        print(f'Длина слов {s1} и {s2} или не равна, или они отличаются не на одну букву')

start()
