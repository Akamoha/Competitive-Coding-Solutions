mod = 998244353

def calculate(p, q): 
    expo = 0
    expo = mod - 2
 
    while (expo): 
        if (expo & 1): 
            p = (p * q) % mod 
        q = (q * q) % mod 
 
        expo >>= 1
 
    return p

def M1(N, K):
    DP = [[0 for _ in range(N+1)] for __ in range(N+1)]

    for i in range(1, N+1):
        DP[i][1] = K

    for i in range(2, N+1):
        for j in range(1, N+1):
            DP[i][j] = (DP[i-1][j] + DP[i-1][j-1]*(K-1))%mod

    num = 0
    for j in range(1, N+1):
        num = (num + DP[N][j]*j)%mod
    denom = pow(K, N, mod)

    return calculate(num, denom)
    
def solve(M, N, K):
    DP = [[[0,0] for _ in range(M*N+1)] for __ in range(N+1)]

    for i in range(1, N+1):
        DP[i][1][0] = K
        DP[i][1][1] = 0
    
    DP[1][2][1] = K*(K-1)
        
    for i in range(2, N+1):
        j = 1
        DP[i][j][0] = (DP[i-1][j][0] + 2*DP[i-1][j][1] + (K-1)*DP[i-1][j-1][0] + (K-2)*DP[i-1][j-1][1])
        DP[i][j][1] = (2*(K-1)*DP[i-1][j-1][0] + DP[i-1][j][1] + 2*(K-2)*DP[i-1][j-1][1])
        for j in range(2, M*N+1):
            DP[i][j][0] = (DP[i-1][j][0] + 2*DP[i-1][j][1] + (K-1)*DP[i-1][j-1][0] + (K-2)*DP[i-1][j-1][1])
            DP[i][j][1] = (2*(K-1)*DP[i-1][j-1][0] + (K-1)*(K-2)*DP[i-1][j-2][0] + DP[i-1][j][1] + 2*(K-2)*DP[i-1][j-1][1] + ((K-2)*(K-3) + 1 + 2*(K-2))*DP[i-1][j-2][1])
    
    return DP
    
M, N, K = list(map(int, input().split()))

if M == 1:
    smallans = M1(2, K)
    print((smallans*(N-1)-(N-2))%mod)
else:
    DP = solve(2, 3, K)
    num1, num2, num3 = 0, 0, 0
    for j in range(1, 7):
        num1 = (num1 + sum(DP[1][j])*j)
        num2 = (num2 + sum(DP[2][j])*j)
        num3 = (num3 + sum(DP[3][j])*j)
    denom1 = pow(K, M*1)
    denom2 = pow(K, M*2)
    denom3 = pow(K, M*3)

    if N == 1:
        print(calculate(num1, denom1))
    else:
        ans = calculate(num2, denom2)
        diff = calculate(num3, denom3) - calculate(num2, denom2)
        for i in range(2, N):
            ans = (ans + diff)%mod
        print(ans)