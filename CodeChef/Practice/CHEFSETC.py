for _ in xrange(input()):
	L = map(int, raw_input().split())
	sums = []
	for i in xrange(1, 16):
		s = 0
		b = '{0:04b}'.format(i)
		for j in xrange(4):
			if b[j] == '1':
				s += L[j]
		sums.append(s)
	print "Yes" if 0 in sums else "No"