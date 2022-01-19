# Object introspection

class User(object):
    def __int__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
        # super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


# introspection
wizard1 = Wizard('Merlin', 50)
print(dir(wizard1))
