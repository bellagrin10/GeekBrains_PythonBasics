"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для  сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно.
Первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и пр.
"""

import copy


def print_stars(func):
    def wrapper(*args):
        print('***********')
        return func(*args)

    return wrapper


class Matrix:
    def __init__(self, items):
        self.matrix = copy.deepcopy(items)
        self.size = (len(self.matrix), len(self.matrix[0]))

    @print_stars
    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])

    def __add__(self, other):

        if self.size == other.size:
            rows = self.size[0]
            columns = self.size[1]
            new = [[self.matrix[i][j] + other.matrix[i][j] for j in range(columns)] for i in range(rows)]
            print('***********\nNew Matrix:')
            return Matrix(new)
        else:
            msg = 'Matrix sizes do not match:'
            # raise Exception(msg)
            return f'{msg} {self.size} X {other.size}'


if __name__ == '__main__':
    matrix1 = Matrix([[1, 0, 15], [0, 1, 4], [5, 0, 1]])
    matrix2 = Matrix([[8, 1, -2], [0, 2, -4], [2, 10, 0]])
    matrix3 = Matrix([[0, 1], [20, 0], [-1, -2], [4, 6]])
    matrix4 = Matrix([[1, 1], [5, 0], [-10, 1], [0, 6]])
    matrix5 = Matrix([[1, 2, 3, 4], [4, 3, 2, 1]])
    matrix6 = Matrix([[10, 20, 30, 40], [-4, -3, -2, -1]])

    print(matrix1)
    print(matrix2)
    print(matrix1 + matrix2)
    print()
    print(matrix3)
    print(matrix4)
    print(matrix3 + matrix4)
    print()
    print(matrix5)
    print(matrix6)
    print(matrix5 + matrix6)
    print()
    print(matrix1)
    print(matrix3)
    print(matrix1 + matrix3)
