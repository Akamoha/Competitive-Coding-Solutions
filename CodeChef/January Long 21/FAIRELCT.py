def read_input():
    return list(map(int, input().split()))

for _ in range(int(input())):
    N, M = read_input()
    A = read_input()
    B = read_input()
    A.sort()
    B.sort()
    i, j = 0, M-1
    vA, vB = sum(A), sum(B)
    if vA > vB:
        print(0)
        continue
    swaps = 0
    while i < N and j >= 0:
        vA += B[j] - A[i]
        vB += A[i] - B[j]
        swaps += 1
        if vA > vB:
            break
        i += 1
        j -= 1
    if vA > vB:
        print(swaps)
    else:
        print(-1)