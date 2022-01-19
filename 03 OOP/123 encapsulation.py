# Encapsulation (binding of data and function)

class PlayerCharacter:
    # Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Methods
    def run(self):
        print('run')

    def speak(self):
        print(f'my name is {self.name}, and I am {self.age} years old')


player1 = PlayerCharacter('wayne', 22)
player1.speak()
