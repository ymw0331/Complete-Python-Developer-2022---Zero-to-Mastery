# Scope - what variable do iIhave access to?

if True:
    x = 10


def some_func():
    total = 100
    print(x)


print(x)
