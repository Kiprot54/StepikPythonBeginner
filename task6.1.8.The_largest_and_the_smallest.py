print('Наибольшее и наименьшее')
print()
# var 1
# n1 = float(input('Введи первое число: '))
# n2 = float(input('Введи второе число: '))
# n3 = float(input('Введи третье число: '))
# n4 = float(input('Введи четвёртое число: '))
# n5 = float(input('Введи пятое число: '))

# var 1.1
# min_n = 0
# max_n = 0
# if n1 < n2 and n1 < n3 and n1 < n4 and n1 < n5:
#     min_n = n1
# elif n2 < n1 and n2 < n3 and n2 < n4 and n2 < n5:
#     min_n = n2
# elif n3 < n1 and n3 < n2 and n3 < n4 and n3 < n5:
#     min_n = n3
# elif n4 < n1 and n4 < n3 and n4 < n2 and n4 < n5:
#     min_n = n4
# elif n5 < n1 and n5 < n3 and n5 < n4 and n5 < n2:
#     min_n = n5
# if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
#     max_n = n1
# elif n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
#     max_n = n2
# elif n3 > n2 and n3 > n1 and n3 > n4 and n3 > n5:
#     max_n = n3
# elif n4 > n2 and n4 > n3 and n4 > n1 and n4 > n5:
#     max_n = n4
# elif n5 > n2 and n5 > n3 and n5 > n4 and n5 > n1:
#     max_n = n5
# print(f'Наименьшее из чисел ({n1}, {n2}, {n3}, {n4}, {n5}): {min_n}')
# print(f'Наибольшее из чисел ({n1}, {n2}, {n3}, {n4}, {n5}): {max_n}')

# var 1.2
# min_n = n1
# max_n = n1
# if n2 > max_n:
#     max_n = n2
# if n3 > max_n:
#     max_n = n3
# if n4 > max_n:
#     max_n = n4
# if n5 > max_n:
#     max_n = n5
# if n2 < min_n:
#     min_n = n2
# if n3 < min_n:
#     min_n = n3
# if n4 < min_n:
#     min_n = n4
# if n5 < min_n:
#     min_n = n5
# print(f'Наименьшее из чисел ({n1}, {n2}, {n3}, {n4}, {n5}): {min_n}')
# print(f'Наибольшее из чисел ({n1}, {n2}, {n3}, {n4}, {n5}): {max_n}')

# var 2
n = float(input('Введи число: '))
max_n = n
min_n = n
lst = [n]
for i in range(1, 5):
    n = float(input('Введи следующие число: '))
    lst.append(n)
    if n > max_n:
        max_n = n
    elif n < min_n:
        min_n = n
print(f'Наименьшее из чисел ({lst[0]}, {lst[1]}, {lst[2]}, {lst[3]}, {lst[4]}): {min_n}')
print(f'Наибольшее из чисел ({lst[0]}, {lst[1]}, {lst[2]}, {lst[3]}, {lst[4]}): {max_n}')
