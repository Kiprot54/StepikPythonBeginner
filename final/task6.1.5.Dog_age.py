print('Dog age')
print()
while True:
    dog_year = input('Введи возраст собаки: ')
    if dog_year.isdigit() and int(dog_year) != 0:
        dog_year = int(dog_year)
        break
    else:
        print('Нужно ввести целое положительное число')
        print()
print()
man_year = 10.5
if 1 <= dog_year <= 2:
    man_year *= dog_year
elif 2 < dog_year:
    man_year = man_year * 2 + 4 * (dog_year - 2)
print(f'Возрасту собаки {dog_year} лет соотвествует возраст человека {man_year} лет')
