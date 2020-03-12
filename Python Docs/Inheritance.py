# users
# Mage
# Archers
# Assassin
# Warriors


class User:
    name = 'null'

    def sign_in(self):
        print(f'{self.name} has logged in')


class Mage(User):
    def __init__(self, name, mana=20, health=100):
        self.name = name
        self.mana = mana
        self.health = health

    def heal(self):
        self.mana -= 6
        print(f'{self.name} casts heal. {self.mana} mana left')

    def teleport(self):
        self.mana -= 4
        print(f'{self.name} casts teleport. {self.mana} mana left')

    def meteor(self):
        self.mana -= 8
        print(f'{self.name} casts meteor. {self.mana} mana left')

    def ice_snake(self):
        self.mana -= 4
        print(f'{self.name} casts ice snake.{self.mana} mana left')


class Archer(User):
    def __init__(self, name, mana=20, health=100):
        self.name = name
        self.mana = mana
        self.health = health

    def arrow_bomb(self):
        self.mana -= 8
        print(f'{self.name} casts arrow bomb. {self.mana} mana left')

    def escape(self):
        self.mana -= 3
        print(f'{self.name} casts escape. {self.mana} mana left')

    def arrow_storm(self):
        self.mana -= 6
        print(f'{self.name} casts arrow storm. {self.mana} mana left')

    def arrow_shield(self):
        self.mana -= 10
        print(f'{self.name} casts arrow shield. {self.mana} mana left')


class Warrior(User):
    def __init__(self, name, mana=20, health=100):
        self.name = name
        self.mana = mana
        self.health = health

    def bash(self):
        self.mana -= 6
        print(f'{self.name} casts bash. {self.mana} mana left')

    def charge(self):
        self.mana -= 4
        print(f'{self.name} casts charge. {self.mana} mana left')

    def uppercut(self):
        self.mana -= 10
        print(f'{self.name} casts uppercut. {self.mana} mana left')

    def war_screan(self):
        self.mana -= 6
        print(f'{self.name} casts war scream. {self.mana} mana left')


class Assassin(User):
    def __init__(self, name, mana=20, health=100):
        self.name = name
        self.mana = mana
        self.health = 100

    def spin_attack(self):
        self.mana -= 6
        print(f'{self.name} casts spin attack. {self.mana} mana left')

    def vanish(self):
        self.mana -= 1
        print(f'{self.name} casts vanish. {self.mana} mana left')

    def multi_hit(self):
        self.mana -= 8
        print(f'{self.name} casts multi hit. {self.mana} mana left')

    def smoke_bomb(self):
        self.mana -= 8
        print(f'{self.name} casts smoke bomb. {self.mana} mana left')


mage1 = Mage('Bob')
archer1 = Archer('Billy')
mage1.sign_in()
mage1.meteor()
archer1.arrow_storm()
# print(isinstance(mage1, object))
