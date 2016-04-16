for t in xrange(input()):
	N = input()
	HT = {}
	for _ in xrange(2*N-1):
		L = map(int, raw_input().split())
		for l in L:
			if l not in HT:
				HT[l] = 1
			else:
				HT[l] += 1
	answer = []
	for l in HT:
		if HT[l]%2 != 0:
			answer.append(l)
	answer.sort()
	print "Case #"+str(t+1)+":",
	for l in answer:
		print l,
	print