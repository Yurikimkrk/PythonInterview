"""
Задание 2.	Дополнить следующую функцию недостающим кодом:
def print_directory_contents(sPath):
    Функция принимает имя каталога и распечатывает его содержимое
    в виде «путь и имя файла», а также любые другие
    файлы во вложенных каталогах.
    Эта функция подобна os.walk. Использовать функцию os.walk
    нельзя. Данная задача показывает ваше умение работать с
    вложенными структурами.
    заполните далее
Пример:
[
('mainapp', 'admin.py'),
('mainapp\\management\\commands', 'seed_db.py'),
...
]
"""
import os


def print_directory_contents(path):
    def get_content(path):
        content = []
        for element in os.listdir(path):
            full_path = os.path.join(os.path.abspath(path), element)
            if os.path.isfile(full_path):
                content.append((os.path.abspath(path), element))
            else:
                content.append(get_content(full_path))
        return content

    return get_content(path)


print(print_directory_contents('../les1'))
