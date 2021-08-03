"""
Дан стартер для проекта со следующей структурой:
|--my_project
   |--settings
   |  |--__init__.py
   |  |--dev.py
   |  |--prod.py
   |--mainapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--mainapp
   |        |--base.html
   |        |--index.html
   |--authapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--authapp
   |        |--base.html
   |        |--index.html

Написать скрипт, который собирает все шаблоны в одну папку templates, например:
|--my_project
   ...
   |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html


Примечание: исходные файлы необходимо оставить;
обратите внимание, что html-файлы расположены в родительских папках (они играют роль пространств имён);
предусмотреть возможные исключительные ситуации;
"""
import os
import shutil
from task_7_1 import make_path

destination = make_path('my_project', 'templates')
for root_dir, list_dir, files in os.walk('my_project'):
    if list_dir == ['templates']:
        source = make_path(root_dir, 'templates')
        print(source)
        shutil.copytree(source, destination, dirs_exist_ok=True)
