print('Корректный ip-адрес')
print()

while True:
    ip_address = input('Введи ip-адрес: ')
    if len(ip_address.strip()) == 0:
        print('Строка не должна быть пустой')
        print()
    else:
        break
print()

ip_addresses = ip_address.split('.')
flag = True
for el in ip_addresses:
    if not el.isdigit() or not 0 <= int(el) <= 255:
        flag = False
        break
temp = ''
if not flag:
    temp = 'не '
print(f'{ip_address} {temp}является корректным ip-адресом')
