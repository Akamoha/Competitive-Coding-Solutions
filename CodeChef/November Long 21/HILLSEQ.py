for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    ht = {}
    for a in A:
        if a not in ht:
            ht[a] = 0
        ht[a] += 1
    for a in ht:
        if ht[a] > 2:
            print(-1)
            break
    else:
        ek = [a for a in ht if ht[a] == 1]
        do = [a for a in ht if ht[a] == 2]
        if len(do) == 0:
            ek.sort(reverse=True)
            for a in ek:
                print(a, end=" ")
            print()
        elif len(ek) == 0:
            print(-1)
        elif max(ek) < max(do):
            print(-1)
        else:
            left = do.copy()
            right = ek + do
            left.sort()
            right.sort(reverse=True)
            for a in left+right:
                print(a, end=" ")
            print()