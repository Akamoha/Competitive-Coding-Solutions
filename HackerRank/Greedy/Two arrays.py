for _ in range(input()):
    N, K = map(int, raw_input().split())
    A = map(int, raw_input().split())
    B = map(int, raw_input().split())
    A.sort()
    B.sort()
    for i in range(N):
        for j in range(len(B)):
            if A[i] + B[j] >= K:
                B.pop(j)
                i -= 1
                j = "ALL OK"
                break
        if j != "ALL OK":
            print "NO"
            break
    else:
        print "YES"