MOD = 10**9+7
for _ in xrange(input()):
	N, K = map(int, raw_input().split())
	print ((pow(K-1, N-1, MOD)%MOD)*(K%MOD))%MOD