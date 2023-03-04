# -*- coding: utf-8 -*-
"""
Задание 6.6a

Сделать копию скрипта задания 6.6.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделены точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: "Неправильный IP-адрес".
Если адрес правильный, проверять и выводить тип адреса как в задании 6.6.

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Пример выполнения скрипта:
$ python task_6_6a.py
Введите IP-адрес: 10.10.1.1
unicast

$ python task_6_6a.py
Введите IP-адрес: 10.1.1
Неправильный IP-адрес

$ python task_6_6a.py
Введите IP-адрес: a.a.10.1
Неправильный IP-адрес

$ python task_6_6a.py
Введите IP-адрес: 50.1.a.a
Неправильный IP-адрес

$ python task_6_6a.py
Введите IP-адрес: 10,1,1,1
Неправильный IP-адрес

$ python task_6_6a.py
Введите IP-адрес: 500.1.1.1
Неправильный IP-адрес

$ python task_6_6a.py
Введите IP-адрес: 50.1.1.1.1
Неправильный IP-адрес
"""

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
		
