# Higher order function HOC

def greet(func):
    func()


def greet2():
    def func():
        return 5

    return func()
