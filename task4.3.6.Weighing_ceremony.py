print('Церемония взвешивания')
print()
name = input('Введи своё имя: ')
while True:
    weight = input('Введи свой вес: ')
    if weight.isdigit() and weight != 0:
        weight = int(weight)
        break
    else:
        print('Нужно ввести целое положительное число')
        print()
print()
if weight < 60:
    print(f'{name}, твоя категория - лёгкий вес')
elif weight < 64:
    print(f'{name}, твоя категория - первый полусредний вес')
elif weight < 69:
    print(f'{name}, твоя категория - полусредний вес вес')