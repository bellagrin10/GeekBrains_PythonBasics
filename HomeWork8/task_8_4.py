"""
Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции и
выбрасывать исключение ValueError, если что-то не так, например:
def val_checker...
    ...

@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3

a = calc_cube(5)
Вывод:
125
a = calc_cube(-5)
Вывод:
Traceback (most recent call last):
  ...
    raise ValueError(msg)
ValueError: wrong val -5

Примечание: сможете ли вы замаскировать работу декоратора?
"""
from functools import wraps


def val_checker(condition):
    try:
        def execute_function(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                nonlocal condition
                if condition(args[0]):
                    return func(*args, **kwargs)
                else:
                    msg = f'wrong val {args[0]}'
                    raise ValueError(msg)
            return wrapper
        return execute_function
    except ValueError as e:
        print(e)


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(5))
print(calc_cube(-5))
