# Dictionary methods

user = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    'age': 20

}
user.clear()
print(user)

print(user.get('age', 55))  # assign default value when age does not exist

user2 = dict(name='JohnJohn')  # built in function for dictionary
print(user2)
