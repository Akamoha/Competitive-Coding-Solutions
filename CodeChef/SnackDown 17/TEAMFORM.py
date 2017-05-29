for _ in xrange(input()):
	n, m = map(int, raw_input().split())
	for i in xrange(m):
		u, v = map(int, raw_input().split())
	print "yes" if (n-2*m)%2 == 0 else "no"