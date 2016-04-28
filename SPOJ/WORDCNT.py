for _ in xrange(input()):
	S = raw_input().split()
	mx = 0
	cur = 0
	l = len(S[0])
	for s in S:
		if len(s) == l:
			cur += 1
		else:
			cur = 1
			l = len(s)
		mx = max(cur, mx)
	print mx