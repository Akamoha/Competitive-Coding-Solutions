import bisect as bi
M = 10**9+7
N = 10**5

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m=M):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
        
fact = [1, 1]
for i in range(2, N+1):
    fact.append((fact[-1]*i)%M)
    
numsPerRow = [i*(i+1)//2+1 for i in range(N)]
def findpos(x):
    i = bi.bisect_right(numsPerRow, x)
    return (i, x-numsPerRow[i-1])
    
for _ in range(int(input())):
    s, e = list(map(int, input().split()))
    srow, sidx = findpos(s)
    erow, eidx = findpos(e)
    if erow <= srow or eidx<sidx or eidx-sidx > erow-srow:
        print(0)
    else:
        R = eidx-sidx
        L = erow-srow-R
        print((fact[L+R]*modinv(fact[L]*fact[R]))%M)