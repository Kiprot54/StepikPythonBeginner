print('Цветовой микшер')
print()
color_1 = input('Введи первый цвет: ').lower()
color_2 = input('Ведди второй цвет: ').lower()
print()

if color_1 == 'желтый':
    color_1 = 'жёлтый'
if color_2 == 'желтый':
    color_2 = 'жёлтый'

if (color_1 == 'красный' and color_2 == 'синий') or (color_1 == 'синий' and color_2 == 'красный'):
    print(f'При смешивании цветов {color_1} и {color_2} получается фиолетевый')
elif (color_1 == 'красный' and color_2 == 'жёлтый') or (color_1 == 'жёлтый' and color_2 == 'красный'):
    print(f'При смешивании цветов {color_1} и {color_2} получается оранжевый')
elif (color_1 == 'синий' and color_2 == 'жёлтый') or (color_1 == 'жёлтый' and color_2 == 'синий'):
    print(f'При смешивании цветов {color_1} и {color_2} получается зелёный')
elif color_1 == 'красный' and color_2 == 'красный':
    print(f'При смешивании цветов {color_1} и {color_2} получается красный')
elif color_1 == 'синий' and color_2 == 'синий':
    print(f'При смешивании цветов {color_1} и {color_2} получается синий')
elif color_1 == 'жёлтый' and color_2 == 'жёлтый':
    print(f'При смешивании цветов {color_1} и {color_2} получается жёлтый')
else:
    print('Такие цвета я не умею смешивать')
