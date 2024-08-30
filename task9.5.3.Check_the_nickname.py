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
var1 = nickname[0] == '@'
var2 = 5 <= len(nickname) <= 15
var3 = nickname[1:] == nickname[1:].lower()
var4 = nickname[1:].isalnum()
if nickname[0] == '@' and 5 <= len(nickname) <= 15 and nickname[1:] == nickname[1:].lower() and nickname[1:].isalnum():
    print('Никнейм правильный')
else:
    print('Никнейм неправильный')
print(var1)
print(var2)
print(var3)
print(var4)