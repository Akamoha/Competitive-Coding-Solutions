import sys
sys.setrecursionlimit(2147000000)
def get_ints():
    return map(int, sys.stdin.readline().strip().split())

X = 10**15
def solve(N,E,H):
    global A,B,C,DP
    if (N,E,H) in DP:
        return DP[(N,E,H)]
    ret = X
    if N <= 0:
        return 0
    if 2*N <= E:
        ret = min(ret, N*A)
    if 3*N <= H:
        ret = min(ret, N*B)
    if N <= E and N <= H:
        ret = min(ret, N*C)
    if (H-N)//2 >= max(N-E, 1):
        x = min(N-1, (H-N)//2) if B < C else max(1, N-E)
        ret = min(ret, x*(B-C)+N*C)
    if E//2 >= max(1, (3*N-H+2)//3):
        x = min(N-1, E//2) if A < B else max(1, (3*N-H+2)//3)
        ret = min(ret, x*(A-B)+N*B)
    if E-N >= 1 and E+H >= 2*N:
        x = min(N-1, E-N) if A < C else max(1, N-H)
        ret = min(ret, x*(A-C)+N*C)
    if N >= 3 and E >= 3 and H >= 4:
        ret = min(ret, A+B+C+solve(N-3, E-3, H-4))
    DP[(N,E,H)] = ret
    return DP[(N,E,H)]
    
for _ in range(int(input())):
    n,e,h,A,B,C = get_ints()
    DP = {}
    ans = solve(n,e,h)
    ans = -1 if ans == X else ans
    sys.stdout.write(str(ans)+'\n')