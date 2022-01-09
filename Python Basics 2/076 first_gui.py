# First GUI

# clean good code
# readability
# predictability
# DRY (do not repeat yourself), make it reusable

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]


# iterate over picture
# if 0 -> print ""
# if 1 -> print *

def show_tree():
    for row in picture:
        for pixel in row:
            if (pixel):
                print("*", end="")
            else:
                print("", end="")
        print("")  # need a new line after a row


show_tree()
show_tree()
show_tree()
