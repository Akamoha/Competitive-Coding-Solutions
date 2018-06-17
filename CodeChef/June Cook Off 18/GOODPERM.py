import itertools as it

def check(p):
	B = [a for a in A]
	j = 0
	for i in empty:
		B[i] = p[j]
		j += 1
	c = 0
	for i in xrange(1, N):
		if B[i] > B[i-1]:
			c += 1
		if c > K:
			return 0
	if c == K:
		return 1
	return 0

for _ in xrange(input()):
	N, K = map(int, raw_input().split())
	A = map(int, raw_input().split())
	empty = []
	ht = {}
	for i in xrange(N):
		if A[i] == 0:
			empty.append(i)
		else:
			ht[A[i]] = 1
	sub = [item for item in range(1, N+1) if item not in ht]
	ans = 0
	for p in list(it.permutations(sub)):
		ans += check(p)
	print ans