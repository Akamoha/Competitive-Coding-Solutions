for _ in range(int(input())):
    S = '#'+input()
    N = len(S)
    A = ['' for _ in range(N)]
    A[N-1] = ('.', N)
    cur = S[N-1]
    idx = N-1
    for i in range(N-2, -1, -1):
        A[i] = (cur, idx)
        if S[i] <= cur:
            cur = S[i]
            idx = i
    cur, i = A[0]
    prefix = cur
    take = S[1:i]
    sth = S[1:]
    while True:
        prv = i
        nxt, i = A[i]
        if i == N:
            break
        if nxt == cur:
            prefix += nxt
            take += S[prv+1:i]
        else:
            if len(take) == 0:
                cur = nxt
                prefix += nxt
                take += S[prv+1:i]
            elif take[0] < nxt:
                take += S[prv+1:]
                break
            elif take[0] > nxt:
                cur = nxt
                prefix += nxt
                take += S[prv+1:i]
            else:
                sth = min(sth, prefix + take + S[prv+1:])
                cur = nxt
                prefix += nxt
                take += S[prv+1:i]
                
    print(min(prefix+take, sth))