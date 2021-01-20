for _ in range(int(input())):
    n = int(input())
    p = [i for i in range(n+1)]
    ops = []
    for i in range(1, n//2+1):
        ops.append((i, n))
    for i in range(n-1, n//2, -1):
        ops.append((i, 1))
    print(sum([(j-i)**2 for i, j in ops]))
    for i, j in ops:
        p[i], p[j] = p[j], p[i]
    p = p[1:]
    print(' '.join(map(str, p)))
    print(len(ops))
    for i, j in ops[::-1]:
        print(i, j)