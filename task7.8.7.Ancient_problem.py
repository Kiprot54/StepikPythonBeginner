print('Старинная задача')
print()

for x in range(0, 101):
    for y in range(0, 101 - x):
        for z in range(0, 101 - x - y):
            if x + y + z == 100 and 10 * x + 5 * y + 0.5 * z == 100:
                print(f'Покупая 100 голов скота на 100 долларов, можно купить {x} быков, {y} коров, {z} телят')
