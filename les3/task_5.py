"""
5. Усовершенствовать первую функцию из предыдущего примера.

Необходимо просканировать текстовый файл, созданный на предыдущем задании
и реализовать создание и запись нового текстового файла

В новый текстовый файл обеспечить запись строк вида:

zmsebjvdgi zmsebjvdgi
ychpwljtzn ychpwljtzn
...

Т.е. извлекаются строки из первого текстового файла
а в новый они записываются в виде, где вместо числа ставится строка

Здесь необходимо использовать регулярные выражения.
"""
from re import findall


def create_new_file(file):
    with open(file, 'r', encoding='utf-8') as dscr:
        with open("task5file.txt", 'w', encoding='utf-8') as new_dscr:
            for line in dscr:
                string = findall(r'(?<=[ ])[a-z]+', line)[-1]
                new_dscr.write(f'{string} {string}\n')


create_new_file("task4file.txt")
