print('Список палиндромов')
print()

palindroms = [i for i in range(100, 1001) if str(i) == str(i)[::-1]]

print(palindroms)
