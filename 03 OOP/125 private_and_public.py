# Private and Public
# Python has no true private variable

class PlayerCharacter:
    # Attributes
    '''
    __init__ is a dunder method, built into python,
    double underscore has special meaning to python
    '''

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # Methods
    def run(self):
        print('run')

    def speak(self):
        print(f'my name is {self.name}, and I am {self.age} years old')


player1 = PlayerCharacter('wayne', 22)
# player1.name = '1111'
# player1.speak = 'BOOOOOO'

print(player1.speak)
