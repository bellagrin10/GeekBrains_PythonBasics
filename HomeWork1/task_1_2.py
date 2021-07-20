"""
Create a list of cubes of odd numbers from 1 to 1000:
a. Calculate the sum of those numbers from this list, the sum of the digits of which is evenly divisible by 7.
For example, the number "19 ^ 3 = 6859" will be included in the sum, since 6 + 8 + 5 + 9 = 28 is evenly divisible by 7.
Attention: use only arithmetic operations!
b. Add 17 to each element of the list and recalculate the sum of those numbers from this list,
the sum of the digits of which is divisible by 7.
c. * Solve the problem under point b without creating a new list.
"""


def is_the_sum_of_digits_divisible_by_7(digits):
    sum_of_digits = 0
    while digits > 0:
        sum_of_digits += digits % 10
        digits //= 10
    if sum_of_digits % 7 == 0:
        return True


def sum_of_numbers_by_condition(numbers, condition, task=''):
    sum_of_numbers = 0
    for number in numbers:
        if task == '*':
            number += 17
        if condition(number):
            sum_of_numbers += number
    return sum_of_numbers


odd_numbers_cubed = [number ** 3 for number in range(1, 1001)]
# a.
print(sum_of_numbers_by_condition(odd_numbers_cubed, is_the_sum_of_digits_divisible_by_7))
# c.*
print(sum_of_numbers_by_condition(odd_numbers_cubed, is_the_sum_of_digits_divisible_by_7, '*'))
# b.
odd_numbers_cubed_plus_17 = [number ** 3 + 17 for number in range(1, 1001)]
print(sum_of_numbers_by_condition(odd_numbers_cubed_plus_17, is_the_sum_of_digits_divisible_by_7))
