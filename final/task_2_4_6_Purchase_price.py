print('Стоимость покупки')
print()
while True:
    monitor = input('Введи стоимость монитора: ')

    if monitor.isdigit():
        monitor = int(monitor)
        break
    else:
        print('Нужно ввести целое положительное число')
        print()
while True:
    system_block = input('Введи стоимость системного блока: ')

    if system_block.isdigit():
        system_block = int(system_block)
        break
    else:
        print('Нужно ввести целое положительное число')
        print()
while True:
    keyboard = input('Введи стоимость клавиатуры: ')

    if keyboard.isdigit():
        keyboard = int(keyboard)
        break
    else:
        print('Нужно ввести целое положительное число')
        print()
while True:
    mouse = input('Введи стоимость мыши: ')

    if mouse.isdigit():
        mouse = int(mouse)
        break
    else:
        print('Нужно ввести целое положительное число')
        print()
print()
print(f'Стоимость 1 монитора: {monitor};')
print(f'Стоимость 1 системного блока: {system_block};')
print(f'Стоимость 1 клавиатуры: {keyboard};')
print(f'Стоимость 1 мыши: {mouse};')
print(f'Стоимость 3 компьютеров: {(monitor + keyboard + mouse + system_block) * 3}.')
