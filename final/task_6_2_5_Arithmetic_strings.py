print('Арифметические строки')
print()
s1 = input('Введи первую строку: ')
s2 = input('Введи вторую строку: ')
s3 = input('Введи третью строку: ')
len_s1 = len(s1)
len_s2 = len(s2)
len_s3 = len(s3)
if len_s1 > len_s2:
    max_len_s = len_s1
    min_len_s = len_s2
else:
    max_len_s = len_s2
    min_len_s = len_s1
if len_s3 > max_len_s:
    middle_len_s, max_len_s = max_len_s, len_s3
elif len_s3 < min_len_s:
    middle_len_s, min_len_s = min_len_s, len_s3
else:
    middle_len_s = len_s3
if middle_len_s - min_len_s == max_len_s - middle_len_s:
    print(f'Длины строк <{s1}>, <{s2}>, <{s3}> составляют арифметическую прогрессию')
else:
    print(f'Длины строк <{s1}>, <{s2}>, <{s3}> не составляют арифметическую прогрессию')
