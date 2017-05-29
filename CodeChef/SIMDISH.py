for _ in xrange(input()):
	ht = {}
	for dish in raw_input().split():
		ht[dish] = 1
	for dish in raw_input().split():
		ht[dish] = 1
	print "similar" if len(ht) <= 6 else "dissimilar"