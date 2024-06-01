print('Пересчёт временного интервала')
print()

while True:
    minutes = input('Введи количество минут: ')  # 65
    print()
    if minutes.isdigit():
        minutes = int(minutes)
        hours = minutes // 60
        minutes_left = minutes % 60
        print(f'{minutes} мин - это {hours} час {minutes_left} минут.')
        break
    else:
        print('Нужно ввести положительное целое число')
        print()
