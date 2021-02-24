MOD = 998244353

import sys
def get_ints():
    return list(map("{:031b}".format, map(int, sys.stdin.readline().strip().split())))

N = int(input())
A = get_ints()

C = [0 for _ in range(31)]
for a in A:
    for i in range(31):
        C[i] += int(a[i])

triangle = []
def makeTriangle():
    global triangle
    triangle = [[0 for _ in range(1001)] for __ in range(1001)]
    triangle[0][0] = 1
    for i in range(1, 1001):
        triangle[i][0] = 1
        for j in range(1, i+1):
            triangle[i][j] = (triangle[i-1][j-1] + triangle[i-1][j])%MOD
makeTriangle()

def nCr(n, r):
    if n < r:
        return 0
    return triangle[n][r]
            
def count(i, m):
    # count m-length subsequences with odd number of 1s
    ret = 0
    c, e = C[i], N-C[i]
    for k in range(1, m+1, 2):
        ret = (ret + nCr(c, k)*nCr(e, m-k))%MOD
    return ret

def countk(i, m, k):
    # count m-length subsequences with k number of 1s
    c, e = C[i], N-C[i]
    return (nCr(c, k)*nCr(e, m-k))%MOD
    
ht = [[0 for _ in range(31)] for __ in range(1001)]
for i in range(31):
    ansfori = count(i, 1)
    ht[1][i] = ansfori
    for m in range(2, 1001):
        ansfori = (ansfori + count(i, m))%MOD
        ht[m][i] = ansfori

Q = int(input())
for _ in range(Q):
    M = int(input())
    ans = 0
    for i in range(31):
        ans = (ans + ht[M][i]*pow(2, 30-i, MOD))%MOD
    print(ans)