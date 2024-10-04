print('Все сразу 1')
print()

numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
len_numbers = len(numbers)
last_element = numbers[-1]
reverse_numbers = numbers[::-1]
if 5 in numbers and 17 in numbers:
    is_5_and_17 = 'Числа 5 и 17 есть в списке'
else:
    is_5_and_17 = 'Чисел 5 и 17 нет в списке'
del numbers[0]
del numbers[-1]
print(len_numbers)
print(last_element)
print(reverse_numbers)
print(is_5_and_17)
print(numbers)