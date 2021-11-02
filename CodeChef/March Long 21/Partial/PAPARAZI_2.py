import sys
def get_ints():
    return list(map(int, sys.stdin.readline().strip().split()))

for t in range(int(input())):
    N = int(input())
    A = get_ints()
    ans = 1
    for i in range(N-1):
        ph, pi = A[i+1], i+1
        for j in range(i+2, N):
            if (A[j]-A[i])*(pi-i) >= (j-i)*(ph-A[i]):
                ans = max(ans, j-i)
                ph, pi = A[j], j
    sys.stdout.write(str(ans)+'\n')