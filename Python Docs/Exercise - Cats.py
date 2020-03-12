class Cat:
    species = 'mammal'

    def __init__(self, name='null', age=0):
        self.name = name
        self.age = age


Cat1 = Cat('Eric', 9)
Cat2 = Cat('Bobby', 6)
Cat3 = Cat('Billy', 4)


def oldest(*args):  # *args takes in as many arguments
    return(max(args))  # returns highest


print(f'The oldest cat is {oldest(Cat1.age,Cat2.age,Cat3.age)} years old.')
