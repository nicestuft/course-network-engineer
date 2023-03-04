# -*- coding: utf-8 -*-
"""
Задание 6.6

Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223 (пример адреса 50.1.1.1)
   'multicast' - если первый байт в диапазоне 224-239 (пример адреса 224.1.1.1)
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Пример выполнения скрипта:
$ python task_6_6.py
Введите IP-адрес: 10.1.1.1
unicast

$ python task_6_6.py
Введите IP-адрес: 224.1.1.1
multicast

$ python task_6_6.py
Введите IP-адрес: 0.0.0.0
unassigned

$ python task_6_6.py
Введите IP-адрес: 255.255.255.255
local broadcast

$ python task_6_6.py
Введите IP-адрес: 250.1.1.1
unused

"""

ip = input("Введите IP-адрес: ")

first_octet = int(ip.split(".")[0])

if 1 <= first_octet <= 223:
	print("unicast")
elif 224 <= first_octet <= 239:
	print("multicast")
elif ip == "255.255.255.255":
	print("local broadcast")
elif ip == "0.0.0.0":
	print("unassigned")
else:
	print("unused")
