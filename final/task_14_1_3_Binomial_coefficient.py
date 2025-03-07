import ifnumber

print('')
print()

def compute_binom(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

def get_number():
    while True:
        n = input('Введи целое положительное число: ')
        if_number = ifnumber.if_number(n)
        if if_number == 'int' and int(n) > 0:
            n = int(n)
            return n
        else:
            print('Данные введены некорректно! Нужно ввести целое положительное число')
            print()

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

n = get_number()
k = get_number()

# print(f'{n}! / ({k}! * ({n} - {k})!) = {compute_binom(n, k)}')
print(f'     {n}!')
print(f'------------------    = {compute_binom(n, k)}')
print(f'{k}! * ({n} - {k})!')
