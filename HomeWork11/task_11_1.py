"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода:
Первый — с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй — с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""
import datetime


class Date:
    @classmethod
    def str_date_to_integer(cls, date_as_string):
        day, month, year = date_as_string.split('-')
        cls.date_as_int = tuple(map(int, [year, month, day]))
        return cls.date_as_int

    @staticmethod
    def date_validation(int_date):
        is_valid_date = True
        try:
            datetime.datetime(*int_date)
        except ValueError:
            is_valid_date = False

        if is_valid_date:
            print("Input date is valid.")
        else:
            print("Input date is not valid.")


# Enter the date in format 'dd-mm-yy')
input_date = Date.str_date_to_integer('20-02-2002')
print(*input_date, sep='-')
Date.date_validation(input_date)
input_date = Date.str_date_to_integer('30-02-2002')
print(*input_date, sep='-')
Date.date_validation(input_date)
