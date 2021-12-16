for _ in range(int(input())):
    N, M = list(map(int, input().split()))
    if N == M:
        ans = "01"*(N+1)
    elif N > M:
        ans = "0" + "10"*(M+1) + "010"*(N-M-1)
    else:
        ans = "1" + "01"*(N+1) + "101"*(M-N-1)
    print(len(ans))
    print(ans)