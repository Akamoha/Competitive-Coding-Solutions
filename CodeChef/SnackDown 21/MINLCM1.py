for _ in range(int(input())):
    X, K = list(map(int, input().split()))
    print(X*2, X*K*(X*K-1))