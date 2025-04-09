import random

print('Подбрасывание монеты')
print()

for _ in range(10):
    n = random.randint(0, 1)
    if n == 0:
        print('Орёл')
    else:
        print('Решка')