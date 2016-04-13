for _ in xrange(input()):
	N, M = map(int, raw_input().split())
	if N == 1 and M == 2:
		print "Yes"
	elif N == 2 and M == 1:
		print "Yes"
	elif N == 1 or M == 1:
		print "No"
	else:
		print "Yes" if N%2 == 0 or M%2 == 0 else "No"