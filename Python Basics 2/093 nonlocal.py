# Nonlocal (new keyword in python3)

def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()

# 1 - start with local
# 2 - parent local?
# 3 - global
# 4 - built-in python functions
