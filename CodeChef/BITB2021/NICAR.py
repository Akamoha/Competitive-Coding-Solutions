n = int(input())
C = list(map(int, input().split()))
N = [0]
for i in range(n):
    a = C[i]+N[i]
    N.append(max(N[i], a))
    print(a, end=' ')
print()