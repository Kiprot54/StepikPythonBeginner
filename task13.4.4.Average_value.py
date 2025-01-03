print('Среднее значение')
print()

def compute_average(numbers):
    total = sum(numbers)
    numbers_len = len(numbers)
    middle = total / numbers_len
    return middle

numbers = [1, 3, 5, 1, 6, 8, 10, 2]

print(compute_average(numbers))
