for _ in range(int(input())):
    N = input()
    A = list(map(int, input().split()))
    L = [0, 0, 0]
    for a in A:
        if a in (0, 2):
            L[a] += 1
    print((L[0]*(L[0]-1)+L[2]*(L[2]-1))//2)