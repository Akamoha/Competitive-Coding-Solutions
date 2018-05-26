for _ in xrange(input()):
	m, n = map(int, raw_input().split())
	grid = []
	DP = []
	for __ in xrange(m):
		grid.append(map(int, raw_input().split()))
		DP.append([0 for ___ in xrange(n)])
	i = 0
	for j in xrange(n):
		DP[i][j] = grid[i][j]
	j = 0
	for i in xrange(m):
		DP[i][j] = grid[i][j]
	mx = 0
	for i in xrange(1, m):
		for j in xrange(1, n):
			if grid[i][j] == 1:
				DP[i][j] = 1 + min(DP[i-1][j], DP[i][j-1], DP[i-1][j-1])
				mx = max(mx, DP[i][j])
	print mx