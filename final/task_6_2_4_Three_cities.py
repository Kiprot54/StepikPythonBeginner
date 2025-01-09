print('Три города')
print()
city_name_1 = input('Введи название первого города: ')
city_name_2 = input('Введи название второго города: ')
city_name_3 = input('Введи название третьего города: ')
len_city_name_1 = len(city_name_1)
len_city_name_2 = len(city_name_2)
len_city_name_3 = len(city_name_3)
if len_city_name_1 > len_city_name_3:
    len_city_name_max = len_city_name_1
    len_city_name_min = len_city_name_3
    city_name_max = city_name_1
    city_name_min = city_name_3
else:
    len_city_name_max = len_city_name_3
    len_city_name_min = len_city_name_1
    city_name_max = city_name_3
    city_name_min = city_name_1
if len_city_name_2 > len_city_name_max:
    len_city_name_max = len_city_name_2
    city_name_max = city_name_2
elif len_city_name_2 < len_city_name_min:
    len_city_name_min = len_city_name_2
    city_name_min = city_name_2
print(f'Из трёх городов {city_name_1}, {city_name_2}, {city_name_3} самое короткое название у города {city_name_min} - {len_city_name_min} букв')
print(f'Из трёх городов {city_name_1}, {city_name_2}, {city_name_3} самое длинное название у города {city_name_max} - {len_city_name_max} букв')
