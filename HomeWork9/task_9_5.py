"""
Реализовать класс Stationery (канцелярская принадлежность):
- определить в нём атрибут title (название) и метод draw (отрисовка).
  Метод выводит сообщение «Запуск отрисовки»;
- создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
- в каждом классе реализовать переопределение метода draw.
  Для каждого класса метод должен выводить уникальное сообщение;
- создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


def print_stars(func):
    def wrapper(*args):
        print('*************************************************')
        return func(*args)
    return wrapper


class Stationery:
    def __init__(self, title):
        self.title = title

    @print_stars
    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, *args):
        super().__init__(*args)

    def draw(self):
        super().draw()
        print(f'Для зарисовки используется {self.title}.')


class Pencil(Stationery):
    def __init__(self, *args):
        super().__init__(*args)

    def draw(self):
        super().draw()
        print(f'Для эскиза используется {self.title}.')


class Handle(Stationery):
    def __init__(self, *args):
        super().__init__(*args)

    def draw(self):
        super().draw()
        print(f'Для выделения и подчеркивания используется {self.title}.')


stationery = Stationery('перо')
stationery.draw()
print(stationery.title)
pen = Pen('ручка')
pen.draw()
pencil = Pencil('карандаш')
pencil.draw()
handle = Handle('маркер')
handle.draw()
