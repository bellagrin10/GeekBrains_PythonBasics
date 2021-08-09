"""
Написать декоратор для логирования типов позиционных аргументов функции, например:
def type_logger...
    ...

@type_logger
def calc_cube(x):
   return x ** 3

a = calc_cube(5)
Вывод:
5: <class 'int'>

Примечание: если аргументов несколько - выводить данные о каждом через запятую;
можете ли вы вывести тип значения функции? Сможете ли решить задачу для именованных аргументов?
Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя функции, например, в виде:
a = calc_cube(5)
Вывод:
calc_cube(5: <class 'int'>)
"""
from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_type = {arg: type(arg) for arg in args}
        kwargs_type = {kwargs[kwarg]: type(kwargs[kwarg]) for kwarg in kwargs}
        func_result_type = {func(*args, **kwargs): type(func(*args, **kwargs))}
        result_types = {**args_type, **kwargs_type, **func_result_type}
        result = f'{func.__name__}{result_types}'.replace('{', '(').replace('}', ')')
        return result
    return wrapper


@type_logger
def calc_pow(num, power, msg, flag):
    if flag:
        return f'{msg} {num ** power}'
    return num ** power


print(calc_pow(5, -2, msg='Result:', flag=False))
print(calc_pow(-2.5, 2, msg='Result:', flag=True))
