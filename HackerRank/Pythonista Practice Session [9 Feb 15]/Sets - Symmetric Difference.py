M = int(raw_input())
Mints = set(map(int, raw_input().split()))
N = int(raw_input())
Nints = set(map(int, raw_input().split()))
u = Mints.union(Nints)
i = Mints.intersection(Nints)
d = list(u.difference(i))
d.sort()
for element in d:
    print element

