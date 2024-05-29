while True:
    cm = input('Введи количество сантиметров: ')
    if cm.isdigit():
        m = int(cm) / 100
        print(m)
        break
    else:
        print('Нужно ввести целое положительное число')
        print()