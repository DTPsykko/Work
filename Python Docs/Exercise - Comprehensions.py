some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = list(set(num for num in some_list if some_list.count(
    num) > 1))

print(duplicates)
