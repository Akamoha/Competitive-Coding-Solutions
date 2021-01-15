for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    for i in range(1, k-n+k):
        print(i, end=' ')
    for i in range(k, k-n+k-1, -1):
        print(i, end=' ')
    print()