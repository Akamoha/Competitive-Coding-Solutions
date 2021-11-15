import sys, io, os
def get_ints(): return map(int, sys.stdin.readline().strip().split())

for _ in range(int(input())):
    S = input()
    res = ''
    ht = {}
    for _ in range(int(input())):
        L, R = get_ints()
        L -= 1
        X = []
        i = L
        while i < R:
            if S[i] == '(':
                if i in ht:
                    X.append(ht[i][0])
                    i = ht[i][1]
                else:
                    X.append(i)
            elif S[i] in '+-':
                X.append(S[i])
            elif S[i] == '?':
                X.append([1, 0])
                ht[i] = (X[-1], i)
            else:
                bmax, bmin = X.pop()
                op = X.pop()
                amax, amin = X.pop()
                startpos = X.pop()
                if op == '+':
                    cmax = amax + bmax
                    cmin = amin + bmin
                else:
                    cmax = amax - bmin
                    cmin = amin - bmax
                X.append([cmax, cmin])
                ht[startpos] = (X[-1], i)
            i += 1
        ans, _resmin = X.pop()
        res += str(ans)+' '
    sys.stdout.write(res+"\n")