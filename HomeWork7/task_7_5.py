"""
*Написать скрипт, который выводит статистику для заданной папки в виде словаря,
в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
а значения — кортежи вида (<files_quantity>, [<files_extensions_list>])
<files_quantity> — общее количество файлов (в том числе и в подпапках),
размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
    {
      100: (15, ['txt']),
      1000: (3, ['py', 'txt']),
      10000: (7, ['html', 'css']),
      100000: (2, ['png', 'jpg'])
    }

Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.
"""
import os
import json

def files_quantity(st_size, statistics_dict):
    for key in statistics_dict:
        if st_size < key:
            statistics_dict[key][0] += 1
            return key


def files_extensions_list(ext, statistics_dict, key):
    try:
        statistics_dict[key][1].index(ext)
    except ValueError:
        statistics_dict[key][1].append(ext)


given_folder = os.getcwd()   # можно ввести путь до любой папки

limit = 1
limit_size = [limit := limit * 10 for _ in range(10)]

statistics_dict_for_a_given_folder = {limit: [0, []] for limit in limit_size}

for root, dirs, files in os.walk(given_folder):
    for file in files:
        if not file.startswith('.'):
            rel_path = os.path.join(root, file)
            try:
                size = os.stat(rel_path).st_size
                limit_key = files_quantity(size, statistics_dict_for_a_given_folder)
                extension = file.rsplit('.', maxsplit=1)[-1].lower()
                files_extensions_list(extension, statistics_dict_for_a_given_folder, limit_key)
            except FileNotFoundError as e:
                print(e)

# при работе с json не различаются списки и кортежи: если создадим кортеж - на выходе получим список.
with open('task_7_5_summary.json', 'w', encoding='utf-8') as f:
    json.dump(statistics_dict_for_a_given_folder, f)
