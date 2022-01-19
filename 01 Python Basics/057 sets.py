# Sets (unordered collection of unique objects)
my_list = [1, 2, 3, 4, 5, 5]

print(set(my_list))  # useful in duplicated values(email, username)

my_set = {1, 2, 3, 4, 5, 5}
new_set = my_set.copy()
my_set.clear()

print(new_set)  # to access the set, we have to grab by item in it
print(my_set)
