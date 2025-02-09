import ifnumber

print('Merge lists 2')
print()

def quick_merge(list1, list2):
    result = []

    p1 = 0  # указатель на первый элемент списка list1
    p2 = 0  # указатель на первый элемент списка list2

    while p1 < len(list1) and p2 < len(list2):  # пока не закончился какой-нибудь из списков
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):  # прицепление остатка
        result += list1[p1:]
    else:  # иначе прицепляем остаток другого списка
        result += list2[p2:]

    return result

def get_num():
    while True:
        num = input('Введи целое положительное число: ')
        if_number = ifnumber.if_number(num)
        if if_number == 'int' and int(num) > 0:
            num = int(num)
            return num
        else:
            print('Данные введены некорректно! Нужно ввести целое положительное число')
            print()

def get_strings(num):
    lst = []
    for i in range(1, num + 1):
        s = get_string(i)
        lst.append(s)
    return lst

def get_string(counter):
    while True:
        s = input(f'Введи {counter}-ю строку с целыми числами: ')
        if len(s.strip()) == 0:
            print('Строка не должна быть пустой')
            print()
        else:
            lst = s.split()
            if_num = if_numbers(lst)
            if if_num:
                return s

def if_numbers(lst):
    for el in lst:
        if ifnumber.if_number(el) != 'int':
            print('Нужно ввести целые числа через пробел')
            return False
    return True

def get_list(s):
    lst = s.split()
    return lst


n = get_num()
strings = get_strings(n)
list_result = [int(el) for el in strings[0].split()]
list_result.sort()
for i in range(len(strings) - 1):
    list1 = list_result
    list2 = [int(el) for el in strings[i + 1].split()]
    list2.sort()
    list_result = quick_merge(list1, list2)
print(*list_result)
