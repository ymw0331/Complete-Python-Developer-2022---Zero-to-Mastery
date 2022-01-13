# Class and static methods

# class PlayerCharacter:
#     membership = True
#
#     def __int__(self, name, age):
#         self.name = name  # attributes
#         self.age = age

class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def shout(self):
        print(f'my name is {self.name}')

    @classmethod  # decorator, without instantiate it
    def adding_things(cls, num1, num2):  # cls refer to class, self refer to instance
        return cls('Teddy', num1 + num2)

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2


player1 = PlayerCharacter('Tom', 23)
print(player1.adding_things(2, 3))
