# Special type of thing in python that allow us to pause and resume

# range(100)


def make_list(num):
    result = []
    for i in range(num):
        result.append(i * 2)
    return result


my_list = make_list(100)
print(list(range(100000000)))
