N, K, P = map(int, raw_input().split())
AA = map(int, raw_input().split())
A = []
for i in xrange(N):
	A.append((AA[i], i))
A.sort()
bucket = {}
b = 1
bucket[A[0][1]] = b
for i in xrange(1, N):
	if A[i][0] - A[i-1][0] > K:
		b += 1
	bucket[A[i][1]] = b

for _ in xrange(P):
	A, B = map(int, raw_input().split())
	print "Yes" if bucket[A-1] == bucket[B-1] else "No"
	