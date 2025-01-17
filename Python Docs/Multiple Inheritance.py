class User():
    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power,):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        print(f'{self.arrows} remaining')

    def run(self):
        print('ran really fast')


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)


HB1 = HybridBorg('Joe', 50, 100)
HB1.run()
HB1.check_arrows()
HB1.attack()
HB1.sign_in()
