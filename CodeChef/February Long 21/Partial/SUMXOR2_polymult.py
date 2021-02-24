# First subtask passed using naive polynomial multiplication
# Now using Fast Fourier Transform for polynomial multiplication
# but still TLE

MOD = 998244353
MX = 1001

import sys
def get_ints():
    return list(map("{:031b}".format, map(int, sys.stdin.readline().strip().split())))

def modInverse(a):
    return pow(a, MOD-2, MOD)
        
def nCr(n, r):
    if n < r:
        return 0
    return (((fact[n]*invfact[r])%MOD)*invfact[n-r])%MOD
    
def mul(C_array, B_array):
    ret = [0 for _ in range(len(C_array)+len(B_array)+1)]
    for i in range(len(C_array)):
        for j in range(len(B_array)):
            ret[i+j] = (ret[i+j] + C_array[i]*B_array[j])%MOD
    return ret

def compute_ans(n0s):
    C_array = [nCr(N-n0s, i) for i in range(1, MX+1, 2)]
    B_array = [nCr(n0s, 0)]
    for i in range(1, MX, 2):
        B_array.append((nCr(n0s, i)+nCr(n0s, i+1))%MOD)

    odd_array = [0]
    multed = mul(C_array, B_array)
    for elem in multed:
        odd_array.append((odd_array[-1]+elem)%MOD)
    odd_array = odd_array[1:]

    C_array = [nCr(N-n0s, i) for i in range(1, MX, 2)]
    B_array = []
    for i in range(0, MX-1, 2):
        B_array.append((nCr(n0s, i)+nCr(n0s, i+1))%MOD)

    even_array = [0]
    multed = mul(C_array, B_array)
    for elem in multed:
        even_array.append((even_array[-1]+elem)%MOD)
    even_array = even_array[1:]

    ans_array = []
    for i in range(MX//2):
        ans_array.append(odd_array[i])
        ans_array.append(even_array[i])
    
    return ans_array

fact = [1]
for i in range(1, MX):
    f = (fact[-1]*i)%MOD
    fact.append(f)
    
invfact = [modInverse(fact[-1])]
for i in range(MX-1, 0, -1):
    invfact.append((invfact[-1]*i)%MOD)
invfact = invfact[::-1]

####################################################

N = int(input())
A = get_ints()

C = [0 for _ in range(31)]
for a in A:
    for i in range(31):
        C[i] += int(a[i])

ht = []
for i in range(31):
    ht.append(compute_ans(N-C[i]))

Q = int(input())
for _ in range(Q):
    M = int(input())
    ans = 0
    for i in range(31):
        ans = (ans + ht[i][M-1]*pow(2, 30-i, MOD))%MOD
    print(ans)