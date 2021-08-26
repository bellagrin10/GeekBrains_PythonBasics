"""
Создать собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере.
Запрашивать у пользователя данные и заполнять список необходимо только числами.
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
скрипта, введя, например, команду «stop».
При этом скрипт завершается, сформированный список с числами выводится на экран.
Подсказка: для этого задания примем, что пользователь может вводить только числа и строки.
Во время ввода пользователем очередного элемента необходимо реализовать проверку типа элемента.
Вносить его в список, только если введено число.
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
При этом работа скрипта не должна завершаться.
"""


class OnlyNumbersError(Exception):
    def __init__(self):
        msg = f'OnlyNumbersError: expected number not string'
        super(OnlyNumbersError, self).__init__(msg)


def to_number(num):
    if num.isdigit():
        return int(num)
    else:
        try:
            return float(num)
        except ValueError:
            try:
                if num != 'stop':
                    raise OnlyNumbersError()
            except OnlyNumbersError as e:
                print(e)


number_list = []
input_data = ''
while input_data != 'stop':
    input_data = input('Enter a number: ')
    number = to_number(input_data)
    if number:
        number_list.append(number)
print(f'Formed list with numbers: {number_list}')
