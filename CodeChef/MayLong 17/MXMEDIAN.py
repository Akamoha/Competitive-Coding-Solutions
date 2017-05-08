for _ in xrange(input()):
	N = input()
	A = map(int, raw_input().split())
	A.sort()
	print A[N:][N/2]
	for i in xrange(N):
		print A[i], A[N+i],
	print