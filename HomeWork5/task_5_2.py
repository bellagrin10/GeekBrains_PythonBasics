from random import randint

'''
* Solve the problem of generating odd numbers from 1 to n (inclusive) without using the yield keyword.
'''
n = randint(1, 100)
print(n)
odd_numbers = (number for number in range(1, n+1, 2))
print(*odd_numbers)
