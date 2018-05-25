def solve(N):
	return 2*(N*(N-1) + N*(N-1)*(N-2)) + N*(N-1)*(N-2) + N*(N-1)*(N-2) + N*(N-1)*(N-2)*(N-3) + N*(N-1)*(N-2) + N*(N-1)*(N-2)*(N-3)

for _ in xrange(input()):
	print solve(input())
