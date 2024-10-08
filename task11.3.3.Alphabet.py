print('Алфавит')
print()

lst = []
for i in range(26):
    s = ''
    for j in range(i + 1):
        s += chr(ord('a') + i)
    lst.append(s)
print(lst)