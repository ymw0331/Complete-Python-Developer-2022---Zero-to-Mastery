# Data Structure

li = [1, 2, 3, 4, 5]
li2 = ['a', 'b', 'c']
li3 = [1, 2.5, 'a', True]

# List Slicing
amazon_cart = ['notebooks',
               'sunglasses',
               'toys',
               'grapes'
               ]

amazon_cart[0] = 'laptop'
new_cart = amazon_cart[0:3]
new_cart[0] = 'gum'
# [start:stop:stepover]
print(new_cart)
print(amazon_cart)
