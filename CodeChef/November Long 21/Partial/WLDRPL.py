import sys, io, os
def get_ints(): return map(int, sys.stdin.readline().strip().split())

for _ in range(int(input())):
    S = input()
    res = ''
    for _ in range(int(input())):
        L, R = get_ints()
        L -= 1
        X = []
        for i in range(L, R):
            if S[i] in '(+-':
                X.append(S[i])
            elif S[i] == '?':
                X.append([1, 0])
            else:
                bmax, bmin = X.pop()
                op = X.pop()
                amax, amin = X.pop()
                X.pop()
                if op == '+':
                    cmax = amax + bmax
                    cmin = amin + bmin
                else:
                    cmax = amax - bmin
                    cmin = amin - bmax
                X.append([cmax, cmin])
        ans, _resmin = X.pop()
        res += str(ans)+' '
    sys.stdout.write(res+"\n")