n, m = map(int, raw_input().split())
A = map(int, raw_input().split())
CSA = [0 for _ in xrange(n)]
CSA[0] = A[0]
for i in xrange(1, n):
	CSA[i] = CSA[i-1]+A[i]
ans = 0
for _ in xrange(m):
	l, r = map(int, raw_input().split())
	l -= 1
	r -= 1
	sm = CSA[r] - CSA[l] + A[l]
	if sm > 0:
		ans += sm
print ans