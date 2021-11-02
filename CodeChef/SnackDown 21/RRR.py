for _ in range(int(input())):
    N, K = list(map(int, input().split()))
    print(2* (N-K + K//2 + K%2 - 1))