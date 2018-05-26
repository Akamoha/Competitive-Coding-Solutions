for _ in xrange(input()):
	n = input()
	A = map(int, raw_input().split())
	ht = {}
	for a in A:
		if a not in ht:
			ht[a] = 0
		ht[a] += 1
	for a in A:
		if ht[a] > n/2:
			print a
			break
	else:
		print "NO MAJOR"