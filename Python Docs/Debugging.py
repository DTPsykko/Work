# Debugging

# linting

# try:
#     print(4 + 'brewda')
# except TypeError:
#     print('hi')

# pdb - Python Debugger

import pdb


def add(num1, num2):
    # pdb.set_trace()
    return num1 + num2


print(add(4, 5))
