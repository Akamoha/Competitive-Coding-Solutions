N = int(raw_input())
dictionary = {}
for _ in range(N):
    A = raw_input().split()
    name = A.pop(0)
    dictionary[name] = map(float, A)
name = raw_input()
print "{0:.2f}".format(1.00*sum(dictionary[name])/len(dictionary[name]))
