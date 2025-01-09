print('Делаем срезы 2')
print()

while True:
    s = input('Введи строку длиной больше 5 символов: ')
    if len(s) <= 5:
        print('Строка должна быть длиной больше 5 символов')
        print()
    else:
        break
print()
s_3 = s[2]
s_pre_last = s[-2]
s_first_5 = s[:5]
s_without_last_2 = s[:-2]
s_even_index = s[::2]
s_odd_index = s[1::2]
s_revert = s[::-1]
s_revert_odd = s[-1::-2]

print(f'Третий символ строки "{s}": "{s_3}"')
print(f'Предпоследний символ строки "{s}": "{s_pre_last}"')
print(f'Первые пять символов строки "{s}": "{s_first_5}"')
print(f'Строка "{s}", кроме последних двух символов: "{s_without_last_2}"')
print(f'Символы строки "{s}" с чётными индексами: "{s_even_index}"')
print(f'Символы строки "{s}" с нечётными индексами: "{s_odd_index}"')
print(f'Строка "{s}" в обратном порядке: "{s_revert}"')
print(f'Строка "{s}" в обратном порядке через 1 символ: "{s_revert_odd}"')
