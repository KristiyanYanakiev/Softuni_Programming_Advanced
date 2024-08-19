# def multiply(*numbers):
#     total = 1
#     for num in numbers:
#         total *= num
#
#     return total
from functools import reduce


def multiply(*nums):
    return reduce(lambda x, y: x * y, nums)

