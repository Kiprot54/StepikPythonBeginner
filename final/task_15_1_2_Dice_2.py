import random

print('Игральные кубики 2')
print()

repeat = 'y'
while repeat == 'y':
    print(random.randint(1, 6))
    print(random.randint(1, 6))
    print()
    repeat = input('Будешь бросать кубики ещё раз? Да(y) или нет(n) ')