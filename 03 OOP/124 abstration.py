# Abstraction, hiding the information or abstracting info and giving access to only what is necessary


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
player1.name = '1111'
player1.speak = 'BOOOOOO'

print(player1.speak)
