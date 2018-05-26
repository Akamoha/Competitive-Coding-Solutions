for _ in xrange(input()):
	n = input()
	A = map(int, raw_input().split())
	L = [0 for _ in xrange(n)]
	R = [0 for _ in xrange(n)]
	s = 0
	for i in xrange(n):
		s += A[i]
		L[i] = s
	s = 0
	for i in xrange(n-1, -1, -1):
		s += A[i]
		R[i] = s
	for i in xrange(n):
		if L[i] == R[i]:
			print A[i]
			break
	else:
		print "NO EQUILIBRIUM"