for _ in range(int(input())):
    N = int(input())
    B = list(map(int, input().split()))
    B = [(B[i], i) for i in range(N)]
    B.sort()
    curr = -1
    A = [0 for i in range(N)]
    for b, i in B:
        if curr+1 < b:
            curr += 1
        A[i] = curr
    print(' '.join(list(map(str,A))))