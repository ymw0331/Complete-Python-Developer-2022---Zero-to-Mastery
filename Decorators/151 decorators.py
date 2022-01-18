# Decorators, function that wrap another function to enhance it


def my_decorator(func):
    def wrap_func():
        print("******************")
        func()
        print("******************")

    return wrap_func()


@my_decorator
def hello():
    print('helloooo')


@my_decorator
def bye():
    print("see you later")


