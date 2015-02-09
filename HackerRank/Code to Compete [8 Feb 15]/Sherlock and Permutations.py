import math
T = int(raw_input())
for _ in range(T):
    N, M = map(int, raw_input().split())
    M -= 1
    print (math.factorial(M+N)/(math.factorial(N)*math.factorial(M)))%(10**9 + 7)
