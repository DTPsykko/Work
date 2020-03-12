# @decorator
def hello(func):
    func()
    return


def greet():
    print('still here!')


# a = hello(greet)
# print(a)
