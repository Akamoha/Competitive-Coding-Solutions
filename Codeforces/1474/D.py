def solve2(X):
    return X[0] == X[1]

def s3h(a, b, c):
    return solveN_nosuper([a,b,c])
    
def solve3(X):
    a, b, c = X
    return s3h(a,b,c) or s3h(b,a,c) or s3h(a,c,b)
        
def s4h(a, b, c, d):
    if min(a,b,c,d) < 0:
        return False
    return solveN_nosuper([a,b,c,d])
    
def solve4(X):
    a, b, c, d = X
    return s4h(a,b,c,d) or s4h(b,a,c,d) or s4h(a,c,b,d) or s4h(a,b,d,c)

def solveN_nosuper(X):
    X = X.copy()
    for i in range(len(X)-1):
        if X[i] > X[i+1]:
            return False
        X[i+1] -= X[i]
        X[i] = 0
    return X[-1] == 0
    
def fix(X):
    X = X.copy()
    ret = [X[0]]
    for i in range(1, len(X)):
        if ret[i-1] == -1 or X[i-1] > X[i]:
            ret.append(-1)
        else:
            X[i] -= X[i-1]
            X[i-1] = 0
            ret.append(X[i])
    return ret
    
def solveN(X):
    if solveN_nosuper(X):
        return True
    L = [0]+fix(X)+[0]
    R = [0]+fix(X[::-1])[::-1]+[0]
    X = [0]+X+[0]
    for i in range(1,len(X)-2):
        if s4h(L[i-1], X[i+1], X[i], R[i+2]):
            return True
    return False

for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    if N == 2:
        ans = solve2(A)
    elif N == 3:
        ans = solve3(A)
    elif N == 4:
        ans = solve4(A)
    else:
        ans = solveN(A)
    print("YES" if ans else "NO")