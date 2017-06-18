for _ in xrange(input()):
	n, b = map(int, raw_input().split())
	B = n/2+1
	A = (B+1)/2 + (B+1)%2
	if n == 2:
		if b == 0:
			print "NO"
			continue
		else:
			print "YES"
			print 1, 2
			continue
	if B-A < b:
		print "NO"
		continue
	if b == 0:
		print "YES"
		for i in xrange(2, n+1):
			print 1, i
		continue
	print "YES"
	ghata = 2*(B-A-b)
	for i in xrange(1+ghata, B):
		print i, i+1
	for i in xrange(B+1, n+1):
		print B, i
	for i in xrange(1, 1+ghata):
		print i, 2+ghata