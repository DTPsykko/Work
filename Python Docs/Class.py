# OOP - Object Oriented Programming
# CLASS -> Instantiate -> Instances
# Allows to write code that is efficient and repeatable


class PlayerCharacter:
    #Membership is static
    membership = True  # Class Object Attribute

    def __init__(self, name='Anonymous', age=0):  # constructor function
        if (age > 18):
            self.name = name  # attributes
            self.age = age

    def shout(self):
        print(f'my name is {self.name}')

    @classmethod  # method on the actual class
    def adding_things(cls, num1, num2):  # cls refers to PlayerCharacter
        return num1+num2
    # cares about attributes

    # @staticmethod  # static doesn't have access to cls
    # def adding_things(num1, num2):
    #     return num1+num2
    # does not care about attributes
player1 = PlayerCharacter('George', 10)
# player2 = PlayerCharacter('Obama', 21)
# player2.attack = 50
# print(player2.name)
print(player1.adding_things(4, 5))
