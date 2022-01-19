# Exercise: Check for duplicates in list:

some_list = ['a', 'b', 'c', "b", 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)

# def checkifDuplicates_1(some_list):
#     '''Check if given list contains any duplicates'''
#     if len(some_list) == len(set(some_list)):
#         return False
#     else:
#         return True
#
#
# result = checkifDuplicates_1(some_list)
#
# if result:
#     print("Yes, list is duplicated")
# else:
#     print("No list is not duplicated")
