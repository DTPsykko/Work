

from functools import reduce
my_list = [1, 2, 3]


def multi2(item):
    return item*2


def onlyodd(item):
    return item % 2 != 0


def accumulate(acc, item):
    return acc + item


print(reduce(accumulate, my_list, 0))
print(my_list)
