class PlayerCharacter:
    def __init__(self, name='Anonymous', age=0, money=0):  # constructor function
        self.name = name  # attributes
        self.age = age
        self.money = money

    def shout(self):
        print(
            f'Hi! my name is {self.name} and I\'m currently {self.age} years old! I have {self.money} money left.')

    def run(self):
        print(f'{self.name} has fled the area.')

    def buyweapon(self):
        weapondict = {'Sword': 40, 'Bow': 25, 'Hammer': 50}
        if self.money == 0:
            print('Get out of my shop!')
        elif self.money < 15:
            print(
                f'Your character {self.name} does not have enough money to buy this weapon. Try again another time.')
        elif self.money > 50:
            print(
                f'You character {self.name} has an astounding sum of cash! Which weapons would you like to buy?')
            for k, v in weapondict.items():
                print(k, ':', v)
            Cost = input('Which would would you like to select?: ')
            self.money -= weapondict.get(Cost)
            print(
                f'You have just bought a {Cost} and now have {self.money} money left. Have a nice day!')


player1 = PlayerCharacter('George', 90, 99)
player1.shout()
# player1.run()
player1.buyweapon()
