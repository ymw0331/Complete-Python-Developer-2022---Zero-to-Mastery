# Error Handling

while True:
    try:
        age = int(input('what is you age?'))
        10 / age
        print(age)
    except ValueError:
        print("!!!!")
    except ValueError:
        print("please enter an number")
    except ZeroDivisionError:
        print("please enter age higher than 0")
    else:
        print("thank you")
        break
