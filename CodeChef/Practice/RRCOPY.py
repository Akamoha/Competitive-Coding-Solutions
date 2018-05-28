for _ in xrange(input()):
	N = input()
	A = map(int, raw_input().split())
	HT = {}
	for a in A:
		HT[a] = 1
	print len(HT)