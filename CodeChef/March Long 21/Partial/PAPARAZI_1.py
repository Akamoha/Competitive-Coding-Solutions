import sys
def get_ints():
    return list(map(int, sys.stdin.readline().strip().split()))

def cansee(i, j):
    global A
    for k in range(i+1, j):
        h = A[i] + (A[j]-A[i])*(k-i)/(j-i)
        if A[k] > h:
            return False
    return True
    
for _ in range(int(input())):
    N = int(input())
    A = get_ints()
    ans = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if cansee(i, j):
                ans = max(ans, abs(j-i))
    print(ans)