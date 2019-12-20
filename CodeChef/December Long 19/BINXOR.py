M = 10**9+7

def C(n, r, p=M): 
    num = den = 1 
    for i in range(r): 
        num = (num * (n - i)) % p 
        den = (den * (i + 1)) % p 
    return (num * pow(den,  p - 2, p)) % p 
    
for _ in range(int(input())):
    N = int(input())
    A = input()
    B = input()
    
    a1 = A.count('1')
    a0 = N-a1
    
    b1 = B.count('1')
    b0 = N-b1
    
    min1s = max(a1, b1)-min(a1, b1)
    max1s = a1+b1-max(0, 2*(a1+b1-N))
        
    ans = combo = C(N, min1s)
    
    for n in range(min1s+2, max1s+1, 2):
        num = (combo*(N-n+1)*(N-n+2)) % M
        den = (n*(n-1)) % M
        combo = (num * pow(den,  M - 2, M)) % M
        ans += combo
    
    print(ans%M)