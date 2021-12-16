for _ in range(int(input())):
    input()
    A = list(map(int, input().split()))
    ht = {}
    for a in A:
        if a not in ht:
            ht[a] = 0
        ht[a] += 1
    N, elem = max([(ht[k], k) for k in ht])
    rem = sum(ht.values())-N
    if rem == 0:
        print(0)
    elif N < 2:
        print(-1)
    else:
        print(rem+1)