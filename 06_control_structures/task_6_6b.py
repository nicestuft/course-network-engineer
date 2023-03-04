# -*- coding: utf-8 -*-
"""
Задание 6.6b

Сделать копию скрипта задания 6.6a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'.
Сообщение "Неправильный IP-адрес" должно выводиться только один раз после
каждого ввода адреса, даже если несколько пунктов проверки адреса не выполнены
(пример вывода ниже).

Пример выполнения скрипта:
$ python task_6_6b.py
Введите IP-адрес: 10.1.1.1
unicast

$ python task_6_6b.py
Введите IP-адрес: a.a.a
Неправильный IP-адрес
Введите IP-адрес: 10.1.1.1.1
Неправильный IP-адрес
Введите IP-адрес: 500.1.1.1
Неправильный IP-адрес
Введите IP-адрес: a.1.1.1
Неправильный IP-адрес
Введите IP-адрес: 50.1.1.1
unicast

$ python task_6_6b.py
Введите IP-адрес: 10.a.1.1.1
Неправильный IP-адрес
Введите IP-адрес: 255.255.255.255
local broadcast

"""

while True:
	ip = input("Введите IP-адрес: ")
	correct_ip = True

	length_octets = len(ip.split("."))

	if length_octets != 4:
		correct_ip = False
	else:
		for octet in ip.split("."):
			if not (octet.isdigit() and int(octet) in range(256)):
				correct_ip = False
			
	if not correct_ip:
		print("Неправильный IP-адрес")
	else:
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
		break
