for _ in xrange(input()):
	A, B = raw_input(), raw_input()
	DP = [[0 for _ in xrange(2050)] for _ in xrange(2050)]
	for j in xrange(len(A)+1):
		DP[0][j] = j
	for i in xrange(len(B)+1):
		DP[i][0] = i
	for i in xrange(1, len(B)+1):
		for j in xrange(1, len(A)+1):
			if A[j-1] == B[i-1]:
				DP[i][j] = DP[i-1][j-1]
			else:
				DP[i][j] = 1 + min(DP[i][j-1], DP[i-1][j], DP[i-1][j-1])
	print DP[len(B)][len(A)]