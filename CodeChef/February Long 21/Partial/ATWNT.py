import sys
sys.setrecursionlimit(2147000000)
def get_ints():
    return list(map(int, sys.stdin.readline().strip().split()))

N = int(input())
t = [[] for _ in range(N+1)]
P = [0]+get_ints()
for i in range(1, N):
    t[P[i]].append(i+1)
    
def solve(V, W):
    K = len(t[V])
    if K == 0:
        return W
    elif W % K == 0:
        return sum([solve(child, W//K) for child in t[V]])
    return 0
        
Q = int(input())
for _ in range(Q):
    V, W = get_ints()
    print(W-solve(V, W))