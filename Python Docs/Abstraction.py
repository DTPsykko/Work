# Theres no true private variables
# If theres an _before it then it indicates to not touch


class PlayerChracter:
    def __init__(self, name, age):  # __init__ is a dunder method
        self._name = name
        self._age = age

    def shout(self):
        print(
            f'Hi! my name is {self._name} and I\'m {self._age} years old!')

    def run(self):
        print(f'{self._name} has fled the area.')


player1 = PlayerChracter('Danny', 100)
player1.shout()
# print((1,2,3,1).count(1))
# print(len((1,2,3,1,)))
