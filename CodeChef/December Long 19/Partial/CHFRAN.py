MAXR = 2*(10**6)

for _ in range(int(input())):
    N = int(input())
    A = [0]*(MAXR+2)
    mnr = MAXR
    mxl = 1
    for __ in range(N):
        l, r = list(map(int, input().split()))
        l *= 2
        r *= 2
        mnr = min(mnr, r)
        mxl = max(mxl, l)
        A[l] += 1
        A[r+1] -= 1
    CSA = [0]
    for i in range(MAXR):
        CSA.append(CSA[-1]+A[i])
    try:
        print(min(CSA[mnr+2:mxl+1]))
    except:
        print(-1)