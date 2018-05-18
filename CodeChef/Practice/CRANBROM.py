n = input()
ht = {}
DP = [0 for _ in xrange(n)]
for i in xrange(n):
	event, L = raw_input().split()
	L = int(L)
	if event == 'found':
		DP[i] = DP[i-1]
		ht[L] = i
	else:
		if L in ht:
			DP[i] = max(DP[i-1], L+DP[ht[L]])
		else:
			DP[i] = DP[i-1]
print DP[n-1]