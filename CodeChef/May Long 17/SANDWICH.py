for _ in xrange(input()):
	N, K, M = map(int, raw_input().split())
	if K > N:
		K = N
	if N%K == 0:
		print N/K, 1
		continue
	numPieces = N/K + 1
	DP = []
	for i in xrange(N+10):
		DP.append([0 for j in xrange(numPieces+10)])
	for i in xrange(1, K+1):
		DP[i][1] = 1
	for j in xrange(2, numPieces+1):
		DP[1][j] = 0

	for i in xrange(2, N+1):
		for j in xrange(2, numPieces+1):
			for k in xrange(1, K+1):
				DP[i][j] = (DP[i][j] + DP[i-k][j-1])%M

	# for i in xrange(1, N+1):
	# 	for j in xrange(1, numPieces+1):
	# 		print DP[i][j],
	# 	print
	print numPieces, DP[N][numPieces]%M