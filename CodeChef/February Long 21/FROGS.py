def read():
    return list(map(int, input().split()))

def done(pwl):
    pwl.sort()
    wts = [w for p,w,l in pwl]
    ps  = [p for p,w,l in pwl]
    swts = wts.copy()
    swts.sort()
    return len(set(ps)) == len(ps) and swts == wts

for _ in range(int(input())):
    N = int(input())
    W, L = read(), read()
    pwl = [[i+1, W[i], L[i]] for i in range(N)]
    ans = 0
    while len(pwl) > 1 and not done(pwl):
        pwl.sort()
        minwt = min([w for p,w,l in pwl])
        if minwt == pwl[0][1]:
            for i in range(1, len(pwl)):
                if pwl[0][0] == pwl[i][0]:
                    pwl[i][0] += pwl[i][2]
                    ans += 1
            pwl = pwl[1:]
        else:
            pwl[0][0] += pwl[0][2]
            ans += 1
    print(ans)