def highest_even(li):
    evens = []  # create a list
    for item in li:
        if item % 2 == 0:
            evens.append(item)  # add the even number to te evens list
    return max(evens)


print(highest_even([10, 2, 3, 4, 8, 11]))
