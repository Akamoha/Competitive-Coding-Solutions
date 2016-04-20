N = input()
A = map(int, raw_input().split())
DP = [1 for _ in xrange(N)]
for i in xrange(1, N):
	for j in xrange(i):
		if A[j] < A[i]:
			DP[i] = max(DP[i], DP[j]+1)
print max(DP)