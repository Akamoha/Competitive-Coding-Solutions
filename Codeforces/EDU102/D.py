import sys
def get_ints():
    return list(map(int, sys.stdin.readline().strip().split()))

def get_string():
    return sys.stdin.readline().strip()
    
def solve(l, r):
    asmn, asmx = MNMX_right[r+1]
    if l == 0:
        bsmn, bsmx = 0, 0
        cur = 0
    else:
        bsmn, bsmx = MNMX_left[l-1]
        cur = CSA[l-1]
    mx = max(bsmx, asmx+cur)
    mn = min(bsmn, asmn+cur)
    return mx-mn+1

for _ in range(int(input())):
    n, m = get_ints()
    A = get_string()
    MNMX_right = [[0, 0] for __ in range(n+1)]
    mn, mx = 0, 0
    for i in range(n-1, -1, -1):
        if A[i] == '-':
            mn -= 1
            mx -= 1
        else:
            mn += 1
            mx += 1
        mn = min(mn, 0)
        mx = max(mx, 0)
        MNMX_right[i] = [mn, mx]
    
    MNMX_left = [[0, 0] for __ in range(n+1)]
    CSA = [0 for __ in range(n+1)]
    mn, mx, cur = 0, 0, 0
    for i in range(n):
        if A[i] == '-':
            cur -= 1
        else:
            cur += 1
        mn = min(mn, cur)
        mx = max(mx, cur)
        MNMX_left[i] = [mn, mx]
        CSA[i] = cur
    
    for __ in range(m):
        l, r = get_ints()
        sys.stdout.write(str(solve(l-1, r-1))+'\n')