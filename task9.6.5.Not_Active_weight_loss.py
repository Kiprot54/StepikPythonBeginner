import ifnumber

print('(Не) Активное похудение')
print()

while True:
    day = input('Какой по счёту день похудения? ')
    if_number = ifnumber.if_number(day)
    if if_number == 'int' and 1 <= int(day) <= 60:
        day = int(day)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное число от 1 до 60')
        print()

while True:
    weight = input('Какой вес в этот день? ')
    if_number = ifnumber.if_number(weight)
    if if_number == 'int' and int(weight) > 0:
        weight = int(weight)
        break
    elif if_number == 'float' and float(weight) > 0:
        weight = float(weight)
        break
    else:
        print('Данные введены некорректно! Нужно ввести положительное число')
        print()
print()
start_plan_weight = 100
end_plan_weight = 88
max_days = 60
one_day_plan_lose_weight = (100 - 88) / 60
day_plan_lose_weight = 100 - one_day_plan_lose_weight * day
print(f'#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {weight} кг, ЦЕЛЬ по ВЕСУ = {day_plan_lose_weight} кг.')
if day_plan_lose_weight >= weight:
    print('Всё идет по плану')
else:
    print('Что-то пошло не так')

