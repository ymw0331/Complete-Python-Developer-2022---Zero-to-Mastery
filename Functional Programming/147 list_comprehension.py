# List comprehension

# my_list = [param for param in iterable]
my_list = [char for char in 'hello']
my_list2 = [num for num in range(0, 100)]
my_list3 = [num * 2 for num in range(0, 100)]
my_list4 = [num ** 2 for num in range(0, 100) if num % 2 == 0]

# Descriptive function
# for char in 'hello':
#     my_list.append(char)

print(my_list)
print(my_list2)
print(my_list3)
print(my_list4)
