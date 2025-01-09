print('Проверь никнейм')
print()

while True:
    nickname = input('Введи свой никнейм: ')
    if len(nickname) == 0:
        print('Строка не должна быть пустой')
        print()
    else:
        break
print()

if nickname[0] == '@' and 5 <= len(nickname) <= 15 and nickname[1:] == nickname[1:].lower() and nickname[1:].isalnum():
    print('Никнейм правильный')
else:
    print('Никнейм неправильный')
