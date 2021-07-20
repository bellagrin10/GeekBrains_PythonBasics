from time import perf_counter
from sys import getsizeof

'''
A list of numbers is presented. It is necessary to display those of its elements,
the values of which are greater than the previous one.
Use the features of python to optimize the code in terms of memory, in terms of speed.
'''

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

# *******************************************
# using list
# *******************************************

start = perf_counter()

result = []
for i, value in enumerate(src):
    if i != 0 and value > src[i - 1]:
        result.append(value)

print(*result, f' speed: {perf_counter() - start}  memory: {getsizeof(result)}')

# *******************************************
# the same with List Comprehensions
# *******************************************

start = perf_counter()

print(*[value for i, value in enumerate(src)
        if i != 0 and value > src[i - 1]],
      f' speed: {perf_counter() - start}  memory: {getsizeof(result)}')


# *******************************************
# same using functions that return generators
# *******************************************

def res_gen(source):
    for index, item in enumerate(source):
        if index != 0 and item > src[index - 1]:
            yield item


start = perf_counter()

result = res_gen(src)

print(*result, f' speed: {perf_counter() - start}  memory: {getsizeof(result)}')

# *******************************************
# the same with Generator Expression
# *******************************************

start = perf_counter()

print(*(value for i, value in enumerate(src)
        if i != 0 and value > src[i - 1]),
      f' speed: {perf_counter() - start}  memory: {getsizeof(result)}')
