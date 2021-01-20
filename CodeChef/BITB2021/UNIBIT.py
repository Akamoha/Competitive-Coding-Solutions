for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    ht = {}
    for a in A:
        if a not in ht:
            ht[a] = 0
        ht[a] += 1
    for a in ht:
        if ht[a] == 3:
            print(a)
            break