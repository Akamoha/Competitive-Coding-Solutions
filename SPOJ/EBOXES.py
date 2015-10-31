for _ in range(input()):
	N, K, T, F = map(int, raw_input().split())
	print N + K*(F-N)/(K-1)