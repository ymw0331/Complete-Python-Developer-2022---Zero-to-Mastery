# Tuples (immutable lists)

my_tuple = (1, 2, 3, 4, 5)
# print(my_tuple[1])
# print(5 in my_tuple)

# makes code predictable, more performance than list

user = {
    (1, 2): [1, 2, 3],
    'greet': 'hello',
    'age': 20
}

print(user[(1, 2)])
