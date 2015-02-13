N = input()
a = 0
b = 1
L = [0, 1]
for i in range(N - 2):
    c = a + b
    L.append(c)
    a, b = b, c

cube = lambda a: a**3

if N == 0:
    print []
elif N == 1:
    print [0]
elif N == 2:
    print [0, 1]
else:
    print list(map(cube, L))