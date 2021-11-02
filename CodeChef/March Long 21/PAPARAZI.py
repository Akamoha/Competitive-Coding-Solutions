import sys
def get_ints():
    return map(int, sys.stdin.readline().strip().split())

for t in range(int(input())):
    N = int(input())
    A = [(i, v) for (i, v) in enumerate(get_ints())]
    S = A[0:2]
    ans = 1
    for i in range(2, N):
        while len(S) >= 2:
            m1 = (S[-1][1]-S[-2][1])/(S[-1][0]-S[-2][0])
            m2 = (A[i][1]-S[-1][1])/(A[i][0]-S[-1][0])
            if m1 > m2:
                break
            S.pop()
        S.append(A[i])
        ans = max(ans, S[-1][0]-S[-2][0])
    sys.stdout.write(str(ans)+'\n');