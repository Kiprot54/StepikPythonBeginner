print('Сумма чисел')
print()

while True:
    numbers = input('Введи строку, содержащую натуральные числа: ')
    if len(numbers.strip()) == 0 and int(numbers) > 0:
        print('Строка не должна быть пустой')
        print()
    else:
        break
print()
total = 0
numbers = numbers.split()
for el in numbers:
    total += int(el)
print(*numbers, sep='+', end='')
print('=' + str(total))
