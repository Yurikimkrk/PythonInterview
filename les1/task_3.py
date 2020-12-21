"""
Задание 3.	Разработать генератор случайных чисел.
В функцию передавать начальное и конечное число генерации
(нуль необходимо исключить). Заполнить этими данными список и словарь.
Ключи словаря должны создаваться по шаблону: “elem_<номер_элемента>”.
Вывести содержимое созданных списка и словаря.

Пример:
(
[18, 22, 21, 23, 18, 21, 19, 16, 18, 8],
{'elem_18': 18, 'elem_22': 22, 'elem_21': 21, 'elem_23': 23, 'elem_19': 19, 'elem_16': 16, 'elem_8': 8}
)
"""
from random import random

NUMBER_OF_NUMBERS = 10


def generator(first, last):
    gen_list, gen_dict = [], {}
    for i in range(NUMBER_OF_NUMBERS):
        number = round(first + (last - first) * random())
        gen_list.append(number)
        gen_dict.update({f'elem_{number}': number})
    print(gen_list)
    print(gen_dict)


generator(1, 100)
