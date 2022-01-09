i = 0
while i < 50:
    print(i)
    i = i + 1  # keep increment by 1
else:
    print("done with all the work")

while True:
    response = input('say something:')
    if (response == "bye"):
        break
