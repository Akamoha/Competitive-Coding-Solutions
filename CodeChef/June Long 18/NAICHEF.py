def inp():
	return map(int, raw_input().split())

for _ in xrange(input()):
	N, A, B = inp()
	X = inp()
	HT = {}
	HT[A], HT[B] = 0, 0
	for x in X:
		if x not in HT:
			HT[x] = 0
		HT[x] += 1
	print 1.0*HT[A]*HT[B]/(N*N)