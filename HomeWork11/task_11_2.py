"""
Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверить его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyZeroDivisionError(BaseException):
    def __init__(self, function, expression, divisor):
        msg = f'division by zero\nin {function}\n {expression=} / {divisor=}'
        super().__init__(msg)
