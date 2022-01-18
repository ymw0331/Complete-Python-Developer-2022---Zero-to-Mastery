# Error Handling

def sum(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError):
        print('oppppsss')


print(sum('1', 0))
