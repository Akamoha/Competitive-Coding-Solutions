for _ in xrange(input()):
	N = input()
	A = map(int, raw_input().split())
	A.sort()
	print A[0]+A[1]