def solve():
    N = int(input())
    S = input()
    L = 'abcdefghijklmnopqrstuvwxyz'
    ht = {}
    for l in L:
        ht[l] = -1
    ht[S[0]] = 0
    A = [ht]
    mn = N+1
    for i in range(1, N):
        ht = A[-1].copy()
        if A[-1][S[i]] != -1:
            mn = min(mn, i-A[-1][S[i]])
        if mn == 1:
            break
        ht[S[i]] = i
        A.append(ht)
    if mn == N+1:
        return 0
    return N-mn
    
for _ in range(int(input())):
    print(solve())