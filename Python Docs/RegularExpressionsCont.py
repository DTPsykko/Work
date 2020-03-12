
import re
pattern = re.compile(r"[A-Za-z0-9%$@#]{8,}\d")
string = 'scuffedpassword123'

a = pattern.fullmatch(string)
print(a)
