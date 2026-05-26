def get_int(text):
    while True:
        try:
            n = int(input(f'{text}'))
            return n
        except ValueError:
            print('Нужно ввести целое число')
