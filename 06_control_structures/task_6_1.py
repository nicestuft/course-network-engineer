# -*- coding: utf-8 -*-
"""
Задание 6.1

Список mac содержит MAC-адреса в формате XXXX:XXXX:XXXX однако, в оборудовании Cisco
MAC-адреса используются в формате XXXX.XXXX.XXXX

Написать код, который преобразует MAC-адреса в формат cisco и добавляет их в новый
список result (тест будет проверять переменную result).
Полученный список result вывести на стандартный поток вывода (stdout) с помощью print.

Пример итогового вывода:
$ python task_6_1.py
['aabb.cc80.7000', 'aabb.dd80.7340', 'aabb.ee80.7000', 'aabb.ff80.7000']

Список mac нельзя менять вручную, все изменения надо делать с помощью Python.
"""

mac = ["aabb:cc80:7000", "aabb:dd80:7340", "aabb:ee80:7000", "aabb:ff80:7000"]
result = []

for i in mac:
	result.append(i.replace(":", "."))
	
print(result)
	

