from task_11_2 import MyZeroDivisionError


def calculating_an_expression(expression, divisor):
    try:
        if divisor:
            return expression / divisor
        else:
            raise MyZeroDivisionError(calculating_an_expression.__name__, expression, divisor)
    except MyZeroDivisionError as e:
        print('MyZeroDivisionError:', e)


print(calculating_an_expression(5 * 4, 10))
print(calculating_an_expression(5 * 4, 0))
