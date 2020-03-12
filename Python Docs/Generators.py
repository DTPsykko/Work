# iterable
# iterate
# generator are iterable


# def make_list(num):
#     result = []
#     for i in range(num):
#         result.append(i*2)
#     return result


# my_list = make_list(100)
# print(my_list)

# print(list(range(10)))


def generator_func(num):
    for i in range(num):
        yield i


g = generator_func(100)
print(next(g))
print(next(g))
print(next(g))


# for item in generator_func(1000):
# print(item)
