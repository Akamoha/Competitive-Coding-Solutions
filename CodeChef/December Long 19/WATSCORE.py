for _ in range(int(input())):
    N = int(input())
    A = [0]*12
    for __ in range(N):
        p, s = list(map(int, input().split()))
        A[p] = max(A[p], s)
    print(sum(A[:9]))