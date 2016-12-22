N, K = map(int, raw_input().split())
T = [0 for _ in xrange(N+1)]
for _ in xrange(K):
	s = raw_input()
	if s[:3] == "CLI":
		i = int(s[6:])
		T[i] = 1 - T[i]
	else:
		T = [0 for _ in xrange(N+1)]
	print sum(T)