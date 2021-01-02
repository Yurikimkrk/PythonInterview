"""
4. Написать программу, в которой реализовать две функции.

В первой должен создаваться простой текстовый файл.
Если файл с таким именем уже существует, выводим соответствующее сообщение.

Необходимо открыть файл и подготовить два списка: с текстовой и числовой информацией.
Например:
[91, 42, 47, 64, 60, 23, 82, 78, 22, 15]
и
['zmsebjvdgi', 'ychpwljtzn', 'zqywoopbwf', 'nkxdnnqyhe', 'eqpbrjwjdp',
'sllbegvgmh', 'kzrmrozeco', 'jbppumpypu', 'jjsmronkvm', 'qtnspcleqd']


Для создания списков использовать генераторы. Применить к спискам функцию zip().
Результат выполнения этой функции должен должен быть обработан и записан в файл таким образом,
чтобы каждая строка файла содержала текстовое и числовое значение.
Например:
91 zmsebjvdgi

42 ychpwljtzn

...

Первая функция должна возвращать ссылку на файловый дескриптор


После вызова первой функции возвращаемый файловый дескриптор нужно передавать во вторую функцию
Во второй функции необходимо реализовать открытие файла и простой построчный вывод содержимого.
"""

from os import path
from random import randint


def create_file(file):
    if path.exists(file):
        with open(file, 'r', encoding='utf-8') as dscr:
            return dscr
    with open(file, 'w', encoding='utf-8') as dscr:
        numbers = [randint(10, 100) for _ in range(25)]
        strings = [
            ''.join(([chr(randint(ord('a'), ord('z'))) for _ in range(10)])) for
            _ in range(25)]
        dscr.writelines(['{} {}\n'.format(number, string)
                         for number, string in zip(numbers, strings)])
        return dscr


def open_file(descriptor):
    with open(descriptor.name, 'r', encoding='utf-8') as dscr:
        for i in dscr:
            print(i)


open_file(create_file("task4file.txt"))
