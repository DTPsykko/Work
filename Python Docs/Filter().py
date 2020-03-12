my_list = [1,2,3]
def multi2(item):
    return item*2

def onlyodd(item):
    return item % 2 != 0

print(list(filter(onlyodd, my_list)))
print(my_list)


