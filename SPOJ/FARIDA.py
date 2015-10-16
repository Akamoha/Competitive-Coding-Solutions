for t in range(input()):
	N = input()
	A = map(int, raw_input().split())
	DP = [0, 0] + A
	for i in range(2, N+2):
		DP[i] = max(DP[i-2]+A[i-2], DP[i-1])
	print "Case "+str(t+1)+": "+str(DP[N+1])