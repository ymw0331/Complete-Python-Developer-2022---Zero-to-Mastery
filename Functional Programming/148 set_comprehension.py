# Set Comprehension, no duplicated item but only unique item

my_list = {char for char in 'hello'}
my_list2 = {num for num in range(0, 100)}
my_list3 = {num * 2 for num in range(0, 100)}
my_list4 = {num ** 2 for num in range(0, 100) if num % 2 == 0}

simple_dict = {
    'a': 1,
    'b': 2
}
my_dict = {k: v ** 2 for k, v in simple_dict.items()}

my_dict2 = {num: num*2 for num in [1, 2, 3]}

print(my_dict)
print(my_dict2)
