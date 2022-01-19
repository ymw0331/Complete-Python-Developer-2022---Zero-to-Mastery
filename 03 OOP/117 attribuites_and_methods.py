# Attributes and Methods


class PlayerCharacter:
    # Class Object Attribute(static)
    membership = True

    def __init__(self, name, age):  # constructor method, self refer to player character, equivalent to this() in java
        if (self.membership):
            self.name = name
            self.age = age

    def shout(self):
        print(f'my name is {self.name}')
        return 'done'


player1 = PlayerCharacter('Wayne', 24)
player2 = PlayerCharacter('Tom', 21)
player2.attack = 50

print(player1.shout())
print(player2.shout())
