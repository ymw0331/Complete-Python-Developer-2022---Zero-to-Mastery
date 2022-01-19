# __init__


class PlayerCharacter:
    # Class Object Attribute(static)
    membership = True

    def __init__(self, name='anonymous', age=0):
        # constructor method, self refer to player character, equivalent to this() in java
        if (age > 18):
            self.name = name
            self.age = age

    def shout(self):
        print(f'my name is {self.name}')
        return 'done'


player1 = PlayerCharacter('Tom', 24)

print(player1.shout())
