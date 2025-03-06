import ifnumber

print('Калькулятор доставки')
print()

def get_shipping_cost(quantity):
    num = 1000
    if quantity != 1:
        for i in range(2, quantity + 1):
            num += 1
    return num

def get_num():
    while True:
        num = input('Введи количество товаров в заказе: ')
        if_number = ifnumber.if_number(num)
        if if_number == 'int' and int(num) > 0:
            num = int(num)
            return num
        else:
            print('Данные введены некорректно! Нужно ввести целое положительное число')
            print()

n = get_num()

print(get_shipping_cost(n))