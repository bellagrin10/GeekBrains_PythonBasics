"""
Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp


Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?
"""

import os


def make_path(dir_name, name):
    return os.path.join(dir_name, name)


def make_dir(path):
    os.makedirs(path, exist_ok=True)


def make_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


if __name__ == '__main__':
    MY_PROJECT_PATH = os.getcwd()
    SETTINGS_PATH = make_path('my_project', 'settings')
    MAIN_APP_PATH = make_path('my_project', 'mainapp')
    ADMIN_APP_PATH = make_path('my_project', 'adminapp')
    AUTH_APP_PATH = make_path('my_project', 'authapp')

    # для абсолютного пути:
    # make_path(MY_PROJECT_PATH, SETTINGS_PATH)
    # make_path(MY_PROJECT_PATH, MAIN_APP_PATH)
    # make_path(MY_PROJECT_PATH, ADMIN_APP_PATH)
    # make_path(MY_PROJECT_PATH, AUTH_APP_PATH)

    make_dir(SETTINGS_PATH)
    make_dir(MAIN_APP_PATH)
    make_dir(ADMIN_APP_PATH)
    make_dir(AUTH_APP_PATH)

    # для создания вложенных файлов,
    # например, создать файл test.txt внутри папки settings:
    # name_path = make_path(SETTINGS_PATH, 'test.txt')
    # make_file(name_path)
