print('Алфавит')
print()

lst = []
code_a = ord('a')
div = code_a - 1
for i in range(code_a, ord('z') + 1):
    s = chr(i)
    lst.append(s * (i - div))
print(lst)
