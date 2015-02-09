K = 0
MOD = 10**9

def mul(A, B):
    rows_A = K
    cols_A = K
    rows_B = K
    cols_B = K

    C = [[0 for row in range(cols_B)] for col in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] = (C[i][j] + (A[i][k] * B[k][j])) % MOD
    return C

def pow(A, p):
    if p == 1:
        return A
    if (p % 2):
        return mul(A, pow(A, p-1))
    X = pow(A, p/2)
    return mul(X,X)

T = int(raw_input())
for _ in range(T):
    k = int(raw_input())
    B = map(int, raw_input().split())
    C = map(int, raw_input().split())
    n = int(raw_input())
    K = k
    if n <= k:
        print B[n-1]
        continue
    F1 = B[:k]
    T = []
    for i in range(k-1):
        T.append([0]*k)
        T[-1][i+1] = 1
    T.append(C[::-1])
    T = pow(T, n-1)
    res = 0
    for i in range(K):
        res = (res + (T[0][i] * F1[i])) % MOD
    print res
