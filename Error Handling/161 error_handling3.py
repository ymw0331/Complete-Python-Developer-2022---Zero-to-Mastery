# Error Handling
while True:
    try:
        age = int(input('what is you age?'))
        10 / age
        raise ValueError('hey cut it out')
    except ValueError:
        print("please enter an number")
        continue
    except ZeroDivisionError:
        print("please enter age higher than 0")
        break
    else:
        print("thank you")
        break
    finally:
        print('ok, i am finally done')
    print('can you hear me?')
