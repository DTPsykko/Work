class User(object):
    def sign_in(self):
        print('logged in')

    def attack(self):
        print('do nothing')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left {self.num_arrows - 1}')


wizard1 = Wizard('Merlin', 60)
archer1 = Archer('Robin', 60)


def player_attack(char):  # same function gives
    # different output because of the different object
    # being passed through
    char.attack()


player_attack(wizard1)
player_attack(archer1)

for char in [wizard1, archer1]:
    char.attack()
wizard1.attack()
archer1.attack()
