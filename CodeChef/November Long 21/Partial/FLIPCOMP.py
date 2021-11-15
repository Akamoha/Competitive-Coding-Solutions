def solve(S):
    if len(S) == S.count('0') or len(S) == S.count('1'):
        return 0
    ret = len(S)
    if S[0] != S[1]:
        ret = min(ret, 1+solve(S[1]+S[1:]))
    if S[-1] != S[-2]:
        ret = min(ret, 1+solve(S[:-1]+S[-2]))
    for i in range(1, len(S)-1):
        if S[i-1:i+2] in ['010', '101']:
            ret = min(ret, 1+solve(S[:i]+S[i-1]+S[i+1:]))
    i, j = 0, 1
    while j < len(S):
        if S[i] != S[j]:
            if j-i > 1:
                ret = min(ret, 2+solve(S[:i]+S[j]+S[j:]))
            i, j = j, j+1
        else:
            j += 1
    return ret

for _ in range(int(input())):
    X = input()
    print(solve(X))