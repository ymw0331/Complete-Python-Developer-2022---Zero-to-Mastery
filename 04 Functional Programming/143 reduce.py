# Reduce
from functools import reduce

my_list = [1, 2, 3]
# your_list = (10, 20, 30)
# their_list = (5, 4, 3)


def multiply_by2(item):
    return item * 2


def check_odd(item):
    return item % 2 != 0


def accumlator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumlator, my_list, 10))
