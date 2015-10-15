for _ in range(input()):
	N, K = map(int, raw_input().split())
	heights = map(int, raw_input().split())
	heights.sort()
	mini = 1000000001
	for i in range(0, N-K+1):
		if heights[i + K - 1] - heights[i] < mini:
			mini = heights[i + K - 1] - heights[i]
	print mini