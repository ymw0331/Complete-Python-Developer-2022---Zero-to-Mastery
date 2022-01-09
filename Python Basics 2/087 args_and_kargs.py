# *args **kwargs

# args allow us to give any numbers of positional arguments
# args inside of a function is a tuple of arguments

def super_func(name, *args, i='hi', **kwargs):
    # print(kwargs)
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total


print(super_func('andy', 1, 2, 3, 4, 5, num1=5, num2=10))

# Rule: params, *args, default parameters, **kwargs
