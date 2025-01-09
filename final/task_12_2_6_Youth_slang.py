print('Молодёжный жаргон')
print()

print(*[el[1:] + el[0] + 'ки' for el in input('Введи строку: ').split()])