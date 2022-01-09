# index counter use enumerate

for i, char in enumerate('Helloooooo'):
    print(i, char)

for i, char in enumerate(list(range(100))):
    if char == 50:
        print(f'index of 50 is: {i}')
