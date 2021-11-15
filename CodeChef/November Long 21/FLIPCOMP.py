def solve(X):
    X.append(-1337)
    S = [-1337, X[0]]
    ret = 0
    i = 1
    while i < len(X)-1:
        if X[i] == 1 and S[-1] > 1:
            if X[i+1] != -1337:
                S[-1] = 9
                ret += 1
                i += 2
            else:
                S.append(1)
                i += 1
        elif X[i] == 1 and S[-1] == 1:
            S.append(1)
            i += 1
        elif X[i] > 1 and S[-1] == 1:
            while S[-1] == 1 and S[-2] != -1337:
                S.pop()
                S.pop()
                ret += 1
            S.append(9)
            i += 1
        elif X[i] > 1 and S[-1] > 1:
            S.append(X[i])
            i += 1
    
    S.pop(0)
    if len(S)%2 == 0 and S[0] == 1:
        S.pop(0)
        S[0] += 1
        ret += 1
    elif len(S)%2 == 0 and S[-1] == 1:
        S.pop()
        S[-1] += 1
        ret += 1
    
    if len(S) == 3:
        return ret+2
        
    if S.count(1) == len(S):
        return ret+len(S)//2
        
    ret += 2*(len(S)//2)
    return ret
            
def convert(S):
    S += '#'
    i = 0
    ret = []
    for j in range(1, len(S)):
        if S[j] != S[i]:
            ret.append(j-i)
            i = j
    return ret
    
for _ in range(int(input())):
    S = input()
    print(min(solve(convert(S)), S.count('1'), S.count('0')))