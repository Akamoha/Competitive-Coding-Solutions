import sys
sys.setrecursionlimit(2147000000)

def read_input():
    return list(map(int, input().split()))

def solve(a, b, i):
    global DP, H, K, N
    if (a,b,i) in DP:
        return DP[(a,b,i)]
    if a >= K and b >= K:
        return 0
    if i >= len(H):
        return N+1
    if a >= K:
        DP[(a,b,i)] = 1+solve(a, b+H[i], i+1)
    elif b >= K:
        DP[(a,b,i)] = 1+solve(a+H[i], b, i+1)
    else:
        DP[(a,b,i)] = 1+min(solve(a+H[i], b, i+1), solve(a, b+H[i], i+1))
    return DP[(a,b,i)]

for _ in range(int(input())):
    N, K = read_input()
    H = read_input()
    H.sort(reverse=True)
    DP = {}
    ans = solve(0, 0, 0)
    print(-1 if ans >= N+1 else ans)