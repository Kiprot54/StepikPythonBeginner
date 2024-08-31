def if_number(n):
    if len(n) > 0:
        # Если возможное число отрицательное - избавляемся от минуса
        if n[0] == '-':
            n = n[1:]

        # Подсчитываем количество точек в строке
        count_dot = n.count('.')

        if count_dot > 1:
            return False
        else:
            if n.count('.') == 1:
                index_dot = n.find('.')
                if index_dot != len(n) - 1:
                    # Если в строке одна точка, и она не последний символ, делим эту строку на две: до точки и после
                    n1 = n[:index_dot]
                    n2 = n[index_dot + 1:]

                    # Проверяем, являются ли строки целыми числами
                    if n1.isdigit() and n2.isdigit():
                        return 'float'
                    else:
                        return False
                else:
                    return False
            else:
                # Если в строке нет точек - проверяем, является ли строка целым числом
                if n.isdigit():
                    return 'int'
                else:
                    return False
    else:
        return False
