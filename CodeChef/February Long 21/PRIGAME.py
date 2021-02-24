import sys
def get_ints():
    return map(int, sys.stdin.readline().strip().split())

def sieve(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    ret = []
    for p in range(2, n+1):
        if prime[p]:
            ret.append(p)
    return ret
    
P = sieve(10**6+100)
    
for _ in range(int(input())):
    X, Y = get_ints()
    chef, divyam = "Chef\n", "Divyam\n"
    ans = chef if X < P[min(Y, len(P)-1)] else divyam
    sys.stdout.write(ans)