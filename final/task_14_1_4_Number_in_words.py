import ifnumber

print('Число словами')
print()

def number_to_words(num):
    if num >= 100:
        return 'Число должен быть меньше 100'
    else:
        digits = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
        digits_20 = ['', 'один', 'две', 'три', 'четыр', 'пят', 'шест', 'сем', 'восем', 'девят']
        numbers_10 = ['', 'десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
        if 1 <= num <= 9:
            return digits[num]
        elif 11 <= num <= 19:
            return digits_20[num % 10] + 'надцать'
        else:
            first_digit = num // 10
            last_digit = num % 10
            if last_digit == 0:
                return numbers_10[first_digit]
            else:
                return numbers_10[first_digit] + ' ' + digits[last_digit]

def get_num():
    while True:
        num = input('Введи целое положительное число до 100: ')
        if_number = ifnumber.if_number(num)
        if if_number == 'int' and 1 <= int(num) <= 99:
            num = int(num)
            return num
        else:
            print('Данные введены некорректно! Нужно ввести целое положительное число до 100')
            print()

n = get_num()
print(number_to_words(n))