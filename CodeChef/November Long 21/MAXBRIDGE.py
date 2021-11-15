for _ in range(int(input())):
    N, M = list(map(int, input().split()))
    for i in range(N-1):
        print(i+1, i+2)
    M -= (N-1)
    for i in range(N-2, 0, -1):
        for j in range(i+2, N+1):
            if M:
                print(i, j)
                M -= 1
            else:
                break
        else:
            continue
        break