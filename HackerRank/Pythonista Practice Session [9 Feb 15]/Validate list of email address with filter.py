import re
A = []
for _ in range(input()):
    A.append(raw_input())
B = list(filter(lambda x: re.match('^[a-zA-Z0-9-_]{1,}[@]{1}[a-zA-Z0-9]{1,}[.]{1}[a-zA-Z0-9]{1,3}$', x) != None, A))
B.sort()
print B