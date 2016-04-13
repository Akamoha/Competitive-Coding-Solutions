for _ in xrange(input()):
	N = input()
	S = raw_input()
	HT = {}
	for s in S:
		if s not in HT:
			HT[s] = 1
		else:
			HT[s] += 1
	print N - max(HT.values())