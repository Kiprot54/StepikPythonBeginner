def get_int(text):
    while True:
        try:
            n = int(input(f'{text}'))
            return n
        except ValueError:
            print('Нужно ввести целое число')

def get_float(text):
    while True:
        try:
            n = float(input(f'{text}'))
            return n
        except ValueError:
            print('Нужно ввести число')
