import sys
sys.setrecursionlimit(2147000000)
 
def solve(N, C, U):
    if (N, C) in ht:
        return ht[(N, C)]
    if N == 1:
        if C <= U:
            D[N] = C
            ht[(N, C)] = 1
            return 1
        ht[(N, C)] = 0
        return 0
    for i in xrange(N, min(C+N-1, U)+1):
        if C % (i-(N-1)) == 0:
            r = solve(N-1, C/(i-(N-1)), i)
            if r == 1:
                break
    else:
        ht[(N, C)] = 0
        return 0
    D[N] = i
    ht[(N, C)] = 1
    return 1
 
for _ in xrange(input()):
    N, C = map(int, raw_input().split())
    D = [0 for __ in xrange(N+1)]
    ht = {}
    solve(N, C, C+N-1)
    for i in xrange(1, N+1):
        print D[i],
    print 