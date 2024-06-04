print('Расстояние в метрах')
print()
while True:
    cm = input('Введи количество сантиметров: ')
    if cm.isdigit():
        m = int(cm) / 100
        print(f'{cm} сантиметров - это {m} метров')
        break
    else:
        print('Нужно ввести целое неотрицательное число')
        print()
        