def numBits(n):
	c = 0
	while n:
		n &= (n-1)
		c += 1
	return c
	
for _ in xrange(input()):
	A, B = map(int, raw_input().split())
	if A == B:
		print 0
	elif A == 0 and B == 1:
		print 1
	elif B <= 1:
		print -1
	else:
		nA, nBm1 = numBits(A), numBits(B-1)
		if nA == nBm1:
			print 1
		elif nBm1 > nA:
			print nBm1-nA+1
		else:
			print 2