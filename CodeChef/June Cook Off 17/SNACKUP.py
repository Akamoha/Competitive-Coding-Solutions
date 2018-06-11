for _ in xrange(input()):
	n = input()
	print n
	if n == 2:
		print 2
		print "1 1 2"
		print "2 1 2"
		print 2
		print "1 1 2"
		print "2 1 2"
		continue
	a = 1
	for r in xrange(n-1):
		print n
		for j in xrange(n):
			print j+1, a, a+1
		a += 1
	print n
	for j in xrange(n):
		print j+1, 1, n