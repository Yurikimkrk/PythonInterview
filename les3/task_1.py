"""
1. Написать программу, которая будет содержать функцию
для получения имени файла из полного пути до него.

При вызове функции в качестве аргумента должен передаваться путь до файла.
В функции необходимо реализовать «выделение» из этого пути имени файла (без расширения).

Пример:
функция принмает следующую строку - '../mainapp/views.py'

Результат:
views
"""
import re


# Наверно проще было без Lookahead и Lookbehind, так как можно просто взять
# последнее вхождение чз -1
def get_file_name(path):
    return re.findall(r'(?<=[\/])([\wа-яА-я\-\. ]+)(?=\.\w+[^\/]$)', path)[-1]


print(get_file_name('../mainapp/views.py'))
