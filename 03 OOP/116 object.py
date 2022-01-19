# 03 OOP object
# DRY do not repeat yourself

class PlayerCharacter:
    def __init__(self, name, age):  # constructor method, self refer to player character, equivalent to this() in java
        self.name = name
        self.age = age

    def run(self):
        print('run')


player1 = PlayerCharacter('Wayne', 24)
player2 = PlayerCharacter('Tom', 21)
player2.attack = 50


print(player1)
print(player2.attack)
