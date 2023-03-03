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
