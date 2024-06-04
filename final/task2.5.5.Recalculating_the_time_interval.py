print('Пересчёт временного интервала')
print()

while True:
    minutes = input('Введи количество минут: ')
    print()
    if minutes.isdigit():
        minutes = int(minutes)
        hours = minutes // 60
        minutes_left = minutes % 60
        print(f'{minutes} минут - это {hours} час {minutes_left} минут.')
        break
    else:
        print('Нужно ввести неотрицательное целое число')
        print()
