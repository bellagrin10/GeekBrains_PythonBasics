"""
Осуществить программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс «Клетка».
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__floordiv__()).
Эти методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и
округление до целого числа деления клеток соответственно.
Сложение:
Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание:
Участвуют две клетки. Операцию необходимо выполнять, только если разность количества ячеек двух клеток больше нуля,
иначе выводить соответствующее сообщение.
Умножение:
Создаётся общая клетка из двух. Число ячеек общей клетки — произведение количества ячеек этих двух клеток.
Деление:
Создаётся общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих
двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Этот метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, а количество ячеек в ряду — 5.
В этом случае метод make_order() вернёт строку: *****\n*****\n**.
Или количество ячеек клетки — 15, а количество ячеек в ряду равняется 5.
Тогда метод make_order() вернёт строку: *****\n*****\n*****.
"""


class Cell:
    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        result = self.cells - other.cells
        if result > 0:
            return Cell(result)
        else:
            print('Operation of difference of two cells is not possible')
            return Cell(None)

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __floordiv__(self, other):
        return Cell(self.cells // other.cells)

    def make_order(self, number_of_cells_in_a_row):
        string_of_cells = ''
        if self.cells:
            number_of_full_rows = self.cells // number_of_cells_in_a_row
            number_of_cells_in_the_last_row = self.cells % number_of_cells_in_a_row

            string_of_cells = '\\n'.join('*' * number_of_cells_in_a_row for _ in range(number_of_full_rows))
            if string_of_cells and number_of_cells_in_the_last_row:
                string_of_cells += '\\n'
            string_of_cells += '*' * number_of_cells_in_the_last_row
        return string_of_cells


if __name__ == '__main__':
    cell1 = Cell(4)
    cell2 = Cell(6)
    print(cell1.cells, cell1.make_order(3))
    print(cell2.cells, cell2.make_order(3))
    print((cell1 + cell2).cells, (cell1 + cell2).make_order(4))
    print((cell1 - cell2).cells), (cell1 - cell2).make_order(1)
    print((cell1 * cell2).cells, (cell1 * cell2).make_order(5))
    print((cell1 // cell2).cells, (cell1 // cell2).make_order(2))
    print((cell2 // cell1).cells, (cell2 // cell1).make_order(2))
