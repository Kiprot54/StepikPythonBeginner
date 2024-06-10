print('Трёхзначное число')
print()
while True:
    n = input('Введи число: ')
    if n.isdigit() and n != 0:
        # n = int(n)
        break
    else:
        print('Нужно ввести целое положительное число')
        print()
print()

# if 100 <= n <= 999:
#     print(f'Число {n} - трёхзначное')
# else:
#     print(f'Число {n} - не трёхзначное')

if len(n) == 3:
    print(f'Число {n} - трёхзначное')
else:
    print(f'Число {n} - не трёхзначное')
