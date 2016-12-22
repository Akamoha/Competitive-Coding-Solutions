for _ in xrange(input()):
	N, B, M = map(int, raw_input().split())
	T = -B
	while N > 0:
		T += B
		if N%2 == 0:
			T += N/2*M
			N /= 2
		else:
			T += ((N+1)/2)*M
			N -= (N+1)/2
		M *= 2
	print T