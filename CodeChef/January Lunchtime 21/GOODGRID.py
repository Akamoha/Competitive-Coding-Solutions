for _ in range(int(input())):
    N, X = list(map(int, input().split()))
    for i in range(1, N+1):
        if X%i == 0 and X/i <= N:
            print("Yes")
            break
    else:
        print("No")