import ifnumber

print('Merge lists 1')
print()

def merge(list1, list2):
    lst = list1 + list2
    lst.sort()
    return lst

def get_string():
    while True:
        s = input('Введи целые числа через пробел: ')
        if len(s.strip()) == 0:
            print('Строка не должна быть пустой')
            print()
        else:
            return s

def create_list(s):
    numbers = s.split()
    return numbers

def if_numbers(lst):
    for el in lst:
        if ifnumber.if_number(el) != 'int':
            print('Нужно ввести целые числа через пробел')
            return False
    return True

def get_list():
    while True:
        s = get_string()
        lst = create_list(s)
        numbers = if_numbers(lst)
        if numbers:
            new_lst = convert_list(lst)
            new_lst.sort()
            return new_lst

def convert_list(lst):
    for i in range(len(lst)):
        lst[i] = int(lst[i])
    return lst

list1 = get_list()
list2 = get_list()

print(merge(list1, list2))
