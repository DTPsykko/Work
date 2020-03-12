# map, filter, zip, and reduce
my_list = [1, 2, 3]


def multi2(item):
    # new_list = []
    # for item in li:
    #     new_list.append(item*2)
    # return print(new_list)
    return item*2


# map is useful because of how clean it is
print(list(map(multi2, my_list)))
# multi2([1, 2, 3])
print(my_list)
