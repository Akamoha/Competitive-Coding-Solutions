import bisect as bi
for _ in range(int(input())):
    X = [list(map(int, input().split()))[1:] for _ in range(int(input()))]
    ht = {}
    for x in X:
        for pos in x:
            k = abs(pos)
            if k not in ht:
                ht[k] = 0
            ht[k] += 1   
    c = len([1 for k in ht if ht[k] > 1])
    for x in X:
        for i in range(len(x)):
            pos = x[i]
            if ht[abs(pos)] > 1:
                c += i if pos < 0 else len(x)-i-1
            else:
                c += len(x) - bi.bisect_right(x, -pos) if pos < 0 else bi.bisect_left(x, -pos)
    print(c)