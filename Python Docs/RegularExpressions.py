import re
# string = 'search inside of this text please'

# a = re.search('this', string)
# # print(a.group())
# print(a.group())

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
string = 'hello@hello.com'

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)
# print(a.group())
# print(b)
print(a)
