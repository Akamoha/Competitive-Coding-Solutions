N, M = map(int, raw_input().split())
A = []
DP = []
	
MAX = 1000000
for _ in range(N):
	A.append(map(int, raw_input().split()))
	zeros = []
	for i in range(M+2):
		zeros.append(MAX)
	DP.append(zeros)

DP[0] = [MAX] + A[0] + [MAX]
for i in range(1, N):
	for j in range(1, M+1):
		DP[i][j] = A[i][j-1] + min(DP[i-1][j-1:j+2])
print min(DP[N-1])